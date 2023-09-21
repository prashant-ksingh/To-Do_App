from django.db import models
import datetime

class User(models.Model):
    # id = models.CharField(max_length=25,unique=True, primary = True)
    userid = models.CharField(max_length=50,unique=True)
    name =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.userid}-{self.name}"

class Todo(models.Model):
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE, null= True, blank= True
    )
    # id = models.CharField(max_length=25,unique=True)
    taskname = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=200, null=True)
    added_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    deadline = models.DateTimeField(null=False, default=datetime.datetime.now())
    prior = models.BooleanField(default=False)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.userid}-{self.taskname}"
    
