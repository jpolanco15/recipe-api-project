from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.test import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create(**params)

class PublicUserApiTest(TestCase):
    pass