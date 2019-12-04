# from math import sqrt as s
import math as m

def print10(nb=10):
    i = 0
    while (i < 10):
        print(nb)
        i += 1
        nb += 1

def print11(nb=10):
    for i in range(10):
        print(nb + i)

number = input("NB : ")
print10(int(number))
print("\n", number, end="saucisse\n", sep="")

print(m.sqrt(int(number)))