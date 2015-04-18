from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^single/(?P<id>[0-9a-z]+)', views.quote_single, name='single'),
    url(r'^(?P<sort>latest|highest|random)/$', views.quote_list, name='list'),
    url(r'^(?P<sort>latest|highest|random)/p(?P<page>[0-9]+)/$', views.quote_list, name='list'),
    url(r'^add/$', views.add, name='add'),
]
