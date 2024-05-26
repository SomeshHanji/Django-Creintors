from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomPasswordInput(forms.PasswordInput):
    def __init__(self, placeholder=None, attrs=None, render_value=False):
        super().__init__(attrs, render_value=render_value)
        self.placeholder = placeholder

    def render(self, name, value, attrs=None, renderer=None):
        if self.placeholder is not None:
            attrs = attrs or {}
            attrs['placeholder'] = self.placeholder
        return super().render(name, value, attrs, renderer)

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=CustomPasswordInput(placeholder="Enter your password", render_value=True)
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=CustomPasswordInput(placeholder="Confirm your password", render_value=True)
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
        }
