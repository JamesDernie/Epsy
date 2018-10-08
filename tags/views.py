# Rest
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Models
from .models import Tag
# Serializers
from .serializers import TagSerializer

from django.db.models import Count


class TagViewSet(viewsets.ModelViewSet):
    """
    API end point that allows links to be viewed, created, edited or deleted
    """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset\
            .filter(link__profile=self.request.user.profile)\
            .values('name') \
            .order_by('-count', 'name') \
            .annotate(count=Count('name'))
        return qs
