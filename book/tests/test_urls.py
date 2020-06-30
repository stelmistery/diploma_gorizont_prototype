from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from book.views import room_check, book_process, book_confirmed


class TestUrls(SimpleTestCase):

    def test_check_urls_is_resolved(self):
        url = reverse('room_check')
        self.assertEqual(resolve(url).func, room_check)

    def test_process_urls_is_resolved(self):
        url = reverse('book_form')
        self.assertEqual(resolve(url).func, book_process)

    def test_confirmed_urls_is_resolved(self):
        url = reverse('book_conf')
        self.assertEqual(resolve(url).func, book_confirmed)