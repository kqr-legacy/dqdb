import re
from django.template import Library
from django.core.urlresolvers import reverse
from ipware.ip import get_ip

register = Library()


@register.simple_tag(takes_context=True)
def set_vote_class(context, quote):
    if quote.votes.filter(voter=get_ip(context['request'])).exists():
        quote.vote_class = 'disabled'
    return ''


@register.simple_tag(takes_context=True)
def active(context, view, **kwargs):
    if re.match(reverse(view, kwargs=kwargs), context['request'].path):
        return 'active'
    else:
        return ''
