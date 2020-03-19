from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

REGISTER_USER = reverse('users:register')
LOGIN_USER = reverse('users:login')

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
    
    def test_create_valid_user_without_tag_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test1@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "password": "admin1234"
        }
        res = self.client.post(REGISTER_USER, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_login_user(self):
        """Test User Login"""
        payload = {
            "email": "test1@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "password": "admin1234"
        }
        login_payload = {
            "email": "test1@gmail.com",
            "password": "admin1234"
        }

        register = self.client.post(REGISTER_USER, payload)
        self.assertEqual(register.status_code, status.HTTP_201_CREATED)

        login = self.client.post(LOGIN_USER, **login_payload)
        self.assertEqual(register.status_code, status.HTTP_201_CREATED)

        