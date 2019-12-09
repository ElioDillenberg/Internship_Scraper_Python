import sys
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

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

website_list = [("Welcome to the Jungle", "https://www.welcometothejungle.com/fr/jobs?page=1&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Project%20%2F%20Product%20Management&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=DevOps%20%2F%20Infra&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Frontend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=QA&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Hardware&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Mobile&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=T%C3%A9l%C3%A9coms%20%2F%20R%C3%A9seaux&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=S%C3%A9curit%C3%A9&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=50000&aroundPrecision=50000")]

# user_choices = get_user_input()
# print(user_choices)

session = HTMLSession()

r = session.get("https://www.welcometothejungle.com/fr/jobs?page=1&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Project%20%2F%20Product%20Management&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=DevOps%20%2F%20Infra&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Frontend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=QA&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Hardware&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Mobile&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=T%C3%A9l%C3%A9coms%20%2F%20R%C3%A9seaux&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=S%C3%A9curit%C3%A9&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=50000&aroundPrecision=50000")
soup1 = BeautifulSoup(r, 'lxml')
# soup2 = BeautifulSoup(r.html.render(), 'lxml')
ul_list = soup1.find_all('ul')
print(ul_list)
# links = r.html.find('.sc-1kkiv1h-2 cHZvby', First=true)
# print(links)

# source = requests.get('https://www.welcometothejungle.com/fr/jobs?page=1&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Project%20%2F%20Product%20Management&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=DevOps%20%2F%20Infra&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Frontend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=QA&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Hardware&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Mobile&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=T%C3%A9l%C3%A9coms%20%2F%20R%C3%A9seaux&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=S%C3%A9curit%C3%A9&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=50000&aroundPrecision=50000').text
# soup = BeautifulSoup(source, 'lxml')
# ul_list = soup.find_all('ul')
# print(ul_list)