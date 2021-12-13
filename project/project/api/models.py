from django.db import models

# Create your models here.
class ZipCodes(models.Model):
    zip_code = models.CharField(max_length=10)
    location_key = models.CharField(max_length=20)