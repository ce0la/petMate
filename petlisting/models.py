from django.db import models
from django.utils.timezone import now

# Create your models here.

class Petlisting(models.Model):
    pet_image = models.ImageField(blank=True, null=True)
    pet = models.TextField(max_length=30)
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    gender = models.TextField(max_length=30)
    about = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    interested_pets = models.CharField(max_length=9999, null=True, blank=True)
    date_listed = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
