import sys
import requests
from bs4 import BeautifulSoup

def parse_input(user_input): # maybe here we should send the list from which to pick 
    try:
        user_input = int(user_input)
        assert user_input == 0 # need to link this to a list of possible choices
    except AssertionError:
        print("Le numero fourni ne correspond à aucun des choix proposés")
        sys.exit()
    except ValueError:
        print("Veuilez fournir un chiffre valide")
        sys.exit()
    except:
        print("TYPE ERREUR INCONNU")
        sys.exit()


# this function handles the entire user input at the beginning and returns SMTH that will contain all the choices
# script will then chose the right website witht he right settings to scrap
def get_user_input():
    c_site = input("Veuillez sélectionner un des sites suivant à parser\n \
        0 : Welcome to the Jungle \n\n\
        Choice : ")
    parse_input(c_site)
    c_contract = input("Veuillez sélectionner un type de contrat\n \
        0 : Stage \n\n\
        Choice : ")
    parse_input(c_contract)
    c_language = input("Veuillez sélectionner un type langage\n \
    0 : Python \n\n\
    1 : Javascript \n\n\
    Choice : ")
    parse_input(c_language)
    return c_site, c_contract, c_language

website_list = [("Welcome to the Jungle", "https://www.welcometothejungle.com/fr/jobs")]

user_choices = get_user_input()

print(user_choices)

source = requests.get('https://www.welcometothejungle.com/fr/jobs').text
soup = BeautifulSoup(source, 'lxml')
job_links = soup.find_all('a')
for link in job_links:
    print(link['href'])