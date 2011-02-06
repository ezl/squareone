from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
# from django.contrib.auth.views import password_change


urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', {'next_page':'/'}, name='logout'),
    url(r'^register/$', 'register', name='register'),
    url(r'^settings/$', 'user_settings', name='accounts_user_settings'),
    url(r'^change_password/$', 'change_password', name='accounts_change_password'),
)
