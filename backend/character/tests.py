from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.views import status
from .sentimentAnalyzer import sentiment_analyzer
from . import views


class UserDataTestCase(TestCase):
    def setUp(self):
        self.user_data = []

    def test_get_matched_villain(self):
        snowball = {'name': 'Snowball', 'words': []}
        jigsaw = {'name': 'Jigsaw', 'words': []}
        villains = [snowball, jigsaw]
        matched = sentiment_analyzer.get_matched_villain_test(
            self.user_data, villains)
        # Snowball : 0.91
        # Jigsaw : 0.89
        self.assertEqual(matched, 'Snowball')

    def test_get_mvti_type(self):
        mvti_type = sentiment_analyzer.get_mvti_type(self.user_data)
        self.assertEqual(mvti_type, 'PJTF')


class SentimentAnalyzeTestCase(APITestCase):
    def setUp(self):
        self.url = 'elice-kdt-ai-track-vm-da-05.koreacentral.cloudapp.azure.com/api/sentiment'

    def test_post_user_data(self):
        data = {
            "words": ["death", "fear", "kill", "pray", "god", "hope", "pretty"]
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

