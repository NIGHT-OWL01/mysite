from django.db import models

# Create your models here.

class QrCode(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField()