from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE , related_name='chat_tasks')
    taskContent = models.CharField(max_length=50)
    complete = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added', )

    def __str__(self):
        return f"{self.name}: {self.taskContent}"