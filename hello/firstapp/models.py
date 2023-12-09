from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=20)
    age = models.TextField()
    maker = models.TextField(max_length=20, default='')
    price = models.IntegerField(max_length=10, default='')
    category = models.CharField(max_length=20)
    objects = models.Manager()

