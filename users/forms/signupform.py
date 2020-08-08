from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Group
from users.forms.horizontalformhelper import HorizontalFormHelper


class SignUpForm(UserCreationForm):
    username = UsernameField(
        label=False,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'username'},
        ),
    )
    email = forms.EmailField(
        max_length=254, label=False,
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                       'placeholder': 'e-mail'}),
    )
    password1 = forms.CharField(
        label=False,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                          'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        strip=False, label=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                                          'placeholder': 'confirm password'}),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Hasła nie są identyczne', code='password_mismatch')

        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit)

        try:
            group = Group.objects.get(name="Customer")
            group.user_set.add(user)
            group.save()
        except Group.DoesNotExist:
            pass

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("register")
