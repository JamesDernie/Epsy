# Django Imports
from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import refresh_jwt_token


# App Urls
urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Auth
    path(r'', include('rest_auth.urls')),
    path(r'registration/', include('rest_auth.registration.urls')),
    path(r'refresh-token/', refresh_jwt_token),

    # Apps Urls
    path('links/', include('links.urls')),
    path('profiles/', include('profiles.urls')),
    path('users/', include('users.urls')),

]
