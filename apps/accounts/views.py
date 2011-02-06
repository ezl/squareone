import re

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import (logout as auth_logout,
                                       password_change as auth_password_change)
from django.contrib.auth import authenticate, login as auth_raw_login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site, RequestSite
from django.core.urlresolvers import resolve, reverse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.generic.simple import direct_to_template

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from utils import get_redirect_url


@csrf_protect
@never_cache
def login(request, template_name='accounts/login.html',
          redirect_field_name='next', authentication_form=AuthenticationForm,
          extra_context={}):
    """
    contrib.auth.views.login, but with a few added benefits: extra_context and
    it redirects to settings.LOGIN_REDIRECT_URL if user is already logged in.
    """
    redirect_to = get_redirect_url(request, redirect_field_name=redirect_field_name,
                                   fallback=settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = authentication_form(data=request.POST)
        if form.is_valid():
            auth_raw_login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)
    request.session.set_test_cookie()
    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)
    context = {
        'form': form,
        # 'registration_form': AuthenticationForm(), [ for creating a login/register page]
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name
    }
    context.update(extra_context)
    return direct_to_template(request, template_name, context)


def logout(request, next_page='/'):
    messages.success(request, "You've been successfully logged out.")
    return auth_logout(request, next_page=next_page)


def register(request, redirect_field_name='next', user_type='landlord',
             template_name='accounts/register.html'):
    redirect = request.REQUEST.get(redirect_field_name, '')
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            auth_raw_login(request, user)
            messages.success(request, 'Registration successful.')
            redirect_to = get_redirect_url(request, redirect_field_name=redirect_field_name,
                                           fallback=settings.LOGIN_REDIRECT_URL)
            return HttpResponseRedirect(redirect_to)
    else:
        form = UserCreationForm()
    return direct_to_template(request, template_name, locals())

@login_required
def user_settings(request, template_name='accounts/user_settings.html'):
    return direct_to_template(request, template_name, locals())

@login_required
def change_password(request):
    resp = auth_password_change(request,
            post_change_redirect=reverse('accounts_user_settings'),
            template_name='accounts/change_password.html')
    if resp.status_code == 302:
        # auth_password_change is redirecting, so it succeeded
        messages.success(request, 'Your password has been changed successfully.')
    return resp

