# Django Imports
from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token



# App Urls
urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Auth
    path(r'api/', include('rest_auth.urls')),
    path(r'api/registration/', include('rest_auth.registration.urls')),
    path(r'api/refresh-token/', refresh_jwt_token),
    path(r'api/api-token-verify/', verify_jwt_token),

    # Apps Urls
    path('api/', include('links.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/scraper/', include('scraper.urls')),
    path('api/tags/', include('tags.urls')),
    path('api/users/', include('users.urls')),

]
