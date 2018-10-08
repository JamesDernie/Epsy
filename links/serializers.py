# Rest
from rest_framework import serializers

# Models
from .models import Link
# Serializers
from tags.serializers import TagSerializer


class LinkSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Link
        fields = ('id', 'url', 'image_url', 'title', 'description', 'content_url', 'tags', )
