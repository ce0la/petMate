from django.db import models

# Create your models here.

class Petlisting(models.Model):
    image = models.ImageField(upload_to="images/")
    pet = models.TextField(max_length=30)
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    gender = models.TextField(max_length=7)
    about = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_listed = models.DateTimeField()
