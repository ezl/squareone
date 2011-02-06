from django.conf import settings
from django.http import HttpResponseRedirect, get_host


def request_is_secure(request):
    if request.is_secure():
        return True

    # Handle forwarded SSL (used at Webfaction)                                                           
    if 'HTTP_X_FORWARDED_SSL' in request.META:
        return request.META['HTTP_X_FORWARDED_SSL'] == 'on'

    if 'HTTP_X_SSL_REQUEST' in request.META:
        return request.META['HTTP_X_SSL_REQUEST'] == '1'

    return False


class SSLRedirectMiddleware(object):
    def process_request(self, request):
        if request_is_secure(request):
            request.IS_SECURE=True
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None
        if settings.DEBUG:
            return None
        if not request_is_secure(request):
            return self._redirect(request)

    def _redirect(self, request):
        if settings.DEBUG and request.method == 'POST':
            raise RuntimeError(
            """Django can't perform a SSL redirect while maintaining POST data.                           
                Please structure your views so that redirects only occur during GETs.""")
        newurl = 'http://%s%s' % (get_host(request), request.get_full_path())
        return HttpResponseRedirect(newurl)

