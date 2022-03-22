from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=200)
    user_type = models.PositiveSmallIntegerField(choices='supporter', 'project_user')
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.username