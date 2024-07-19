from django.db import models
from django.contrib import admin
#from .models import Video

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='uploads/videos/')

    def __str__(self):
        return self.title

# admin.py





    
