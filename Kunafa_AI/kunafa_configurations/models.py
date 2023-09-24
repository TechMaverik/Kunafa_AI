from __future__ import unicode_literals 
from django.db import models 

# Create your models here.
class RemiderModel(models.Model):
    reminders = models.CharField(max_length=20, default="")  
    time = models.CharField(max_length=20, default="")  
    class Meta:  
        db_table = "reminders" 