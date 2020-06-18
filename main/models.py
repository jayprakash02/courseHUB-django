from django.db import models

# Create your models here.
class Features(models.Model):
    recent = models.CharField(max_length=50)
    bgimage = models.ImageField(upload_to='uploads',default='#')
    desc = models.CharField(max_length = 100)
    pub_date = models.DateField( auto_now=False, auto_now_add=False)