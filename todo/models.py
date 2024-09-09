from django.db import models
import datetime
from django.contrib.auth.models import User

class Todo(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank=True)
    taskname = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    added_date = models.DateTimeField(null=False, default=datetime.datetime.now())

    def __str__(self):
        return f"{self.taskname}"
    
