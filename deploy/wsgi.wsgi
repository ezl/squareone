import site
site.addsitedir('/home/%(project_username)s/env/lib/python2.6/site-packages')

import sys
sys.path.append('/home/%(project_username)s')
sys.path.append('/home/%(project_username)s/%(project_name)s')
sys.path.append('/home/%(project_username)s/%(project_name)s/apps')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.%(django_settings)s'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
