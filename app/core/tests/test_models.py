from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core import models


class ModelTests(TestCase):

    def test_create_user_email_success(self):
        """Test to validate user create is succesfully just with email and
        password"""
        email = "test@testemail.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(
            email=email, password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        """Validate emails normalization"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:

            user = get_user_model().objects.create_user(email, 'sample124')
            self.assertEqual(user.email, expected)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "sample123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testPass123'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title="example recipe",
            time_minutes=5,
            price=Decimal('5.50'),
            description="This is a test recipe",
        )

        self.assertEqual(str(recipe), recipe.title)
