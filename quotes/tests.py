from selenium import webdriver
import unittest


class FirstTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_to_check_django_page(self):
        # User opens browser
        self.browser.get('http://localhost:8000')

        body = self.browser.find_elements_by_tag_name('body')
        assert 'Django' in self.browser.title


if __name__ == '__main__':
    unittest.main(warnings='ignore')
