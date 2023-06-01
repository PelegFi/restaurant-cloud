from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(required=False)#<----
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:                              
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'is_staff', 'first_name', 'last_name')


class EditUserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30, min_length=3, required=True)
    last_name = forms.CharField(label="last Name", max_length=30, min_length=3, required=True)
    username = forms.CharField(label="username", max_length=30, min_length=5, required=True)
    password = forms.CharField(label='New Password', widget=forms.PasswordInput(),min_length=5, required=True)
    email = forms.CharField(label="email", required=True)
    is_staff = forms.BooleanField(label="is_staff", required=False)

