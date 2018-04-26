# Python
from collections import deque
# Django
from django import forms
# Models
from .models import Folder


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        exclude = []

    def save(self, commit=True):
        m = super(FolderForm, self).save(commit=False)
        # Create path name
        parent = m.parent
        parent_list = deque()
        parent_list.appendleft(m.name)
        while True:
            if parent:
                parent_list.appendleft(parent.name)
                parent = parent.parent
            else:
                m.path = "/".join(parent_list)
                break
        if commit:
            m.save()
        return m
