from django.db import models

# Create your models here.
class ZipCode(models.Model):
    zip_code = models.CharField(max_length=10)
    location_key = models.CharField(max_length=20)

    def __str__(self):
        return self.zip_code