""" tests file container """
from datetime import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest

class TestWeb(unittest.TestCase):
    """Class containing Web related tests"""

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://www.python.org")

    def tearDown(self):
        for _, error in self._outcome.errors:
            if error:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                self.driver.get_screenshot_as_file(
                    self._testMethodName + f"_{timestamp}" + ".png")
        self.driver.close()

    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""

    @pytest.mark.web
    def test_open_python_web(self):
        """Goes to pytest news main page"""
        self.assertIn('Python', self.driver.title,
            "open page does not contain python in title")
        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", self.driver.page_source,
            "No results were found")

    @pytest.mark.web
    def test_open_wiki_fail(self):
        """Goes to pytest news main page"""
        self.assertIn('Wikipedia', self.driver.title,
            "open page does not contain python in title")
