from django import forms
from . import models


class MajorPostForm(forms.ModelForm):
    class Meta:
        model = models.MajorPost
        fields = ("title", "contents", "image", "file")
