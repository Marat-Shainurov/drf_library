from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from library.models import Book
from users.models import CustomUser


class BookTestCase(APITestCase):
    """
    Testcases for the Book CRUD mechanism.
    """

    def setUp(self) -> None:
        user_data = {'username': 'test_username', 'email': 'test_email', 'password': 'QWE123qwe123!'}
        self.test_user = CustomUser.objects.create(**user_data)
        self.client.force_authenticate(user=self.test_user)

        book_data = {
            'title': 'Test book',
            'author': 'Me',
            'publish_year': '2023',
            'ISBN': '123456789112'
        }
        self.test_book = Book.objects.create(**book_data)

    def test_create_book_successfully(self):
        """
        Tests successful Book instance creation.
        """
        data = {
            'title': 'Test book',
            'author': 'Me',
            'publish_year': '2023',
            'ISBN': '123456789222'
        }
        response = self.client.post(reverse('library:create_book'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], data['title'])
        self.assertEqual(response.json()['author'], data['author'])
        self.assertEqual(response.json()['publish_year'], data['publish_year'])
        self.assertEqual(response.json()['ISBN'], data['ISBN'])

    def test_create_book_invalid_data(self):
        """
        Tests the Book instances creation with invalid_data
        (publish_year and ISBN fields values violate the validation patterns).
        """
        data = {
            'title': 'Test book',
            'author': 'Me',
            'publish_year': '202w',
            'ISBN': '123456789112w'
        }
        response = self.client.post(reverse('library:create_book'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['ISBN'],
                         ["Enter a valid ISBN. This value may contain only digits and '-' characters"])
        self.assertEqual(response.json()['publish_year'], ['Enter a valid 4-digit publish year.'])

    def test_create_book_missing_fields(self):
        """
        Tests Book instances creation with missing fields.
        """
        data = {
            'title': 'Test book',
            'ISBN': '123456789222'
        }
        response = self.client.post(reverse('library:create_book'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['author'], ['This field is required.'])
        self.assertEqual(response.json()['publish_year'], ['This field is required.'])

    def test_retrieve_book(self):
        """
        Tests a Book instance retrieval by its id.
        """
        response = self.client.get(reverse('library:get_book', kwargs={'pk': self.test_book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], self.test_book.id)
        self.assertEqual(response.json()['title'], self.test_book.title)
        self.assertEqual(response.json()['author'], self.test_book.author)
        self.assertEqual(response.json()['publish_year'], self.test_book.publish_year)
        self.assertEqual(response.json()['ISBN'], self.test_book.ISBN)

    def test_retrieve_book_wrong_id(self):
        """
        Tests a Book instance retrieval with an invalid book id.
        """
        response = self.client.get(reverse('library:get_book', kwargs={'pk': int(self.test_book.id) + 1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')

    def test_get_books(self):
        """
        Tests getting a list of Book instances.
        """
        response = self.client.get(reverse('library:get_books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.json()[0]['id'], self.test_book.id)
        self.assertEqual(response.json()[0]['title'], self.test_book.title)

    def test_put_book(self):
        """
        Tests successful Book instances update via the PUT method.
        """
        data_to_update = {
            'title': 'Test book UPDATED',
            'author': 'Me UPDATED',
            'publish_year': '2022',
            'ISBN': '123-456-789-112'
        }
        response = self.client.put(reverse(
            'library:update_book', kwargs={'pk': self.test_book.id}), data=data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], data_to_update['title'])
        self.assertEqual(response.json()['author'], data_to_update['author'])
        self.assertEqual(response.json()['publish_year'], data_to_update['publish_year'])
        self.assertEqual(response.json()['ISBN'], data_to_update['ISBN'])

    def test_patch_book(self):
        """
        Tests successful Book instances update via the PATCH method.
        """
        data_to_update = {
            'title': 'Test book UPDATED',
            'publish_year': '2022'
        }
        response = self.client.patch(reverse(
            'library:update_book', kwargs={'pk': self.test_book.id}), data=data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], data_to_update['title'])
        self.assertEqual(response.json()['author'], self.test_book.author)
        self.assertEqual(response.json()['publish_year'], data_to_update['publish_year'])
        self.assertEqual(response.json()['ISBN'], self.test_book.ISBN)

    def test_put_book_wrong_id(self):
        """
        Tests Book instances update via the PUT method with an invalid book id provided.
        """
        data_to_update = {
            'title': 'Test book UPDATED',
            'author': 'Me UPDATED',
            'publish_year': '2022',
            'ISBN': '123-456-789-112'
        }
        response = self.client.put(
            reverse('library:update_book', kwargs={'pk': int(self.test_book.id) + 1}), data=data_to_update)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')

    def test_patch_book_wrong_id(self):
        """
        Tests Book instances update via the PATCH method with an invalid book id provided.
        """
        data_to_update = {
            'title': 'Test book UPDATED',
            'publish_year': '2022'
        }
        response = self.client.patch(
            reverse('library:update_book', kwargs={'pk': int(self.test_book.id) + 1}), data=data_to_update)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')

    def test_delete_book(self):
        """
        Tests Book instances deletion from the database.
        """
        response = self.client.delete(reverse('library:delete_book', kwargs={'pk': self.test_book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.test_book.id).exists())
