from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'main.views.helloworld', name='helloworld'),
    url(r'^accounts/login/$', 'accounts.views.login', name='login'),
    url(r'^accounts/logout/$', 'accounts.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^apply/(?P<url_hash>(\w|-)+)/$', 'applications.views.apply', name='application'),
)

# includes
urlpatterns += patterns('',
    (r'^accounts/', include('accounts.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^adminfiles/', include('adminfiles.urls')),
    (r'^applications/', include('applications.urls')),
    (r'^mailing/', include('mailer.urls')),
    (r'^notifications/', include('notification.urls')),
    (r'^rentals/', include('rentals.urls')),
)

# dev niceties
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^raw_template/(?P<template>.*)', 'django.views.generic.simple.direct_to_template'),
        (r'^messages_test/$', 'main.views.messages_test'),
    )
