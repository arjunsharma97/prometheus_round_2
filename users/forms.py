from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser as CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):
    pass