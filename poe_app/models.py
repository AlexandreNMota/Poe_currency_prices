from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100)
    chaosEquivalent = models.FloatField()
    
    class Meta:
       app_label = 'poe_app'
