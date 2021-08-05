from celery import shared_task
from .models import Comment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def mail_new_comment(pid):
    comment = Comment.objects.select_related('user', 'post').get(pk=pid)
    author_email = comment.post.author.email
    subject = 'Новый отклик на объявление'

    html_content = render_to_string(
        'new_comment.html',
        {
            'title': comment.post.title,
            'comment_author': comment.user.username,
            'username': comment.post.author.username,
            'post_link': f'http://127.0.0.1:8000/posts/{comment.post.id}',
            'comments_link': f'http://127.0.0.1:8000/posts/comments/'
        })
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email='ithekozub@i.ua',
        to=[author_email],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()


@shared_task
def mail_accepted_comment(pid):
    comment = Comment.objects.select_related('user', 'post').get(pk=pid)
    email = comment.user.email
    subject = 'Ваш отклик принят'
    html_content = render_to_string(
        'accepted_comment.html',
        {
            'title': comment.post.title,
            'post_author':  comment.post.author.username,
            'username': comment.user.username,
            'post_link': f'http://127.0.0.1:8000/posts/{comment.post.id}',
            'comments_link': f'http://127.0.0.1:8000/posts/comments/',
        })
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email='ithekozub@i.ua',
        to=[email],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()
