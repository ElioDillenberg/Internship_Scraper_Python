import sys
import os

def parse_input(user_input):
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

# ADD NEW SPIDERS TO THIS LIST (spiders need to have the same name as in their Scrapy classes)
spiders = list()
spiders.append("WelcomeToTheJungle")

# prompt user for website to scrape -> retuns index of corresponding website
def get_user_input(spiders):
    print ("Veuillez sélectionner un des sites suivant à scraper \n")
    for i, spider in enumerate(spiders):
        print(str(i) + " : " + spider)
    c_site = input("Choice : ")
    parse_input(c_site)
    return int(c_site)

user_choice = get_user_input(spiders)

# calling scrapy from system to start crawling user choice / comment if you want to scrap all with bellow
scrapy_call = "scrapy crawl " + spiders[user_choice] + " -o " + spiders[user_choice] + ".json -t json"
os.system(scrapy_call)

# Uncomment below to execute script on all websites (need to comment the two lines above)
# for spider in spiders:
#     scrapy_call = "scrapy crawl " + spider + " -o " + spider + ".json -t json"
#     os.system(scrapy_call)