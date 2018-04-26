# Rest
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from .models import Link

# Serializers
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    """
    API end point that allows links to be viewed, created, edited or deleted
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset.filter(profile=self.request.user.profile)
        return qs



