# Rest
from rest_framework import serializers

# Models
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(
        read_only=True,
        required=False,
    )

    class Meta:
        model = Tag
        fields = ('name', 'count', )