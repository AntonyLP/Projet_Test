from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    IMPORTANCE_TAGS = [
        ('high', 'Haute'),
        ('medium', 'Moyenne'),
        ('low', 'Faible')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    importance = models.CharField(max_length=20, choices=IMPORTANCE_TAGS, default='medium')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
