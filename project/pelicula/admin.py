from django.contrib import admin

from  .models import Author, Genre, Peliculas

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Peliculas)