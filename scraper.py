import requests
from bs4 import BeautifulSoup
import json
import os
import time

urls = [
        "https://www.reddit.com/r/QuebecTI/comments/11ti937/salaire_pour_developpeur/",
        "https://www.reddit.com/r/QuebecTI/comments/17k9tck/setup_de_t%C3%A9l%C3%A9_travail/",
        "https://www.reddit.com/r/QuebecTI/comments/17m9igj/je_capote/",
        "https://www.reddit.com/r/QuebecTI/comments/17bul2f/recherche_travail/",
        "https://www.reddit.com/r/QuebecTI/comments/17b5inm/se_d%C3%A9velopper_et_se_mettre_en_valeur_dans_un/",
        "https://www.reddit.com/r/QuebecTI/comments/17afi2c/ce_que_jaurais_du_faire_avant_ma_premiere_entrevue/",
        "https://www.reddit.com/r/QuebecTI/comments/17mnijh/un_dev_phpsymfony_%C3%A7a_peut_monter_%C3%A0_combien_%C3%A0_mtl/",
        "https://www.reddit.com/r/QuebecTI/comments/17lradj/wifi_qui_donne_mal_%C3%A0_la_t%C3%AAte/ "
    ]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os
import time

def scrape_and_save_multiple(urls, output_folder='output', use_proxies=False):
    # Set up the Chrome webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        for url in urls:
            # Make a GET request to the URL with Selenium
            driver.get(url)

            # Wait for the page to fully load (adjust the timeout as needed)
            driver.implicitly_wait(10)

            # Get the page source after waiting for the content to load
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

# Example usage with multiple URLs
urls_to_scrape = [
    'https://www.reddit.com/r/QuebecTI/comments/11ti937/salaire_pour_developpeur/',
    'https://www.reddit.com/r/QuebecTI/comments/17k9tck/setup_de_t%C3%A9l%C3%A9_travail/',
    'https://www.reddit.com/r/QuebecTI/comments/17m9igj/je_capote/',
    'https://www.reddit.com/r/QuebecTI/comments/17bul2f/recherche_travail/',
    'https://www.reddit.com/r/QuebecTI/comments/17b5inm/se_d%C3%A9velopper_et_se_mettre_en_valeur_dans_un/'
]

scrape_and_save_multiple(urls_to_scrape, use_proxies=True)

