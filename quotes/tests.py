# unit tests for app
# Remember: Functional tests are the ultimate indicator of whether your Project works or not,
# while Unit tests are the means to help you reach that end. This will all make sense soon.

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from .views import index


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/index/')
        self.assertEqual(found.func, index)

    def test_index_returns_right_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>quotes</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
