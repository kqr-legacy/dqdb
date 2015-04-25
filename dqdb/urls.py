from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views as auth

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', auth.login, name='login'),
    url(r'^accounts/logout/', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include('quotes.urls', namespace='quotes')),
]
