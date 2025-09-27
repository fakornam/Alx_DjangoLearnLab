from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Chinua Achebe')
        self.book = Book.objects.create(title='Things Fall Apart', publication_year=1958, author=self.author)

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Things Fall Apart', str(response.data))

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'No Longer at Ease',
            'publication_year': 1960,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Arrow of God',
            'publication_year': 1964,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Things Fall Apart - Revised'}
        response = self.client.put(reverse('book-update'), {'pk': self.book.id, **data})
        self.book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Things Fall Apart - Revised')

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('book-delete'), {'pk': self.book.id})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(reverse('book-list') + f'?author={self.author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(reverse('book-list') + '?search=Things')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Things Fall Apart', str(response.data))

    def test_order_books_by_year(self):
        Book.objects.create(title='Earlier Work', publication_year=1950, author=self.author)
        response = self.client.get(reverse('book-list') + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Earlier Work')