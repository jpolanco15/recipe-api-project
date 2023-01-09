from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe
from recipe.serializers import RecipeSerializer


def create_recipe(user, **kwargs):
    defaults = {
        'title': 'Sample Recipe',
        'description': 'This is a description of the recipe',
        'price': 12.45,
        'time_minutes': Decimal('5.73'),
        'link': 'http//example.com', 
    }
    defaults.update(kwargs)
    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    #def test