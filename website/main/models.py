from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=250)
    task = models.TextField('Description')
    number = models.CharField('№', max_length=9)
    FCS = models.TextField('FCs')


def __str__(self):
    return self.title
