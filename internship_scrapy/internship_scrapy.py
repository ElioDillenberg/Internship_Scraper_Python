import sys
import os
import scrapy

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

# print("Ce script vous permer de trouver rapidement les offres d'emploi pour les technos qui vous intéressent\n \
#     pour info: les recherches s'effectuent pour l'instant uniquement sur Paris\n\n")

# this function handles the entire user input at the beginning and returns SMTH that will contain all the choices
# script will then chose the right website witht he right settings to scrap
def get_user_input():
    c_site = input("Veuillez sélectionner un des sites suivant à scraper\n \
    0 : Welcome to the Jungle \n\n \
    1 : LinkedIn \n\n \
    Choice : ")
    parse_input(c_site)
    c_contract = input("Veuillez sélectionner un type de contrat\n \
    0 : Stage \n\n \
    1 : CDI/CDD \n\n \
    Choice : ")
    parse_input(c_contract)
    c_language = input("Veuillez sélectionner langage\n \
    0 : Python \n\n \
    1 : Javascript \n\n \
    2 : PHP \n\n \
    Choice : ")
    parse_input(c_language)
    return c_site, c_contract, c_language

# user_choices = get_user_input()
# print(user_choices)

os.system("scrapy crawl WelcomeToTheJungle -o data.json -t json")