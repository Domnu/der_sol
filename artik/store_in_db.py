import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "der_sol.settings")
django.setup()

from artik.models import PageWeb  # Import your data model
import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(level=logging.INFO)


def extraire_contenu_et_enregistrer(url):
    try:
        if url.startswith("http"):
            # Execute an HTTP request to the URL
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                contenu = soup.get_text()
            else:
                logging.error(f'HTTP request failed with status code {response.status_code}')
                return False
        else:
            with open(url, "r", encoding="utf8") as file:
                soup = BeautifulSoup(file, 'html.parser')
                contenu = soup.get_text()

        page_web = PageWeb(url=url, contenu=contenu)
        page_web.save()
        return True
    except Exception as e:
        logging.error(f"Error during the extraction and registration : {str(e)}")
    return False


ur = extraire_contenu_et_enregistrer(r"H:\der_sol\artik\templates\artik\index.html")

pages_web = PageWeb.objects.all()
print('Lin 43 store_in_db.py - pages_web =', pages_web)
