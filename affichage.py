#Ce programme à pour but de tester l'affichage
#date de création : 19/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
import os #import du module os
from time import sleep #import de la fonction sleep pour attendre

texte = input("Entrez le texte à afficher : ")
x = 0
i = 0
couleur = str()

while True:
    print(texte.center(i))
    couleur = "color " + str(x)
    os.system(couleur)
    int(x)
    if x > 9:
        x = 0
    x += 1
    i += 1
    sleep(1)

os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
