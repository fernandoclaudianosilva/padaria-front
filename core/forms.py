from django import forms
from .models import CakeTastingRequest, ContactMessage, NewsletterSubscriber


class CakeTastingRequestForm(forms.ModelForm):
    class Meta:
        model = CakeTastingRequest
        fields = ['name', 'email', 'phone', 'preferred_date', 'guests', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '(508) 000-0000'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'placeholder': 'Number of guests', 'min': 1}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about your event...'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'preferred_date': 'Preferred date',
            'guests': 'Number of guests',
            'message': 'Message',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Message'}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
        }
