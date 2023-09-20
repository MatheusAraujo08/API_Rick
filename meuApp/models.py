from django.db import models
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100) #varchar
    type = models.CharField(max_length=150, null=False)
    dimension = models.DecimalField(max_digits=10, decimal_places=2)
    residents = models.BigIntegerField() #bigint
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name 
    
class Character(models.Model):
    name = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=150, null=False)
    species = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=150, null=False)
    gender = models.CharField(max_length=150, null=False)
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name 


class Episode(models.Model):
    name = models.CharField(max_length=150, null=False)
    air_date = models.DateTimeField(default=timezone.now())
    episode = models.CharField(max_length=150, null=False)
    created = models.DateTimeField(default=timezone.now())
    character = models.ForeignKey(Character, related_name="personage", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    