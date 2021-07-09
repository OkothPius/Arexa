from django.db import models
from django.utils import timezone

class Home(models.Model):
    """
    A model to display home attributes.
    """
    title = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    pub_date = models.DateField()
    estate = models.CharField(max_length=100)

class Category(models.Model):
    """
    Model for category.
    """
    home = models.ManyToManyField(Home)

class Location(models.Model):
    home = models.ForeignKey(
        Home,
        on_delete = models.CASCADE,
    )
