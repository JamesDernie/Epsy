# Django Imports
from django.db import models


class Link(models.Model):
    profile = models.ForeignKey('profiles.Profile', related_name='links', on_delete=models.CASCADE)

    url = models.URLField(null=True, blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)

    folders = models.ManyToManyField('folders.Folder')
    tags = models.ManyToManyField('tags.Tag', null=True, blank=True)

    def __str__(self):
        return self.title
