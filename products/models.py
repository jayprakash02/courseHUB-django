from django.db import models

# Create your models here.
choice = [
    ('1','webdev'),
    ('2','ml'),
    ('3','uiux'),
    ('4','business')
]
class Allproduct(models.Model):
    name = models.CharField(max_length=50)
    character = models.CharField( max_length=50,choices=choice,default='1')
    authur_name = models.CharField( max_length=50)
    desc = models.CharField( max_length=50)
    img_url = models.ImageField( upload_to='uploads', height_field=None, width_field=None, max_length=None,default='#')
