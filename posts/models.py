from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Category(models.TextChoices):
        TN = 'TN', 'Танки'
        HI = 'HI', 'Хилы'
        DD = 'DD', 'ДД'
        TR = 'TR', 'Торговцы'
        GM = 'GM', 'Гилдмастеры'
        QG = 'QG', 'Квестгиверы'
        AS = 'AS', 'Кузнецы'
        SK = 'SK', 'Кожевники'
        PM = 'PM', 'Зельевары'
        SM = 'SM', 'Мастера заклинаний'
        SL = 'SL', 'Выбрать'

    title = models.CharField(max_length=128, verbose_name='Название')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    post_time = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.CharField(max_length=2,
                                choices=Category.choices,
                                default=Category.SL,
                                verbose_name='Категория')

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.CharField(max_length=256, verbose_name='Отклик')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    accept = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


