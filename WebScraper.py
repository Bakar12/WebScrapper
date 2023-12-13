
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the headlines on the page using the specified CSS class
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

        # If no headlines are found, log a warning and return None
        if not headlines:
            logging.warning("No headlines found. The site's structure may have changed.")
            return None

        # Extract the text from each headline and strip any leading/trailing whitespace
        return [headline.get_text().strip() for headline in headlines]

    except requests.RequestException as e:
        # Log an error if there's an issue fetching data from the URL
        logging.error(f"Error fetching data from {url}: {e}")
        return None

def main():
    # Configurability: Allow user to input URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://www.bbc.com/news"  # Default URL

    # Log the URL being scraped
    logging.info(f"Scraping headlines from {url}")

    # Call the scrape_headlines function to retrieve the headlines
    data = scrape_headlines(url)

    if data:
        # If headlines are retrieved, create a DataFrame and save it to a CSV file
        df = pd.DataFrame(data, columns=['Headline'])
        df.to_csv('headlines.csv', index=False)
        logging.info("Headlines saved to headlines.csv")
    else:
        # If no headlines are retrieved, log a message indicating no data to save
        logging.info("No data to save.")

if __name__ == "__main__":
    main()
    