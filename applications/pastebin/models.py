from django.db import models

# Create your models here.

class Bin(models.Model):
	code = models.CharField(max_length=10)
	content = models.TextField() # max_length=...
