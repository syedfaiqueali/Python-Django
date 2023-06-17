"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def create_user_with_email_successful(self):
        """ Test creating a user with an email is successful """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().object.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)