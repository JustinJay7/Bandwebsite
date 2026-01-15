from django.db import models
from django.contrib.auth.models import User

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
#   image = models.ImageField(upload_to='band/images/', blank=True)
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
#   cover_image = models.ImageField(upload_to='band/covers/', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.DurationField()

    def __str__(self):
        return self.title
