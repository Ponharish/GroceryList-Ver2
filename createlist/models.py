from django.db import models

# Create your models here.

class GroceriesTable(models.Model):
    list = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year = models.IntegerField() 
    grocerylist = models.JSONField(default=dict)
    notes = models.TextField(blank=True, null=True)