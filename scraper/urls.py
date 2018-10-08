# Django
from django.urls import path, include

# Views
from . import views


# App Urls
urlpatterns = [
    path(r'get-link-properties/', views.GetLinkProperties.as_view(), name='get_link_properties'),
]