from django.db import models


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


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie
