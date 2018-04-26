from django.contrib import admin

# Model Imports
from .models import User
from profiles.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]


admin.site.register(User, UserAdmin)
