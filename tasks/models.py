from django.db import models
from uuid import uuid4
from accounts.models import User
import time

# Create your models here.
class Task(models.Model):

    priority_choices = [
        ('low',"Low"),
        ('medium','Medium'),
        ('high','High')
    ]

    status_choices = [
        ("open","Open"),
        ("in_progress","In_Progress"),
        ("closed","Closed")
    ]
    
    id = models.UUIDField(unique=True,primary_key=True,default=uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    due_date = models.DateField()
    priority = models.CharField(choices=priority_choices,max_length=10,default="medium")
    status = models.CharField(max_length=15,choices=status_choices,default="open")
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    assignee = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self) -> str:
        return self.title
    




