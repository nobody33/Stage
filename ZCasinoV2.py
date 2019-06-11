#Ce programme à pour but d'imiter le jeu de la roulette avec une interface graphique
#date de création : 23/04/19 par : Quentin Dhersin
#dernière modification le : 13/05/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*

##Déclaration des import
#permet de mettre en pause le système pour l'affichage
from os import system
#fonction pour arreter un programme
from sys import exit
#importer du module tkinter qui sert à la programmation graphique
from tkinter import *
#fonction qui permet d'arrondir au nombre supérieur
from math import ceil
#fonction qui permet de tirer un numéro au hasard
from random import randrange
#import du packtage pour afficher les messages
from tkinter import messagebox

##Déclaration des variables
#crée une fenetre jeu vide
Bienvenue = Tk()
#crée une variable pour stocker l'argent du joueur
total=IntVar()
#crée une variable pour stocker l'argent que le joueur mise
mise=IntVar()
#on initialise le numéro choisi à 0
numeroChoisi=0

"""Déclaration des fonctions"""
#fonction qui teste que la mise est possible
def testMise():
    while type(mise) is not int and mise < 1:
        try:
            mise = int(champMise.get())
        except:
            messagebox.showerror("Erreur", "veuillez entrez un nombre entier supérieur à 0")
            continue
        try:
            mise < 1 == false
        except:
            messagebox.showinfo("Attention", "Vous devez miser au moins 1$")
            continue

#fonction qui récupère le montant entré par le joueur en début de partie pour vérifier qu'il peut jouer
def testArgent():
    try:
        total = int(solde.get())
    except:
        messagebox.showerror("Erreur", "Vous devez entrer un montant supérieur à 0$")
    init = total
    #on vérifie que le joueur a assez d'argent
    if total < 1:
        #affiche un message d'erreur dans une nouvelle fenêtre
        messagebox.showinfo("Attention", "Vous devez avoir au moins 1$ pour jouer")
        #met fin au programme
        exit()
    else:
        #on supprime la première fenêtre
        Bienvenue.destroy()
        #on crée une nouvelle fenêtre
        jeu = Tk()
        #on affiche le texte de choix du nombre
        t_choix_nb = Label(jeu, text="Choisissez le numéro sur lequel vous voulez jouer")
        #on affiche le texte
        t_choix_nb.pack()
        #on crée une liste déroulante avec tous les nombres
        l_nb = Listbox(jeu)
        i = 1
        j = 0
        while j < 50:
            l_nb.insert(i, str(j))
            i += 1
            j += 1
        #on affiche la liste
        l_nb.pack()
        #demande au joueur combien il veut miser
        label = Label(jeu, text="Combien voulez-vous miser ?")
        #affiche le text dans la fenetre
        label.pack()
        #on crée une zone de texte pour l'utilisateur
        champMise = Entry(jeu, textvariable=int, width=30)
        #on affiche cette zone de saisie
        champMise.pack()
        #on crée un bouton qui va appeler la fonction testMise()
        bouton_miser = Button(jeu, text="Miser", command=lambda:testMise())
        #on affiche le bouton
        bouton_miser.pack()
        """
            mise = input("Combien voulez vous misez ? ")
                if 0 < mise <= total:
                    #on fait tourner la roulette
                    resultat = randrange(50)
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
        """
        #on démarre la boucle tKinter qui s'interrompt quand on ferme la fenetre
        jeu.mainloop()

#change le text affiché dans la fenetre jeu
label = Label(Bienvenue, text="Bienvenue au jeu de la roulette, de combien d'argent disposez vous ? ")
#affiche le text dans la fenetre
label.pack()
#on crée une zone de texte pour l'utilisateur
solde = Entry(Bienvenue, textvariable=int, width=30)
#on affiche cette zone de saisie
solde.pack()
#on crée un bouton qui va appeler la fonction testArgent()
bouton_jouer = Button(Bienvenue, text="Jouons", command=lambda:testArgent())
#on affiche le bouton
bouton_jouer.pack()

#on démarre la boucle tKinter qui s'interrompt quand on ferme la fenetre
Bienvenue.mainloop()
#met le system en pause pour qu'il reste affiché à l'écran
system("pause");
