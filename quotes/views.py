from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from .models import Quote
from .forms import QuoteForm

def home(request):
    return quote_list(request, sort='latest', quote_query=Quote.objects.all()[:5])


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

