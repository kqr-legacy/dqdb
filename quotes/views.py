from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError

from ipware.ip import get_ip

from .models import Quote, Vote
from .forms import QuoteForm

def home(request):
    return quote_list(
        request, sort='latest',
        quote_query=Quote.objects.all()[:5]
    )


def quote_list(request, sort, page=None, quote_query=None):
    default_queryset = {
        'latest': Quote.objects.all(),
        'highest': Quote.top.all(),
        'random': Quote.objects.order_by('?'),
    }[sort]
    queryset = quote_query or default_queryset

    paginator = Paginator(queryset, 15)
    try:
        quotes = paginator.page(page or 1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    return render(request, 'quotes/list.html', {
        'quotes': quotes,
        'sort': sort,
    })


def quote_single(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except ValueError:
        quote = get_object_or_404(Quote, legacy_hash=id)
        
    return render(request, 'quotes/single.html', {'quote': quote})


def search(request, terms=None):
    terms = terms or request.GET.get('q', None)
    if terms:
        return quote_list(
            request, sort='latest',
            quote_query=Quote.objects.filter(text__icontains=terms)
        )

    return render(request, 'quotes/search.html')


@login_required
def add(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.submitter = request.user
            quote.save()
            return redirect('quotes:home')
    else:
        form = QuoteForm

    return render(request, 'quotes/add.html', {'form': form})


def vote(request, id):
    quote = get_object_or_404(Quote, id=id)

    res = {'err': None}
    try:
        Vote(voter=get_ip(request), quote=quote).save()
    except IntegrityError:
        # IntegrityError = person has already voted for that quote.
        # That's okay, we just don't save that vote and go on with
        # our lives!
        pass
    except Exception as e:
        res = {'err': str(e)}

    # Intentionally making a new count instead of just re-using score.
    return JsonResponse(dict(res, count=quote.votes.count()))


