from django.test import TestCase, RequestFactory, Client
from django.shortcuts import reverse
from django.contrib.auth.models import AnonymousUser, User

from memes.models import Meme
from memes import views

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='karton', email='karton@box.pl', password='top_secret')

    def tearDown(self):
        self.client = None
        self.factory = None
        self.user = None

    def test_index_not_loged(self):
        request = self.factory.get('/')

        request.user = AnonymousUser()

        response = views.loging(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('../templates/memes/skeleton.html')

    def test_index_loged(self):
        request = self.factory.get('/')

        request.user = self.user

        response = views.loging(request)

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('../templates/memes/skeleton.html')

    def test_index_url_accessible_by_name(self):
        response = self.client.get(reverse('imgs:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_url_accessible_by_name_loged(self):
        request = self.client.get(reverse('imgs:index'))
        request.user = self.user
        response = views.index(request)
        self.assertEqual(response.status_code, 200)