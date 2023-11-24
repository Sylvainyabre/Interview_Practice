from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import os

def scrape_and_save(url, output_folder='output', use_proxies=False):
    # Set up the Chrome webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Make a GET request to the URL with Selenium
        driver.get(url)

        # Explicitly wait for the post-content element to be present
        post_content_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="post-content"]'))
        )

        # Get the page source after the content is fully loaded
        page_source = driver.page_source

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the element using data-test-id
        post_content_div = soup.find('div', {'data-test-id': 'post-content'})
        # Check if the content was found
        if post_content_div:
            # Extract the text content from the div
            text_content = post_content_div.get_text(strip=True)

            # Create a dictionary to store the extracted data
            data = {'url': url, 'text_content': text_content}

            # Create the output folder if it doesn't exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Save the data as JSON in the output folder
            output_file = os.path.join(output_folder, f"{url.split('//')[1].replace('/', '_')}.json")
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=2)

            print(f"Data extracted from {url} and saved to {output_file}")
        else:
            print(f"No post content found on {url}")

    finally:
        # Close the webdriver
        driver.quit()

# Example usage with a single URL
url_to_scrape = 'https://www.reddit.com/r/QuebecTI/comments/11ti937/salaire_pour_developpeur/'
scrape_and_save(url_to_scrape, use_proxies=True)
