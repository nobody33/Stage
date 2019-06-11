#Ce programme à pour but de tester la programmation grahique
#date de création : 23/04/19 par : Quentin Dhersin
#dernière modification le : 26/04/19 par : Quentin Dhersin

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*
from tkinter import * #importer du module tkinter qui sert à la programmation graphique
from tkinter import messagebox #import de messagebox qui sert à afficher des alert

#crée une fenetre yo vide
fenêtre = Tk()
#change le text affiché dans la fenetre yo
label = Label(fenêtre, text="Hello world")
#affiche le text dans mla fenetre
label.pack()

#création d'une scrollbar
scrollbar = Scrollbar(fenêtre, orient=HORIZONTAL)
scrollbar.pack()

#crée un canevas
canevas1 = Canvas(fenêtre, width=200, height=100, yscrollcommand=scrollbar.set, scrollregion=(0,0,1000,1000))
#affiche le canevas
canevas1.pack()
#trace une ligne avec comme paramètre x1, y1, x2, y2
canevas1.create_line(0, 50, 2000, 50)
canevas1.create_line(0, 49, 2000, 49)
canevas1.create_line(0, 48, 2000, 48)
canevas1.create_line(0, 51, 2000, 51)
canevas1.create_line(0, 52, 2000, 52)

scrollbar.config(command=canevas1.yview)

#crée une liste
liste = Listbox(fenêtre)
#remplie la liste
liste.insert(1, "premier")
liste.insert(2, "second")
#affiche la liste
liste.pack()
#affiche la liste dans une fenêtre d'information
messagebox.showinfo("info", liste)

#on crée une variable chaine de caractère de Tkinter
var_texte=IntVar()
#on crée une zone de texte pour l'utilisateur
ligne_texte= Entry(fenêtre, textvariable=var_texte, width=30)
#on affiche cette zone de saisie
ligne_texte.pack()
#on crée un bouton qui va fermer la fenêtre
quitter = Button(fenêtre, text="Quitter", command=lambda:fenêtre.quit())
#on affiche le bouton
quitter.pack()

#on démarre la boucle tKinter qui s'interrompt quand on ferme la fenetre
fenêtre.mainloop()

#inutile de mettre os.system("pause") lorsque tout se passe dans une interface graphique
