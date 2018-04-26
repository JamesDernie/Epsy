from django.db import models


class Tag(models.Model):
    profile = models.ForeignKey('profiles.Profile', related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('profile', 'name', )

    def __str__(self):
        return self.name
