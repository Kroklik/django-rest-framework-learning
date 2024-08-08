from django.db import models


# Create your models here.

class Actor(models.Model):
    title = models.CharField(verbose_name='Имя актера', max_length=120)
    content = models.CharField(verbose_name='Описание актера', max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=120, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
