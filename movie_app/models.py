from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    director = models.ForeignKey(Director, related_name='movies', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    @property
    def reviews_list(self):
        return [i.text for i in self.reviews.all()]

    @property
    def rating(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg']


class Review(models.Model):
    STAR_CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    stars = models.IntegerField(default=1, choices=STAR_CHOICES)
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
