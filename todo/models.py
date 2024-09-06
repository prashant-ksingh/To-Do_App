from django.db import models
import datetime

class User(models.Model):
    name =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.userid}-{self.name}"

class Todo(models.Model):

    taskname = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    added_date = models.DateTimeField(null=False, default=datetime.datetime.now())

    def __str__(self):
        return f"{self.taskname}"
    
