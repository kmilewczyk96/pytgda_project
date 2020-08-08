from django import forms

from users.forms.horizontalformhelper import HorizontalFormHelper
from users.models import Posts


class CreatePostForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'Share something...'}
        )
    )

    class Meta:
        model = Posts
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(CreatePostForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("Add")
        self.helper.add_cancel("Cancel")
