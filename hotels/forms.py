from django import forms
from django.forms import ModelForm

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class ReviewForm(forms.Form):
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    comment = forms.CharField(required=True, widget=forms.Textarea)
