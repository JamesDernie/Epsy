# Django
from django.contrib.auth import get_user_model
# Rest
from rest_framework import serializers
# Models
from .models import User

# Get the UserModel
UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'date_joined', 'is_staff', )


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'email', )
        read_only_fields = ('email', )