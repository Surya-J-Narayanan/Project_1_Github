from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class img_details(models.Model):
    
    img = models.ImageField(upload_to ='pics')
    name =  models.CharField(max_length = 100)
    size = models.CharField(max_length = 20)
    bestwork = models.BooleanField(default=False)
