from __future__ import unicode_literals
from django.db import models


class ShowTime(models.Model):
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='Mon', blank=True)
    time = models.TimeField(blank=True)

    def __str__(self):
        return u"%s" % self.day


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return u"%s" % self.name


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=2500, blank=True)
    categories = models.ManyToManyField(Category, related_name="categories")
    showTimes = models.ManyToManyField(ShowTime, related_name="showTimes")

    def __str__(self):
        return u"%s" % self.name
