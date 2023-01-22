from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del autor")

    def __str__(self):
        return self.name

class Peliculas(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=100, help_text="pon aqui de que trata la pelicula")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reversed('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)