from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShowTime
        fields = ('id', 'day', 'time')


class MovieSerializer(serializers.ModelSerializer):
    showTimes = ShowTimeSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Movie
        fields = ('id', 'name', 'description', 'showTimes', 'categories')
