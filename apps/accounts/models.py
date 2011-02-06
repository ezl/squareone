from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User)
    def __unicode__(self):
        s = '%s' % self.user
        return s

def create_profile(sender, instance, created, **kwargs):
    if instance is None or not created:
        return
    UserProfile.objects.create(user=instance)
models.signals.post_save.connect(create_profile, sender=User)
