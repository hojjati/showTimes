from rest_framework import viewsets

from . import models
from . import serializers


# viewset MovieItem API
class MovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
