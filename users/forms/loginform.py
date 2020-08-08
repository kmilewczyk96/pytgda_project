from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from users.forms.horizontalformhelper import HorizontalFormHelper


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'username'}
        )
    )

    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'password'}
        )
    )

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("login")
