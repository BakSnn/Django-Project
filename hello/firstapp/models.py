from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=20)
    age = models.DateField()
    maker = models.TextField(max_length=20, default='')
    price = models.FloatField(max_length=10, default='')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    category = models.CharField(max_length=20)
    objects = models.Manager()

