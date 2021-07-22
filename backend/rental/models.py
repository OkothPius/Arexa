from django.db import models
from django.utils import timezone
from django.urls import reverse

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

class Location(models.Model):
    home = models.ForeignKey(
        Rental,
        on_delete = models.CASCADE,
    )
