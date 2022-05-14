from django.contrib.auth import get_user_model
from django.db import models
from django.forms import CharField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    location = models.CharField(max_length=200)
    urgent = models.BooleanField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    # pledge_date = models.DateTimeField() 
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # 
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

class Service(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
