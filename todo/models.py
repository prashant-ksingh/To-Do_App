from django.db import models

class User(models.Model):
    id = models.CharField(max_length=25,unique=True)
    name =models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userid = models.CharField(max_length=50,unique=True)
    password = models.CharField()

class Todo(models.Model):
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE, null= True, blank= True
    )
    id = models.CharField(max_length=25,unique=True)
    taskname = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    added_date = models.DateTimeField()
    deadline = models.DateTimeField()
    prior = models.BooleanField()
    iscompleated = models.BooleanField()

    def __str__(self):
        return self.taskname
    
