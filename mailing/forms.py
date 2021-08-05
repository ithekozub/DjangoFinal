from django import forms
from .models import Mailing
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MailingForm(forms.ModelForm):
    body = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Mailing
        fields = ('subject', 'body')

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),

        }
