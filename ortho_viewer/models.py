from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from datetime import date
import os

class Orthoimage(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    inspection_date = models.DateField(null = True, default='')
    address = models.CharField(max_length=100, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class panel_fault(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_id = models.ForeignKey(Orthoimage, on_delete=models.CASCADE)
    px_x = models.FloatField(default = 1, null=True)
    px_y = models.FloatField(default = 1, null=True)
    fault_image = models.ImageField(upload_to='image/', null=True, blank=True)
    fault_type = models.CharField(max_length=200, default="Bypass Fault")
    fault_x = models.FloatField(default = 0.0)
    fault_y = models.FloatField(default = 0.0)
    fault_width = models.FloatField(default = 0.0)
    fault_height = models.FloatField(default = 0.0)

    def publish(self):
        self.save()

    def __int__(self):
        return self.image_id

    def filename(self):
        return os.path.basename(self.file.name)

   


# Create your models here.
