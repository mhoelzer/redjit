from django import forms
from models import RedjitUser


class SignupForm(forms.Form):

    # https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RedjitUser


class LoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()