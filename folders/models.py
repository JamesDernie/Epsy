from django.db import models


class Folder(models.Model):
    """
    Folder model for links
    Categories can have sub categories, and are linked to a users profile
    """
    profile = models.ForeignKey('profiles.Profile', related_name='folders', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='sub_folders', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    path = models.CharField(max_length=1000, null=True, blank=True, unique=True)

    def __str__(self):
        return self.path

