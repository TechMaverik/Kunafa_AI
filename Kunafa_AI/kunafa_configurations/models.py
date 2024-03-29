from __future__ import unicode_literals 
from django.db import models 

# Create your models here.
MODES = (
    ('Disabled','Disabled'),
    ('Face_Tracking','Face Tracking'),
    ('Full_Body_Detection', 'Full Body Detection'),  
    ('Upper_Half_Body_Detection', 'Upper Half Body Detection'),  
    ('Lower_Half_Body_Detection', 'Lower Half Body Detection'),  
)
VOICE =(
    ('Enabled','Enabled'),
    ('Disabled','Disabled'),
)
class IPCamera(models.Model):
    IPV4 = models.CharField(max_length=30, default="0") 
    PORT = models.CharField(max_length=30, default="") 
    MODEL = models.CharField(max_length=30, choices=MODES, default='Disabled')
    SOUND = models.CharField(max_length=30, choices=VOICE, default='Disabled')

    class Meta:  
        db_table = "kunafa_vision_configurations"
