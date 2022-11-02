from django.db import models

# Create your models here.
class Task(models.Model):
    heading=models.CharField(max_length=100)
    detail=models.CharField(max_length=500)
    date=models.DateField()
    is_deleted=models.CharField(max_length=2)
