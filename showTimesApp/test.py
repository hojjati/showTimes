# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from showTimesApp.models import *
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ERPTestCases(APITestCase):
    listUrl = reverse('movie-list')

    def setUp(self):
        self.mondayShowTime = ShowTime.objects.create(id="1", day="Mon", time="18:00:00")
        self.actionCategory = Category.objects.create(id="1", name="Action")
        self.thorMovie = Movie.objects.create(id="1", name="Thor", description="A good movie")
        self.thorMovie.showTimes.add(self.mondayShowTime)
        self.thorMovie.categories.add(self.actionCategory)

    # This test ensures that retrieved data for a movie through the API matches with the database record
    def testMovieDetailRetrieve(self):
        response = self.client.get(reverse("movie-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "name": "Thor",
                          "description": "A good movie",
                          "showTimes": [{"id": 1, "day": "Mon", "time": "18:00:00"}],
                          "categories": [{"id": 1, "name": "Action"}]
                          })
