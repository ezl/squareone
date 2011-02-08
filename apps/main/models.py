# so that south can introspect the django_extensions custom fields
# as per http://south.aeracode.org/docs/customfields.html#where-to-put-the-code
# there is no specific location this should go in.
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django_extensions\.db\.fields"])

from django.db import models

