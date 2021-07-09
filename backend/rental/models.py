from django.db import models
from django.utils import timezone

class Rental(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField()
    pub_date = models.DateField()
    estate = models.CharField(max_length=100)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

class Category(models.Model):
    home = models.ManyToManyField(Rental)

class Location(models.Model):
    home = models.ForeignKey(
        Rental,
        on_delete = models.CASCADE,
    )
