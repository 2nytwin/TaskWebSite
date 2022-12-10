from django.db import models


class Task(models.Model):
    title = models.CharField('FCS', max_length=250)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'