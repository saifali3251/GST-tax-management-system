from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.utils.translation import ugettext_lazy as _



class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name','last_name','username','password1','password2')
        # fields = '__all__'
        model = get_user_model()

    labels = {
                "first_name": _("First Name    "),
                "last_name": _("Last Name    "),
                "username": _("UserName"),
                "password1": _("Password"),
                "password2": _("Confirm Password"),
                # "address": _("Street Address"),
                }

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     # self.fields['username'].label = 'Display Name'
        # self.fields['username'].placeholder = 'Display Name'
        # self.fields['email'].label = 'Email Address'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['middleName']

    labels = {
                "middleName": _("Middle Name    "),
                "role": _("Enter Role"),
                # "address": _("Street Address"),
                }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']

    labels = {
                "middleName": _("Middle Name    "),
                "role": _("Enter Role"),
                # "address": _("Street Address"),
                }
