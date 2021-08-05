from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('category', 'title', 'content')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

    widgets = {
        'comment': forms.TextInput(attrs={'class': 'form-control'}),
    }


