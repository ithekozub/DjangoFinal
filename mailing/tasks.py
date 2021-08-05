from celery import shared_task
from django.contrib.auth.models import Group

from .models import Mailing
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def send_mailing(pid):
    mailing = Mailing.objects.get(pk=pid)
    subject = mailing.subject
    group = Group.objects.get(name="basic")
    recipients = group.user_set.all()
    for user in recipients:
        email = user.email
        html_content = render_to_string(
            'mailing_email.html',
            {

                'body': mailing.body,
                'link': 'http://127.0.0.1:8000'
            })
        msg = EmailMultiAlternatives(
            subject=subject,
            from_email='ithekozub@i.ua',
            to=[email],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()
    mailing.finished = True
    mailing.save()


