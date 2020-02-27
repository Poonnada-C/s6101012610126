from django.test import LiveServerTestCase
from django.test import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
class NewVisitorTest(LiveServerTestCase):
    def test_user_can_checkout_aboutpage(self):
        self.browser.get(self.live_server_url)
        self.assertIn('about', self.browser.title)
        self.assertIn('Poonnada Chaichamniankul', self.webpage.text)
        self.assertIn('6101012610126', self.webpage.text)
