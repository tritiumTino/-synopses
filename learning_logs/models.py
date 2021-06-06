from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """the topic the user is studying"""
    text = models.CharField(max_length=200, verbose_name='Тема')
    date_added = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['-date_added']

    def __str__(self):
        return self.text


class Entry(models.Model):
    """the information learned by the user on the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(default='', verbose_name='Содержание')
    date_added = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['-date_added']

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
