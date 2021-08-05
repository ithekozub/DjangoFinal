from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mailing(models.Model):
    subject = models.CharField(max_length=128, verbose_name='Тема рассылки')
    body = models.TextField(blank=True, null=True, verbose_name='Тело рассылки')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    finished = models.BooleanField(default=False)