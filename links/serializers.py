# Rest
from rest_framework import serializers

# Models
from .models import Link

# Serializers
from folders.serializers import FolderSerializer
from tags.serializers import TagSerializer


class LinkSerializer(serializers.ModelSerializer):
    folders = FolderSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Link
        fields = ('id', 'url', 'title', 'description', 'comment', 'folders', 'tags', )