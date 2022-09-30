from django import forms
from django.forms import CharField, Textarea
from .models import Dweet
from django.contrib.auth.models import User
class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "placeholder": "Dweet something...",
            "class": "textarea is-success is-medium",
        }),
        label=""
        )
    class Meta:
        model = Dweet
        exclude = ("user",)
class LoginForm(forms.ModelForm):
    name = forms.CharField(max_length=244)
    password = forms.PasswordInput()
    class Meta:
        model = User
        exclude =("user",)