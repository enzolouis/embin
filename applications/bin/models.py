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