from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Posts (models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return "Post" + " " + str(self.id) + " " + "-" + " "+ self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" )
        return super().save(*args, **kwargs)