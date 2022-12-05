from django.test import TestCase
from django.urls import reverse
import json
from rest_framework.test import APITestCase

class Tests(APITestCase):
    def test_get_correct(self):
        url = reverse('get', args=["rabota", "rabota", "rabota1"])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), [{
            "id": 38,
            "Title":"rabota",
            "ConfDate":"rabota",
            "ConfTag":"rabota1"
        }])