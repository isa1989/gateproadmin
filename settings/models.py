from django.db import models
from solo.models import SingletonModel

# Create your models here.

class Settings(SingletonModel):
    banner_image = models.ImageField(upload_to='banner-img')
        
        
        