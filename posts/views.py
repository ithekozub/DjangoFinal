from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.cache import cache


from .models import Post, Comment
from .forms import PostForm, CommentForm
from .filters import CommentFilter


def CategoryView(request, cats):
    category_ads = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'category_ads': category_ads, 'cats': cats})


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.select_related('author').order_by('-id')
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_queryset(self):
        return Post.objects.select_related('author').filter(pk=self.kwargs['pk'])


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()

        return redirect('post_detail', p.id)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    context_object_name = 'post'
    form_class = PostForm

    def get_queryset(self):
        return Post.objects.select_related('author').filter(pk=self.kwargs['pk'])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def get_queryset(self):
        return Post.objects.select_related('author').filter(pk=self.kwargs['pk'])


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_create.html'
    context_object_name = 'comment'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

        return redirect('post_detail', post.id)


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'comments_list.html'
    context_object_name = 'comments'


    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = CommentFilter(self.request.GET,
                                          queryset=Comment.objects.select_related('user', 'post', 'post__author').filter(post__author=self.request.user))
          # вписываем наш фильтр в контекст
        return context


@login_required()
def CommentAcceptView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if not comment.accept and request.user == comment.post.author:
        comment.accept = True
        comment.save()
    return HttpResponseRedirect(reverse('comments'))


@login_required()
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user == comment.post.author:
        comment.delete()
    return HttpResponseRedirect(reverse('comments'))