from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

REGISTER_USER = reverse('users:register')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_with_tag_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test1@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "password": "admin1234",
            "tag": [{"tag":"tag 1"}, {"tag":"tag 2"}]
        }
        res = self.client.post(REGISTER_USER, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
    
    def test_create_valid_user_with_empty_tag_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test1@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "password": "admin1234",
            "tag": []
        }
        res = self.client.post(REGISTER_USER, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
