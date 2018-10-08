# Rest Framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Requests
import requests
from requests.exceptions import MissingSchema, InvalidSchema

# Beautiful Soup
from bs4 import BeautifulSoup

from .exceptions import NoUrlProvided
from .scrape import scrape


class GetLinkProperties(APIView):
    """
    Accepts a url parameter and return properties for that url
    """
    permission_classes = (IsAuthenticated, )

    def get_link(self, request):
        url = request.GET.get('url', None)
        if url:
            return url
        else:
            raise NoUrlProvided()

    def get(self, request, format=None):

        url = self.get_link(request)

        try:
            result = requests.get(url, headers={'User-agent': 'Epsy__{}'.format(request.user.id)})
        except (MissingSchema, InvalidSchema):
            return Response('Please provide a valid url', status=400)
        else:
            c = result.content
            soup = BeautifulSoup(c, "lxml")
            print(soup)
            data = scrape(soup, url)

            return Response(data)
