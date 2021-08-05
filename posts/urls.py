from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    CommentCreateView, CommentListView, CommentAcceptView, CommentDeleteView

urlpatterns = [
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/add_comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/', CommentListView.as_view(), name='comments'),
    path('comments/accept/<int:pk>', CommentAcceptView, name='comment_accept'),
    path('comments/delete/<int:pk>', CommentDeleteView, name='comment_delete'),

]