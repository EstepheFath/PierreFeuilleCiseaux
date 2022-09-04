import random
from random import randint

user_choice = int(input("Choisissez une chiffre: 0 pour pierre / 1 pour papier / 2 pour ciseaux : "))

if user_choice == 0:
    print ("Vous avez choisi la pierre.")

if user_choice == 1:
    print ("Vous avez choisi le papier.")

if user_choice == 2:
    print ("Vous avez choisi les ciseaux.")


computer_choice = random.randint(0,2)

print ("Computer chose :"+ str(computer_choice))

if ((computer_choice == 0) and (user_choice == 1)) or (computer_choice == 2 and (user_choice == 0)) or (computer_choice == 1 and (user_choice == 2)):
    print ("Vous avez gagné!")

if ((computer_choice == 0) and (user_choice == 2)) or ((computer_choice == 1) and (user_choice == 0)) or ((computer_choice == 2) and (user_choice == 1)):
    print ("Vous avez perdu!")