# -------------------------------------------
# Import the necessary libraries
# -------------------------------------------

import pdb
# To parameterize the script for cmd execution
import argparse

# To access web pages 
import requests

# To parse the website contents
from bs4 import BeautifulSoup

# To manage files
from pathlib import Path

# -------------------------------------------
# Parse command line arguments
# -------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Scrape Economic Survey PDFs from KNBS website")
    parser.add_argument('--url', 
                        type=str, 
                        required=True, 
                        help='Start URL of the KNBS reports page')
    
    parser.add_argument('--output-dir', 
                        type=str, 
                        default='datafiles/', 
                        help='Directory to save downloaded files')
    
    return parser.parse_args()

# -------------------------------------------
# Fetch the web page
# -------------------------------------------
def fetch_url(url):
    """
    Fetches a specified url
    Args:
        url - the target web page to fetch
    Returns:
        HTMLResponse - a HTML response object
    """
    
    try:
        response = requests.get(url)
        response.raise_for_status
    except requests.RequestException as e:
        print(f"Error: {e}")
        response = None

    return response
    

# -------------------------------------------
# Parse HTML and extract PDF links
# -------------------------------------------    
def extract_pdf_links(html):
    """
    Parses HTML and returns a list of PDF links.
    Args:
        html: str - the fetched HTML Response Page
    Returns:
        list, BeautifulSoup object - pdf links and a soup object
    """
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a')
    pdf_links = [a['href'] for a in anchors if 'href' in a.attrs and a['href'].endswith('pdf')]
    return pdf_links, soup


# -------------------------------------------
# Download files to output directory
# -------------------------------------------
def download_files(pdf_links, output_dir):
    """
        Download files from the URL provided into the output_dir location
        Args:
            url - website URL to access
            output_dir - folder to save the downloaded files
        Returns:
            None
    """
    # Create the output directory if it does not exist
    OUTPUT_PATH = Path(output_dir)
    OUTPUT_PATH.mkdir(exist_ok=True)

    for link in pdf_links:
        filename = link.rsplit('/', 1)[-1]
        filepath = OUTPUT_PATH / filename

        if filepath.exists():
            print(f"{filename} already exists. Skipping.")
            continue

        content = fetch_url(link)
        filepath.write_bytes(content.content)
        print(f"Downloaded: {filename}")

# -------------------------------------------
# Handle pagination recursively
# -------------------------------------------
def handle_pagination(soup, output_dir):
    """
    Checks for 'next' page and recursively processes it.
    """
    next_page = soup.find('a', class_='next page-numbers')
    if next_page:
        next_url = next_page['href']
        print(f"Navigating to next page: {next_url}")
        process_page(next_url, output_dir)

# ----------------------------
# Main scraping function
# ----------------------------
def process_page(url, output_dir):
    """
    Combined logic for fetching, parsing, downloading and paginating.
    """
    response = fetch_url(url)
    if response.status_code == 200:
        pdf_links, soup = extract_pdf_links(response.text)
        download_files(pdf_links, output_dir)
        handle_pagination(soup, output_dir)
    else:
        print(f"Failed to fetch {url}: {response.reason}")


# -------------------------------------------
# Program execution entry point
# -------------------------------------------
if __name__ == "__main__":
    # Filter 'economic survey' on the 
    # Kenya National Bureau of Statistics(KNBS) website
    
    # URL = "https://www.knbs.or.ke/all-reports/page/1/?filter_sub_category_7867=economic_surveys"
    # Use this URL for the economic survey reports only

    # URL = "https://www.knbs.or.ke/all-reports/"  
    # Use this URL to download all reports, uncomment it

    # parse command line arguments
    args = parse_args()

    print(f"Scraping from: {args.url}")
    print(f"Saving files to: {args.output_dir}")

    process_page(args.url, args.output_dir)