# Rest
from rest_framework import serializers

# Models
from .models import Profile

# Serializers
from links.serializers import LinkSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('url', 'id', 'first_name', 'last_name', 'display_name', 'links', )