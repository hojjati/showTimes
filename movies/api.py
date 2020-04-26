from rest_framework import routers
from showTimesApp import api_views as myappViews
from django.urls import path, include

router = routers.DefaultRouter()

# routers for using api
router.register(r'movies', myappViews.MovieViewset)

urlpatterns = [
    path('', include(router.urls))
]
