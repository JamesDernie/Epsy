# Rest
from rest_framework import serializers

# Models
from .models import Folder


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('path', )
