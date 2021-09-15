from django import forms
from . import models


class MarketPostForm(forms.ModelForm):
    class Meta:
        model = models.CommunityPost
        fields = ("title", "contents", "image", "file", "market_tag")


class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = models.CommunityPost
        fields = ("title", "contents", "image", "file")
