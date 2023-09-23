from django.db import models

# Create your models here.

class Profile(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)