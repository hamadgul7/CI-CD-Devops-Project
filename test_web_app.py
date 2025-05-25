from selenium import webdriver
import unittest
import time

class WebAppTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome browser (make sure chromedriver is in PATH)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost")  # or your web app URL

    def test_title(self):
        """Test that the page title contains expected text"""
        title = self.driver.title
        self.assertIn("My Web App", title)

    def test_content(self):
        """Test that specific content is present on the page"""
        body = self.driver.find_element("tag name", "body").text
        self.assertIn("Welcome", body)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

