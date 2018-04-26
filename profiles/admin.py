# Django Imports
from django.contrib import admin

# Models
from .models import Profile
from links.models import Link


class LinkInline(admin.TabularInline):
    model = Link


class ProfileAdmin(admin.ModelAdmin):
    inlines = [LinkInline, ]


admin.site.register(Profile, ProfileAdmin)
