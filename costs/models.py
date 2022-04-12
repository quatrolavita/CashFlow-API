from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Expense(models.Model):
    """ Class Expense. Contain information about user costs"""

    class Status(models.TextChoices):
        DONE = 'DN',
        IN_PROGRESS = 'IP',

    description = models.TextField(default='Description')
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.IN_PROGRESS)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.description}, in {self.pub_date}'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
