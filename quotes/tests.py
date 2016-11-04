from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from .models import Quote


class QuotesTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_to_check_functionality(self):

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

        # to test string representation for models

        quote = Quote(title="Quote title")
        self.assertEqual(str(quote), quote.title)

        # to test for verbose plural name

        self.assertEqual(str(Quote._meta.verbose_name_plural), "quotes")

        # test to ensure user can add data

        # user clicks on the Quotes link

        quotes_links = self.browser.find_elements_by_link_text('Quotes')
        quotes_links[0].click()

        # user clicks on the Add Quote link

        add_quote_link = self.browser.find_element_by_link_text('Add')
        add_quote_link.click()

        # user fills out the form
        self.browser.find_element_by_name('title').send_keys(' "Stay hungry, Stay foolish" Steve Jobs')
        self.browser.find_element_by_name('submitter').send_keys("Quotes")
        self.browser.find_element_by_name('description').send_keys("What an amazing quote")

        # user clicks the save button

        self.browser.find_element_by_css_selector("input[value='Save']").click()

        # the Quote has been added

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Stay hungry', body.text)

        # user returns to the main admin screen

        home_link = self.browser.find_element_by_link_text('Home')
        home_link.click()

        # user clicks on the Quotes link

        quotes_links = self.browser.find_elements_by_link_text('Quotes')
        quotes_links[0].click()

        # user clicks on the Add Quote link

        add_quote_link = self.browser.find_element_by_link_text('Add')
        add_quote_link.click()

        # user fills out the form
        self.browser.find_element_by_name('title').send_keys(' "You can be anything in this world" Apostle Grace L')
        self.browser.find_element_by_name('submitter').send_keys("Quotes")
        self.browser.find_element_by_name('description').send_keys("What an amazing quote")

        # user clicks the save button

        self.browser.find_element_by_css_selector("input[value='Save']").click()

        # the Quote has been added

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('You can be anything', body.text)

        # user returns to the main admin screen

        home_link = self.browser.find_element_by_link_text('Home')
        home_link.click()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
