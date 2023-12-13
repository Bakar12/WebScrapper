import unittest
import sys
import os

# Append the project root directory to sys.path
project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(project_root)

from WebScraper import scrape_headlines


class TestWebScraper(unittest.TestCase):

    def test_scrape_headlines_valid(self):
        # Test case to check if scrape_headlines returns a valid result
        result = scrape_headlines("https://www.bbc.com/news")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_scrape_headlines_invalid(self):
        # Test case to check if scrape_headlines returns None for an invalid URL
        result = scrape_headlines("https://invalidurl.com")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
