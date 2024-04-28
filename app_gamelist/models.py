from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    initial_release = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    image_relative_url = models.CharField(max_length=50,null=True,blank=True)
    genre = models.CharField(max_length=60,blank=True)