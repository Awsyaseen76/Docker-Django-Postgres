from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignUpForm(UserCreationForm):
    dob = forms.CharField(max_length=100, help_text='Required, Please select your date of birth')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('dob')