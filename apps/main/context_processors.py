from django.contrib.sites.models import RequestSite


def request_site(request):
    return {'site': RequestSite(request)}