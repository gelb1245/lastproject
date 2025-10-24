# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст публікації")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")
    author = models.CharField(max_length=100, verbose_name="Автор", default="Адміністратор")

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
