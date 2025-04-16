from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    username = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    message_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField()

    class Meta:
        ordering = ('date_added', )

    def __str__(self):
        return f"{self.username}: {self.message_content}"


class Room(models.Model):
    name = models.CharField(max_length=50)
    # for url
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    taskContent = models.CharField(max_length=50)
    complete = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('date_added', )

    def __str__(self):
        return f"{self.name}: {self.taskContent}"
