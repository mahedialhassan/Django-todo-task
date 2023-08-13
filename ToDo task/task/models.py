from django.db import models

class TaskModel(models.Model):
   
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)