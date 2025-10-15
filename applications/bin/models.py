"""from django.db import models

# Create your models here.

class Bin(models.Model):
	code = models.CharField(max_length=10)
	#title = models.TextField(max_length=50)
	content = models.TextField() # max_length=...
"""

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Bin(models.Model):
    code = models.CharField(max_length=10)#, unique=True)
    content = models.TextField()
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.code

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'bin')

    def __str__(self):
        return f"{self.user.username} - {self.bin.code}"

class Pattern(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    height = models.FloatField(null=True, blank=True)
    headheight = models.FloatField(null=True, blank=True)
    backwaistlength = models.FloatField(null=True, blank=True)
    frontwaistlength = models.FloatField(null=True, blank=True)
    hipdepth = models.FloatField(null=True, blank=True)
    jacketlength = models.FloatField(null=True, blank=True)
    dresslength = models.FloatField(null=True, blank=True)
    skirtlength = models.FloatField(null=True, blank=True)
    cratchlength = models.FloatField(null=True, blank=True)
    kneelength = models.FloatField(null=True, blank=True)
    trouserslength = models.FloatField(null=True, blank=True)
    elbowlength = models.FloatField(null=True, blank=True)
    sleevelength = models.FloatField(null=True, blank=True)
    chestCirc = models.FloatField(null=True, blank=True)
    bustcirc = models.FloatField(null=True, blank=True)
    waistcirc = models.FloatField(null=True, blank=True)
    hip = models.FloatField(null=True, blank=True) # hipCirc
    neckcircumference = models.FloatField(null=True, blank=True)
    wristcircumference = models.FloatField(null=True, blank=True)
    backwidth = models.FloatField(null=True, blank=True)
    # <=> shoulderwidth
    backshoulderwidth = models.FloatField(null=True, blank=True)
    bustheight = models.FloatField(null=True, blank=True)
    bustdifference = models.FloatField(null=True, blank=True)
    breastdistance = models.FloatField(null=True, blank=True)
    bottomtrouserswidth = models.FloatField(null=True, blank=True)
    waistbanwidth = models.FloatField(null=True, blank=True)
    
    easeallowance = models.FloatField(null=True, blank=True)
    trouserseaseallowance = models.FloatField(null=True, blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name