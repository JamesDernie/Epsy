# Rest
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Django
from django.db.models import Q, Count
from django.utils.datastructures import MultiValueDictKeyError
# Models
from .models import Link
from folders.models import Collection
from tags.models import Tag
# Serializers
from .serializers import LinkSerializer
# Python
from functools import reduce
from urllib.parse import urlparse
import re


class LinkViewSet(viewsets.ModelViewSet):
    """
    API end point that allows links to be viewed, created, edited or deleted
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = self.queryset.filter(profile=self.request.user.profile).prefetch_related('tags')
        tags = self.request.GET.getlist('tag[]', None)
        q = self.request.GET.get('queryString', None)

        # Filter by tags, order by number of matching tags
        if tags:
            tag_query = reduce(lambda q, tag: q | Q(tags__name=tag), tags, Q())
            qs = qs.filter(tag_query).order_by('-count', 'id').annotate(count=Count('id'))

        # Filter by query string
        if q:
            query = (
                Q(title__icontains=q) |
                Q(url__icontains=q) |
                Q(description__icontains=q) |
                Q(tags__name__icontains=q)
            )
            qs = qs.filter(query).order_by('-count', 'id').annotate(count=Count('id'))

        return qs
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            url = request.data['url']
            parsed_uri = urlparse(url)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            domain = re.sub(r'(www.|.com)', '', string=domain)

            m = serializer.save(profile=request.user.profile, domain=domain)

            # Parse tags string and create tags for link
            try:
                tags_str = request.data['tags_str']
            except MultiValueDictKeyError:
                tags_str = None

            if tags_str:
                tags_list = [s.strip() for s in tags_str.split(',')]
                Tag.objects.bulk_create([
                    Tag(link=m, name=tag.lower()) for tag in tags_list
                ])

            return Response(LinkSerializer(m).data)

        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            obj = self.queryset.get(id=pk)
        except Link.DoesNotExist:
            return Response(
                'This link does not exist or you do not have permission to access it',
                status=404,
            )
        serializer = self.serializer_class(obj, data=request.data)

        if serializer.is_valid():
            m = serializer.save()

            try:
                tags_str = request.data['tags_str']
            except MultiValueDictKeyError:
                tags_str = None

            if tags_str:
                tags_list = [s.strip() for s in tags_str.split(',')]
                Tag.objects.bulk_create([
                    Tag(link=m, name=tag.lower()) for tag in tags_list
                ])

            return Response(LinkSerializer(m).data)

        else:
            return Response(serializer.errors, status=400)
