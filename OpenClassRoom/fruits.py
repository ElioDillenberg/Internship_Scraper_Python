from operator import itemgetter

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

inventaire.sort(key = itemgetter(1))
print(inventaire)