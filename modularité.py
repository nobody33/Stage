#Ce programme à pour but de tester le principe de modularité
#date de création : 18/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
import os #import du module os
import testPackage.multipli #on importe le module multipli du package testPackage
import testPackage.Bissextile #on importe le module Bissextile du package testPackage


#test de la fonction table
testPackage.multipli.table(5)
testPackage.multipli.table(8, 3)

#déclaration des variables
i_annee = input("Entrez une année : ");#on récupère la saisie de l'utilisateur dans i_annee sous forme de string
b_bissextile = False;#on déclare un booleen b_bissextile à False par défaut pour déterminer l'affichage final

#on gère le cas où l'utilisateur ne rentre pas un nombre entier
while i_annee != int:
    try:
        #on convertie i_annee en integer
        i_annee = int(i_annee);
        break;
    except:
        print("Vous devez entrer une année");
        i_annee = input("Entrez une année : ");

#test de la fonction bissextile
testPackage.Bissextile.bissextile(i_annee)

os.system("pause"); #met le system en pause pour qu'il reste affiché à l'écran
