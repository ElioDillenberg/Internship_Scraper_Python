import sys
import math
import random

num = input("Please provide a number between 0 and 49 : ")
mise = input("How much do you want to bet? ")

try:
    num = int(num)
    assert num > 0
    assert num < 50
    mise = int(mise)
except AssertionError:
    print("Number must be between 0 and 49")
    raise SystemExit
except:
    print("Please provide a valid number")
    raise SystemExit

winner = random.randrange(50)
w_pair = 1 if winner % 2 == 0 else 0
n_pair = 1 if num % 2 == 0 else 0 

if num == winner:
    print("BINGO! : vous repartez avec $", mise * 4, sep="")
elif w_pair == n_pair:
    print("Pas mal! : vous repartez avec $", math.ceil(mise + mise / 2), sep="")
else:
    print("Dommage pour cette fois.. mais c'est perdu!")