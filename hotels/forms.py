from django import forms
from django.forms import ModelForm

from .models import Room

from django.conf import settings
from django.core.mail import send_mail


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class ReviewForm(forms.Form):
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=70)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone = self.cleaned_data["phone"]
        message = self.cleaned_data["message"]

        send_mail(
            subject=f"Message from {name} (email: {email}, tel: {phone})",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
        )
