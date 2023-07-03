from django.db import models

# Create your models here.

class Newapp(models.Model):
    title = models.CharField(max_length=30)
    intro = models.CharField(max_length=100)
    head = models.FloatField()


    def __str__(self):
        return self.title
