from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    pictures = models.ImageField(upload_to="movie", blank=True, null=True)
    rating = models.SmallIntegerField(null=True, blank=True)
    notes = models.TextField(max_length=200, null=True, blank=True)