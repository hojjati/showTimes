# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from showTimesApp.models import ShowTime, Movie, Category


# Giving adming page access to ShowTime Model
@admin.register(ShowTime)
class MoviesAdmin(admin.ModelAdmin):
    model = ShowTime
    list_display = ("id", "day", "time")


# Giving adming page access to Category Model
@admin.register(Category)
class MoviesAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("id", "name")


# Giving adming page access to Movie Model
@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ("id", "name", "description")
