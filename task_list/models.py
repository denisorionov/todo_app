from django.db import models
from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class Task(models.Model):
    STATUS_CHOICES = [
        ('done', 'done'),
        ('in progress', 'in progress')
]
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    due_date = models.DateField('Срок выполнения', blank=True, null=True)
    status = models.CharField('Статус задачи', max_length=11, default='in progress', choices=STATUS_CHOICES, db_index=True)
    tags = TaggableManager(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title
