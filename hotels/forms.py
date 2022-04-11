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

    def get_info(self):
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('phone')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )