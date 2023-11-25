from datetime import timedelta, datetime

import pytz
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from config import settings
from users.models import CustomUser


class UsersTestCase(APITestCase):
    def test_create_user_successful(self):
        """
        Tests successful creation of a CustomUser instance.
        """
        data = {
            'username': 'test_username',
            'email': 'test_email@mail.com',
            'password': 'QWE123qwe123!'
        }
        response = self.client.post(reverse('users:register_user'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['username'], data['username'])
        self.assertEqual(response.json()['email'], data['email'])

        user = CustomUser.objects.get(username=data['username'])
        delta = timedelta(minutes=2)
        tz = pytz.timezone(settings.TIME_ZONE)
        now = datetime.now(tz=tz)
        self.assertTrue(now - delta < user.registration_date < now + delta)

    def test_create_user_invalid_email(self):
        """
        Tests creation of a CustomUser instance with invalid email.
        """
        data = {
            'username': 'test_username',
            'email': 'test_emailmail.com',
            'password': 'QWE123qwe123!'
        }
        response = self.client.post(reverse('users:register_user'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'], ['Enter a valid email address.'])

    def test_create_user_missing_fields(self):
        """
        Tests creation of a CustomUser instance with missing fields.
        """
        data = {}
        response = self.client.post(reverse('users:register_user'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['username'], ['This field is required.'])
        self.assertEqual(response.json()['email'], ['This field is required.'])
        self.assertEqual(response.json()['password'], ['This field is required.'])
