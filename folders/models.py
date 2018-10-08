from django.db import models


class Collection(models.Model):
    profile = models.ForeignKey('profiles.Profile', related_name='collections', on_delete=models.CASCADE)

    domain = models.URLField()
