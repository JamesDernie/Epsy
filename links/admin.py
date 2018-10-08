# Django
from django.contrib import admin
# Models
from .models import Link
from tags.models import Tag


class TagInline(admin.TabularInline):
    model = Tag


class LinkAdmin(admin.ModelAdmin):
    inlines = (TagInline, )


admin.site.register(Link, LinkAdmin)