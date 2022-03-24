from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    providing = models.ManyToManyField("projects.Service", related_name="providers", null=True, blank=True)

    def __str__(self):
        return self.usernamex