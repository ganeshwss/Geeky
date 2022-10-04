from django.db import models

# Create your models here.
class Transformer(models.Model):
    alive=models.BooleanField()
    alternate_mode=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    name=models.CharField(max_length=100)