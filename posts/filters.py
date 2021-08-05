from django_filters import FilterSet
from .models import Post, Comment


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('title', 'author', 'category')


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'post__title': ['icontains'],
        }
