from django import forms
from .models import Users

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['type']
        fields = ['name', 'email', 'password']  # Include only the necessary fields
        widgets = {
            'password': forms.PasswordInput(),  # Use a password input widget for the password field
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['type']  # Exclude the 'type' field
        fields = ['email', 'password']  # Include only the necessary fields
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),  # Use a password input widget for the password field
        }
