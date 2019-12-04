import sys
import requests
from bs4 import BeautifulSoup

def get_user_input():
    c_site = input("Veuillez sélectionner un des sites suivant à parser\n \
        0 : Welcome to the Jungle \n\n\
        Choice : ")
    try:
        c_site = int(c_site)
        assert c_site == 0
    except AssertionError:
        print("Le numero fourni ne correspond à aucun des choix proposés")
        sys.exit()
    except ValueError:
        print("Veuilez fournir un chiffre valide")
        sys.exit()
    except:
        print("TYPE ERREUR INCONNU")
        sys.exit()

    c_contract = input("Veuillez sélectionner un type de contrat\n \
        0 : Stage \n\n\
        Choice : ")

    try:
        c_site = int(c_site)
        assert c_site == 0
    except AssertionError:
        print("Le numero fourni ne correspond à aucun des choix proposés")
        sys.exit()
    except ValueError:
        print("Veuilez fournir un chiffre valide")
        sys.exit()
    except:
        print("TYPE ERREUR INCONNU")
        sys.exit()
    return c_site, c_contract

website_list = [("Welcome to the Jungle", "https://www.welcometothejungle.com/fr/jobs")]

user_input = get_user_input()

source = requests.get('https://www.welcometothejungle.com/fr/jobs').text
soup = BeautifulSoup(source, 'lxml')
job_links = soup.find_all('a')
for link in job_links:
    print(link['href'])