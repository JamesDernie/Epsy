# Django Imports
from django.urls import path, include

# Rest
from rest_framework import routers

# Views
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


# App Urls
urlpatterns = [
    path(r'', include(router.urls)),
]