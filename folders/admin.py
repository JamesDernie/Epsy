# Django
from django.contrib import admin
# Models
from .models import Folder
# Forms
from .forms import FolderForm


class FolderAdmin(admin.ModelAdmin):
    form = FolderForm
    search_fields = (
        'path',
        'name',
        'profile__display_name',
    )

admin.site.register(Folder, FolderAdmin)

