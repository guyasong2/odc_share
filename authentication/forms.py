from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Confirm Password'})

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'Password'})

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full p-2 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-500",
            "placeholder": "Enter your email"
        })
    )
