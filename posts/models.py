from django.db import models
from datetime import datetime

# Create your models here.

class Posts (models.Model):
    heading = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)