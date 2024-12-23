from django.db import models
from category.models import TaskCategory
import datetime

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=datetime.date.today())
    category = models.ManyToManyField(TaskCategory)
    def __str__(self):
        return self.taskTitle
