#Ce programme à pour but d'indiquer l'argent que je gagne chaque minutes
#date de création : 19/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
import os #import du module os
from time import sleep #import de la fonction sleep pour attendre
from math import ceil #import de la fonction ceil pour arrondir les nombres

#déclaration des variables
total = float()
message = str()
gainMinute = 0.069
gainSeconde = 0.00115
choix = str()
temps = int()

print("Tu désire avoir ton gain en seconde ou en minute ?")
choix = input("Entre s pour seconde ou m pour minute : ")
while True:
    if choix.lower() == "s":
        total += gainSeconde
        temps += 1
        print("tu as gagné", round(total, 5), "€ en", temps, "secondes GG frero")
        if total == 10:
            print("Bien joué t'as gagné de quoi payer le macdo")
        sleep(1)
    elif choix.lower() == "m":
        total += gainMinute
        temps += 1
        print("tu as gagné", round(total, 5), "€ en", temps, "minutes GG frero")
        if total == 10:
            print("Bien joué t'as gagné de quoi payer le macdo")
        sleep(60)
    else:
        print("lis bien la conssigne faut juste taper m ou s tocard")
        choix = input("Entre s pour seconde ou m pour minute : ")

os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
