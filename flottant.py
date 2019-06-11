#Ce programme à pour but de renvoyer un float avec seulement 3 décimal et en remplaçant le . par ,
#date de création : 19/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
import os #import du module os

def flottant(nb):
    while type(nb) is not int:
        nb = 0
        nb = input("Entrez un nombre à virgule : ")
        try:
            nb = float(nb)
        except:
            print("Veuillez entrer un nombre à virgule")
            continue
        nb = str(nb)
        entier, flottant = nb.split(".")
        nb = ",".join([entier, flottant[:3]])
        print(nb)
        nb = 0

flottant(float)

os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
