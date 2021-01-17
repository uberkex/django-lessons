from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=15)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
