from crispy_forms.layout import Button
from users.forms.horizontalformhelper import HorizontalFormHelper
from django import forms
from users.models import Posts


class PostConfirmDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostConfirmDeleteForm, self).__init__(*args, **kwargs)
        self.helper = HorizontalFormHelper()

        self.helper.add_submit("Delete")
        self.helper.add_cancel("Cancel")

