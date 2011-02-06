from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
# from django.contrib.auth.views import password_change
from django.contrib.auth.forms import PasswordChangeForm

    
urlpatterns = patterns('accounts.views',
    url(r'^register/$', 'register', name='accounts_register'),
    url(r'^settings/$', 'user_settings', name='accounts_user_settings'),
    url(r'^change_password/$', 'change_password', name='accounts_change_password'),
)
