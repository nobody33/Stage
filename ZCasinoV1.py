#Ce programme à pour but d'imiter le jeu de la roulette
#date de création : 18/04/19 par : Quentin Dhersin
#dernière modification : 23/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
import os #import du module os
import sys #import du module sys
from math import ceil #on importe la fonction ceil du module math
from random import randrange #on importe la fonction randrange du module random

print("Bienvenue au jeu de la roulette, vous pouvez quittez la table en disant aurevoir au moment de saisir un numéro")
numeroChoisi="" #on initialise le numéro choisi à 0

total=input("De combien d'argent disposez vous ? ") #le joueur indique l'argent qu'il à pour jouer
total=int(total)
init = total
if total < 1: #on vérifie que le joueur a assez d'argent
    print("Vous devez avoir au moins 1$ pour jouer")
    os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
    sys.exit()

while total > 0 and numeroChoisi != "aurevoir": #tant que le joueur a de l'argent
    numeroChoisi = input("\nChoisissez un numéro entre 0 et 49 inclut : ") #le joueur choisi le numéro à jouer
    if numeroChoisi == "aurevoir":
        continue
    try:
        numeroChoisi = int(numeroChoisi)
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
        continue
    if 0 <= numeroChoisi < 50:
        mise = input("Combien voulez vous misez ? ") #le joueur choisi combien il mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi un nombre")
            continue
        if 0 < mise <= total:
            resultat = randrange(50) #on fait tourner la roulette
            print("Le numéro tiré est le", resultat)
            if resultat == numeroChoisi:
                mise=ceil(mise * 3)
                total += mise
                print("Bien joué vous avez le bon numéro, votre solde actuel est de", total, "$\n")
            elif (numeroChoisi%2) == (resultat%2):
                mise = ceil(mise *0.5)
                total += mise
                print("Bien joué vous avez la bonne couleur, votre solde actuel est de", total, "$\n")
            else:
                total -= mise
                print("Vous avez perdu, votre solde actuel est de", total, "$\n")
        elif mise < 0:
            print("Vous devez rentrer une mise positive")
        else:
            print("Vous ne pouvez pas miser autant, vous ne disposez que de", total, "$")
    else:
        print("Veuillez choisir un numéro entre 0 et 49 inclut")

print("\nMerci d'avoir joué vous êtes arrivé avec", init, "$ et vous repartez avec", total, "$")
os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
