from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(default='', verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Отредактировано')
    media = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Файл', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
