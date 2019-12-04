numerateur = input("Numerateur ")
denominateur = input("Denominateur ")
try:
    result = int(numerateur) / int(denominateur)
    assert int(numerateur) >= 10
    print(result)
except NameError:
    print("Veuillez renseigner le numerateur ET le denominateur")
except TypeError:
    print("Veuillez entrer uniquement des nombres")
except ZeroDivisionError:
    print("La divion par 0 n'est pas autorisée")
except AssertionError:
    print("On divise rien de moins de 10 ici, c'est comme ça")