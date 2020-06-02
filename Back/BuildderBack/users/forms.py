from django import forms
from .models import B_User

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        model = B_User
        fields=[
            "photo",
            "first_name",
            "last_name",
            "email",
            # "facebook_link",
            # "twitter_link",
            # "linkedin_link",
            # "P_Creator",
            # "P_Collaborator",
            # "P_Investor",
        ]

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=250)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        model = B_User
        fields=[
            "email",
            "password",
        ]
    