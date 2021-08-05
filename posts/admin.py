from django.contrib import admin
from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'category')
    list_filter = ('post_time', 'author', 'category')
    form = PostAdminForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'comment', 'comment_time', 'accept')
    list_filter = ('user', 'comment_time', 'accept')
