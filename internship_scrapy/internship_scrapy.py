import sys
import os

def parse_input(user_input, len):
    try:
        user_input = int(user_input)
        assert user_input < len
    except AssertionError:
        print("Le numero fourni ne correspond à aucun des choix proposés")
        sys.exit()
    except ValueError:
        print("Veuilez fournir un chiffre valide")
        sys.exit()
    except:
        print("TYPE ERREUR INCONNU")
        sys.exit()

# ADD NEW SPIDERS TO THIS LIST (spiders need to have the same name as in their Scrapy classes)
spiders = list()
spiders.append("WelcomeToTheJungle")

languages = list()
languages.append("Python")
languages.append("PHP")
languages.append("Javascript")

# prompt user for website to scrape -> retuns index of corresponding website
def get_user_input(spiders, languages):
    print ("Veuillez sélectionner un des sites suivant à scraper \n")
    for i, spider in enumerate(spiders):
        print(str(i) + " : " + spider + "\n")
    c_site = input("Choice : ")
    parse_input(c_site, len(spiders))
    print ("\nVeuillez un des langages suivants \n")
    for i, language in enumerate(languages):
        print(str(i) + " : " + language + "\n")
    c_language = input("Choice : ")
    parse_input(c_language, len(languages))

    return int(c_site), int(c_language)

user_choice = get_user_input(spiders, languages)

# calling scrapy from system to start crawling user choice / comment if you want to scrap all with bellow
scrapy_call = "scrapy crawl " + spiders[user_choice[0]] + " -a language=" + languages[user_choice[1]] + " -o " + spiders[user_choice[0]] + ".json -t json"
os.system(scrapy_call)