# Django
from django import forms

# Models
from .models import Link


class CreateLinkForm(forms.ModelForm):
    tags = forms.CharField()

    class Meta:
        model = Link
        fields = ['url', 'icon', 'title', ]

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('request', None)
        super(CreateLinkForm, self).__init__(*args, **kwargs)

