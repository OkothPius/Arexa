import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import admin

class Rental(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    house_detail = models.TextField(default='Full Furnished')
    pub_date = models.DateTimeField('date published')
    estate = models.CharField(max_length=100)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Handles redirect
    def get_absolute_url(self):
        return reverse('post-detail' ,kwargs={'pk': self.pk})

class Images(models.Model):
    head = models.CharField(max_length=100, unique=True, null=True)
    post = models.ForeignKey(Rental, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rental_posts')

    def __str__(self):
        return str(self.head)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural='Images'


class Category(models.Model):
    home = models.ManyToManyField(Rental)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural='Categories'

class Location(models.Model):
    home = models.ForeignKey(
        Rental,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return str(self.home)
