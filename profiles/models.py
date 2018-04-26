# Django Imports
from django.db import models

# Other
from annoying.fields import AutoOneToOneField


class Profile(models.Model):
    user = AutoOneToOneField('users.User', related_name='profile', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

    def save(self, *args, **kwargs):
        self.display_name = '{} {}'.format(self.first_name, self.last_name)
        super(Profile, self).save(*args, **kwargs)
