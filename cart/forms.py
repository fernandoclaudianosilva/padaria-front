from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=80, label='First name')
    last_name = forms.CharField(max_length=80, label='Last name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=30, label='Phone')
    address = forms.CharField(max_length=200, label='Address')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=2, label='State', initial='MA')
    zip_code = forms.CharField(max_length=10, label='ZIP code')
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Order notes')
