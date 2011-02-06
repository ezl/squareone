# so that south can introspect the django_extensions custom fields
# as per http://south.aeracode.org/docs/customfields.html#where-to-put-the-code
# there is no specific location this should go in.
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_extensions\.db\.fields"])


# to work with django-notifications we need to create notice_types
# from django.db import models
# from.django.conf import settings
# 
# if 'notification' in settings.INSTALLED_APPS:
#     from notification import models as notification
# 
#     def create_notice_types(app, created_models, verbosity, **kwargs):
#         notification.create_notice_type()
#         notification.create_notice_type()
#     models.signals.post_syncdb.connect(create_notice_types, sender=notification)