from django.test import SimpleTestCase
from django.urls import reverse, resolve
from panel.urls import *


class TestUrls(SimpleTestCase):

    def test_books_urls_is_resolved(self):
        url = reverse('panel_index')
        self.assertEqual(resolve(url).func, index)

    def test_book_create_urls_is_resolved(self):
        url = reverse('book_view')
        self.assertEqual(resolve(url).func, book_view)

    def test_books_check_urls_is_resolved(self):
        url = reverse('book_check')
        self.assertEqual(resolve(url).func, book_check)

    def test_book_detail_urls_is_resolved(self):
        url = reverse('event_list')
        self.assertEqual(resolve(url).func, event_list)

    def test_confirmed_book_urls_is_resolved(self):
        url = reverse('customer_view')
        self.assertEqual(resolve(url).func, customer_view)

    def test_books_delete_urls_is_resolved(self):
        url = reverse('panel_event_post')
        self.assertEqual(resolve(url).func, panel_event_post)

