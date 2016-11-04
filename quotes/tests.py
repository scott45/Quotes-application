from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from .models import Quote


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_to_check_django_page(self):

        # User opens browser

        self.browser.get('http://localhost:8000')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django', body.text)

        # User opens admin page

        self.browser.get('http://localhost:8000/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # User opens admin page

        self.browser.get('http://localhost:8000/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # users types in username and passwords and presses enter

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('quotes')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('quotes')
        password_field.send_keys(Keys.RETURN)

        # login credentials are correct, and the user is redirected to the main admin page

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # the user is redirected to the main admin page to ensure database models are present

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Quotes', body.text)

        # the user is redirected to the main admin page to ensure database models are present

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Votes', body.text)

        # to test string representation for models

        quote = Quote(title="Quote title")
        self.assertEqual(str(quote), quote.title)

        # to test for verbose plural name

        self.assertEqual(str(Quote._meta.verbose_name_plural), "quotes")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
