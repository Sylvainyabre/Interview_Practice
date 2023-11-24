import requests
from bs4 import BeautifulSoup
import json
import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
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


def scrape_and_save_multiple(urls, output_folder='output', use_proxies=False):
  
    driver = webdriver.Chrome()

    try:
        for url in urls:
            # Make a GET request to the URL with Selenium
            driver.get(url) 
            driver.implicitly_wait(30)
            # Get the page source after waiting for the content to load
            page_source = driver.page_source
           
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            # Find the element using data-test-id
            posts = soup.find_all('p')
        
            if posts:
                data = {'paragraphs': []}
                for post in posts:
                    text_content = post.get_text(strip=True)
                    data['paragraphs'].append(text_content)
                    # Extract the text content from the div
                   
                # Create the output folder if it doesn't exist
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                # Save the data as JSON in the output folder
                output_file = os.path.join(output_folder, f"{url.split('//')[1].replace('/', '_')}.json")
                with open(output_file, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=2)

                print(f"Data extracted from {url} and saved to {output_file}")
                time.sleep(20)
            else:
                print(f"No post content found on {url}")

    finally:
        # Close the webdriver
        driver.quit()

# Example usage with multiple URLs
urls_quebec = [
    "https://www.reddit.com/r/QuebecTI/comments/11ti937/salaire_pour_developpeur/",
    "https://www.reddit.com/r/QuebecTI/comments/17k9tck/setup_de_t%C3%A9l%C3%A9_travail/",
    "https://www.reddit.com/r/QuebecTI/comments/17m9igj/je_capote/",
    "https://www.reddit.com/r/QuebecTI/comments/17bul2f/recherche_travail/",
    "https://www.reddit.com/r/QuebecTI/comments/17b5inm/se_d%C3%A9velopper_et_se_mettre_en_valeur_dans_un/",
    "https://www.reddit.com/r/QuebecTI/comments/17afi2c/ce_que_jaurais_du_faire_avant_ma_premiere_entrevue/",
    "https://www.reddit.com/r/QuebecTI/comments/17mnijh/un_dev_phpsymfony_%C3%A7a_peut_monter_%C3%A0_combien_%C3%A0_mtl/",
    "https://www.reddit.com/r/QuebecTI/comments/17lradj/wifi_qui_donne_mal_%C3%A0_la_t%C3%AAte/",
   " https://www.reddit.com/r/QuebecTI/comments/17s5r2f/vos_exp%C3%A9riences_et_opinions_sur_la_m%C3%A9thodologie/",
   "https://www.reddit.com/r/QuebecTI/comments/17rrszj/des_ressources_gratuites_pour_les_scrum_master_et/",
   "https://www.reddit.com/r/QuebecTI/comments/17s2t82/choix_post_bac_informatique_g%C3%A9nie_logiciel/",
   "https://www.reddit.com/r/QuebecTI/comments/17pw6uh/estce_que_%C3%A7a_vaut_la_peine_daller_dobtenir_un/",
   "https://www.reddit.com/r/QuebecTI/comments/17mnijh/un_dev_phpsymfony_%C3%A7a_peut_monter_%C3%A0_combien_%C3%A0_mtl/",
  "https://www.reddit.com/r/QuebecTI/comments/17h6pi8/analyste_de_donn%C3%A9es_%C3%A0_temps_partiel/",
  "https://www.reddit.com/r/QuebecTI/comments/16sy7l8/entrevue_poste_danalyste_programmeur/",
  "https://www.reddit.com/r/QuebecTI/comments/16pv1r3/devops_formation/",
  "https://www.reddit.com/r/QuebecTI/comments/16orfso/se_sent_coinc%C3%A9_%C3%A0_l%C3%A9cole/"
  "https://www.reddit.com/r/QuebecTI/comments/16ll2p3/apprendre_a_bien_cod%C3%A9_et_structur%C3%A9_un_projet/",
  "https://www.reddit.com/r/QuebecTI/comments/16iw6sl/avisconseils_pour_faire_le_switch_design_uiux/",
  "https://www.reddit.com/r/QuebecTI/comments/16gyvxl/coup_de_gueule_les_quiz_dembauche_techniques/",
  "https://www.reddit.com/r/QuebecTI/comments/16bvdub/carri%C3%A8re_en_gestion_de_produit_saas_par_o%C3%B9/",
  "https://www.reddit.com/r/QuebecTI/comments/169kld7/cyber_forensics/",
  "https://www.reddit.com/r/QuebecTI/comments/16305eo/transition_devs_%C3%A0_managementsm/",
  "https://www.reddit.com/r/QuebecTI/comments/15uzmu5/valeur_dun_dess_ou_programme_court_de_2e_cycle/",
  "https://www.reddit.com/r/QuebecTI/comments/15tt8en/reconversion_ing%C3%A9nieur_data_scientistanalyst/"
  ]

scrape_and_save_multiple(urls_quebec,output_folder='output_quebec')