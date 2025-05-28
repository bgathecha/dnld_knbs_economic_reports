# --------------------------------------
# Import necessary modules and libraries
# --------------------------------------
import unittest
from bs4 import BeautifulSoup
from scraper import fetch_url
from scraper import extract_pdf_links

# --------------------------------------
# Test Cases
# --------------------------------------
class TestScraper(unittest.TestCase):

    def test_extract_pdf_links(self):
        sample_html = '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <title>A sample page for unit tests</title>
                </head>
                <body>
                    <div class="main-container">
                        <h1>Dummy links</h1>
                        <a href="report1.pdf">Report 1</a>
                        <a href="https://example.com/report2.pdf">Report 2</a>
                        <a href="image.jpg">Not a PDF</a>
                    </div>
                </body>
            </html>
        '''
        links, _ = extract_pdf_links(sample_html)
        self.assertEqual(len(links), 2)
        self.assertIn('report1.pdf', links)
        self.assertIn('https://example.com/report2.pdf', links)

    def test_fetch_url_status(self):
        url = "https://www.knbs.or.ke"
        response = fetch_url(url)
        self.assertEqual(response.status_code, 200)

# --------------------------------------
# Entry point for tests if run directly
# --------------------------------------
if __name__ == "__main__":
    unittest.main()