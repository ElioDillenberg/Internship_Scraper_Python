import sys
import math
import random

nb_party_input = input("Please provide the number of participants ")

try:
    nb_party = int(nb_party_input)
except:
    print("Please provide a valid number of players")
    raise SystemExit

participants = list()
for i in range(nb_party):
    participants.append(input("Please provide participant names : "))

print(participants)

to_remove = input("Who do you want to remove ? ")
if to_remove in participants:
    participants.remove(to_remove)
else:
    print(to_remove, "isn't even part of secret santa man.. c'mon")

print(participants)
print(participants[0][2:])