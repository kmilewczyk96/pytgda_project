from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from users.forms.horizontalformhelper import HorizontalFormHelper
from django.contrib.auth.models import User


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                          'placeholder': 'old password'}),
    )

    new_password1 = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                          'placeholder': 'new password'}),
    )

    new_password2 = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                          'placeholder': 'confirm your new password'}),
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(PasswordForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("confirm")
        self.helper.add_cancel('cancel')
