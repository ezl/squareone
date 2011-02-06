def get_redirect_url(request, redirect_url=None, redirect_field_name='next',
                    fallback='/'):
    if not redirect_url:
        redirect_url = request.REQUEST.get(redirect_field_name, '')
    # see contrib.auth.views.login for the rationale of these checks.
    if not redirect_url or ' ' in redirect_url:
        redirect_url = fallback
    elif '//' in redirect_url and re.match(r'[^\?]*//', redirect_url):
        redirect_url = fallback
    return redirect_url
