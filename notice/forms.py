from django import forms
from . import models


class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = ("title", "contents", "image", "file")
