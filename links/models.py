# Django Imports
from django.db import models
from django.utils import timezone


class Link(models.Model):
    profile = models.ForeignKey('profiles.Profile', related_name='links', on_delete=models.CASCADE)

    url = models.URLField(null=True, blank=True)
    domain = models.CharField(max_length=255)

    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)

    # Special content, eg youtube video embed url, imgur img url
    content_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at', 'id')

    def __str__(self):
        return self.title
