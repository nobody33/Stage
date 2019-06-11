#Ce programme est l'interface de l'application USERSKCP
#date de création : 25/04/19 par : Quentin Dhersin
#dernière modification le : 10/05/19 par : Quentin Dhersin

#cette version est la première interface graphique finale

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour window en général
# -*-coding:Latin-1 -*

"""---Déclaration des import---"""
#import du module tkinter qui sert à la programmation graphique
from tkinter import *
#import du packtage messagebox appertenant à tkinter qui sert à afficher des fenêtres avec message
from tkinter import messagebox
#import du packtage tix appertenant à tkinter pour créer des listes déroulantes
from tkinter import tix
#import du module datetime pour avoir la date et l'heure actuelle
import datetime
#import de ttk pour créer des treeview
import tkinter.ttk as ttk

"""déclaration des fonctions"""
#cette fonction permet d'afficher tous les tuples correspondant aux critères entré
#elle est appeler lors du clic sur le bouton chercher
def recherche():
    messagebox.showinfo("Infos", "Recherche réussi")

    """effectuer la recherche SQL dans la table sqlServer
    afficher tous les résultats dans le treeview"""

#cette fonction permet de modifier un tuple
#elle est appeler lors du clic sur le bouton modifier
def modifier():

    #cette fonction permet d'anuler la modification en cours
    #elle est appeler lors du clic sur le bouton annuler
    def annulerModification():
        #on réactive tous les boutons de la fenetre_principale
        bouton_chercher.config(state=NORMAL)
        bouton_modifier.config(state=NORMAL)
        bouton_inserer.config(state=NORMAL)
        bouton_quitter.config(state=NORMAL)

        #on ferme la fenêtre fenetre_modifier
        fenetre_modifier.destroy()

    #cette fonction permet de modifier dans la base de donnée la ligne selectionnée
    #elle est appeler lors du clic sur le bouton enregistrer
    def modifierBD():
        global Outlook_modifier
        global acces_internet_modifier
        global vpn_modifier
        global sap_modifier
        global perif_modifier
        global pc_old_modifier
        if champ_compte_window_modifier.get() != "" and liste_type_modifier['selection'] != "" and champ_nom_modifier.get() != "" and champ_prenom_modifier.get() != "" and liste_ouverture_statut_modifier['selection'] != "" and champ_ouverture_date_modifier.get() != "" and liste_fermeture_statut_modifier['selection'] != "":
            #on vérifie que la date est au bon format
            if len(champ_ouverture_date_modifier.get()) == 10 and (len(champ_fermeture_date_modifier.get()) == 10 or len(champ_fermeture_date_modifier.get())) == 0:
                #on ajoute la nouvelle ligne dans le tableau
                treeview.insert("", "end", text=champ_compte_window_modifier.get(), values=(liste_type_modifier['selection'], champ_nom_modifier.get().upper(),
                                champ_prenom_modifier.get().capitalize(), liste_ouverture_statut_modifier['selection'], champ_ouverture_date_modifier.get(),
                                liste_fermeture_statut_modifier['selection'], champ_fermeture_date_modifier.get(), liste_direction_modifier['selection'],
                                liste_service_modifier['selection'], champ_srv_gespla_modifier.get(), liste_responsable_hierarchique_modifier['selection'],
                                liste_man_modifier['selection'], champ_fonction_modifier.get().capitalize(), Outlook_modifier.get(), acces_internet_modifier.get(),
                                vpn_modifier.get(), sap_modifier.get(), champ_code_sap_modifier.get(), perif_modifier.get(), pc_old_modifier.get(),
                                champ_commentaire_modifier.get().capitalize(), champ_statut_modifier.get().capitalize(), champ_statut_modif_modifier.get().capitalize(),
                                champ_compte_oracle_modifier.get(), champ_groupe_gnao_modifier.get(), champ_sect_xna_modifier.get()))

                """modifie les valeurs du tuple selectionné dans la table sqlServer"""

                #on supprime la ligne sélectionnée
                treeview.delete(ligne_selectionnee)
                #on ferme la fenêtre fenetre_modifier
                fenetre_modifier.destroy()
                #on réactive tous les boutons de la fenetre_principale
                bouton_chercher.config(state=NORMAL)
                bouton_modifier.config(state=NORMAL)
                bouton_inserer.config(state=NORMAL)
                bouton_quitter.config(state=NORMAL)
            else:
                #on affiche un message d'erreur
                fenetre_erreur_date = tix.Toplevel()
                fenetre_erreur_date.title("Erreur")
                erreur = Label(fenetre_erreur_date, text = "La date doit être au format JJ/MM/AAAA ou nul", bg="grey", fg="blue", font=("liberation serif", 12))
                erreur.pack()
                bouton_ok = Button(fenetre_erreur_date, text="OK", command=lambda:fenetre_erreur_date.destroy(), bg="grey")
                bouton_ok.pack()
                fenetre_erreur_date.configure(background="grey")

        else:
            #on affiche un message d'erreur
            fenetre_erreur_champs_vide = tix.Toplevel()
            fenetre_erreur_champs_vide.title("Erreur")
            erreur = Label(fenetre_erreur_champs_vide, text = "Les champs Cpte windows, Type, Nom, Prénom, Ouverture St, Ouverture date et Fermeture St doivent être remplis", bg="grey", fg="blue", font=("liberation serif", 12))
            erreur.pack()
            bouton_ok = Button(fenetre_erreur_champs_vide, text="OK", command=lambda:fenetre_erreur_champs_vide.destroy(), bg="grey")
            bouton_ok.pack()
            fenetre_erreur_champs_vide.configure(background="grey")


    #on désactive les boutons de la fenetre_principale pour éviter les problèmes
    bouton_chercher.config(state=DISABLED)
    bouton_modifier.config(state=DISABLED)
    bouton_inserer.config(state=DISABLED)
    bouton_quitter.config(state=DISABLED)

    #on vérifie qu'une ligne à était selectionnée
    try:
        #on récupère la ligne sélectionnée par l'utilisateur
        ligne_selectionnee = treeview.selection()[0]

    except:
        #on affiche un message d'erreur
        messagebox.showerror("Erreur", "Vous devez selectionner une ligne à modifier")

        #on réactive tous les boutons de la fenetre_principale
        bouton_chercher.config(state=NORMAL)
        bouton_modifier.config(state=NORMAL)
        bouton_inserer.config(state=NORMAL)
        bouton_quitter.config(state=NORMAL)

    #on récupère les valeurs de la ligne sélectionnée dans le dictionnaire valeurs
    valeurs = treeview.item(ligne_selectionnee)

    #on crée une fenêtre pour insérer un nouveau tuple
    fenetre_modifier = tix.Toplevel()
    fenetre_modifier.title("Insertion")

    #on crée un bouton de confirmation et un bouton d'annulation
    bouton_enregistrer_modifier = Button(fenetre_modifier, text="Enregistrer", command=lambda:modifierBD(), font=("liberation serif", 12))
    bouton_annuler_modifier = Button(fenetre_modifier, text="Annuler", command=lambda:annulerModification(), font=("liberation serif", 12))

    #on crée un canvas pour contenir les champs à modifier
    canvas_modifier = Canvas(fenetre_modifier, width=100, height=100, bg="grey")

    #on crée les textes à afficher au dessus des champs à compléter
    texte_compte_window_modifier = Label(canvas_modifier, text="Cpte window", bg="grey", font=("liberation serif", 12))
    texte_type_modifier = Label(canvas_modifier, text="Type", bg="grey", font=("liberation serif", 12))
    texte_nom_modifier = Label(canvas_modifier, text="Nom", bg="grey", font=("liberation serif", 12))
    texte_prenom_modifier = Label(canvas_modifier, text="Prénom", bg="grey", font=("liberation serif", 12))
    texte_ouverture_statut_modifier = Label(canvas_modifier, text="Ouverture St", bg="grey", font=("liberation serif", 12))
    texte_ouverture_date_modifier = Label(canvas_modifier, text="Ouverture Date", bg="grey", font=("liberation serif", 12))
    texte_fermeture_statut_modifier = Label(canvas_modifier, text="Fermeture St", bg="grey", font=("liberation serif", 12))
    texte_fermeture_date_modifier = Label(canvas_modifier, text="Fermeture Date", bg="grey", font=("liberation serif", 12))
    texte_direction_modifier = Label(canvas_modifier, text="Direction", bg="grey", font=("liberation serif", 12))
    texte_service_modifier = Label(canvas_modifier, text="Service", bg="grey", font=("liberation serif", 12))
    taxte_srv_gespla_modifier = Label(canvas_modifier, text="Srv Gespla", bg="grey", font=("liberation serif", 12))
    texte_responsable_hierarchique_modifier = Label(canvas_modifier, text="Resp. Hiérar.", bg="grey", font=("liberation serif", 12))
    texte_man_modifier = Label(canvas_modifier, text="Man.", bg="grey", font=("liberation serif", 12))
    texte_fonction_modifier = Label(canvas_modifier, text="Fonction", bg="grey", font=("liberation serif", 12))
    texte_outlook_modifier = Label(canvas_modifier, text="Outlook", bg="grey", font=("liberation serif", 12))
    texte_acces_internet_modifier = Label(canvas_modifier, text="Accès Internet", bg="grey", font=("liberation serif", 12))
    texte_vpn_modifier = Label(canvas_modifier, text="VPN", bg="grey", font=("liberation serif", 12))
    texte_sap_modifier = Label(canvas_modifier, text="SAP", bg="grey", font=("liberation serif", 12))
    texte_code_sap_modifier = Label(canvas_modifier, text="code SAP", bg="grey", font=("liberation serif", 12))
    texte_perif_modifier = Label(canvas_modifier, text="Périf", bg="grey", font=("liberation serif", 12))
    texte_pc_old_modifier = Label(canvas_modifier, text="PC Old", bg="grey", font=("liberation serif", 12))
    texte_commentaire_modifier = Label(canvas_modifier, text="Commentaire", bg="grey", font=("liberation serif", 12))
    texte_statut_modifier = Label(canvas_modifier, text="Statut", bg="grey", font=("liberation serif", 12))
    texte_statut_modif_modifer = Label(canvas_modifier, text="Statut modif", bg="grey", font=("liberation serif", 12))
    texte_compte_oracle_modifier = Label(canvas_modifier, text="Cpte Oracle", bg="grey", font=("liberation serif", 12))
    texte_groupe_gnao_modifier = Label(canvas_modifier, text="Grp Gnoa", bg="grey", font=("liberation serif", 12))
    texte_sect_xna_modifier = Label(canvas_modifier, text="Sect Xnn", bg="grey", font=("liberation serif", 12))

    #on crée les zones de texte à compléter
    champ_compte_window_modifier = Entry(canvas_modifier, width=20)
    champ_nom_modifier = Entry(canvas_modifier, width=20)
    champ_prenom_modifier = Entry(canvas_modifier, width=20)
    champ_ouverture_date_modifier = Entry(canvas_modifier, width=20)
    champ_fermeture_date_modifier = Entry(canvas_modifier, width=20)
    champ_srv_gespla_modifier = Entry(canvas_modifier, width=20)
    champ_fonction_modifier = Entry(canvas_modifier, width=20)
    champ_code_sap_modifier = Entry(canvas_modifier, width=20)
    champ_commentaire_modifier = Entry(canvas_modifier, width=20)
    champ_compte_oracle_modifier = Entry(canvas_modifier, width=20)
    champ_groupe_gnao_modifier = Entry(canvas_modifier, width=20)
    champ_sect_xna_modifier = Entry(canvas_modifier, width=20)
    champ_statut_modifier = Entry(canvas_modifier, width=20)
    champ_statut_modif_modifier = Entry(canvas_modifier, width=20)

    #on affiche les valeurs de la ligne sélectionnée dans les champs
    champ_compte_window_modifier.insert(END, valeurs['text'])
    champ_nom_modifier.insert(END, valeurs['values'][1])
    champ_prenom_modifier.insert(END, valeurs['values'][2])
    champ_ouverture_date_modifier.insert(END, valeurs['values'][4])
    champ_fermeture_date_modifier.insert(END, valeurs['values'][6])
    champ_srv_gespla_modifier.insert(END, valeurs['values'][9])
    champ_fonction_modifier.insert(END, valeurs['values'][12])
    champ_code_sap_modifier.insert(END, valeurs['values'][17])
    champ_commentaire_modifier.insert(END, valeurs['values'][20])
    champ_compte_oracle_modifier.insert(END, valeurs['values'][21])
    champ_groupe_gnao_modifier.insert(END, valeurs['values'][22])
    champ_sect_xna_modifier.insert(END, valeurs['values'][23])
    champ_statut_modifier.insert(END, valeurs['values'][24])
    champ_statut_modif_modifier.insert(END, valeurs['values'][25])

    #on récupère la valeur des Checkbutton
    global Outlook_modifier
    global acces_internet_modifier
    global vpn_modifier
    global sap_modifier
    global perif_modifier
    global pc_old_modifier

    Outlook_modifier = StringVar()
    acces_internet_modifier = StringVar()
    vpn_modifier = StringVar()
    sap_modifier = StringVar()
    perif_modifier = StringVar()
    pc_old_modifier = StringVar()

    #on crée les cases à cocher en récupérant les valeurs de la ligne selectionnée
    case_outlook_modifier = Checkbutton(canvas_modifier, variable=Outlook_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][13] == "Oui":
        case_outlook_modifier.select()
    else:
        case_outlook_modifier.deselect()
    case_acces_internet_modifier = Checkbutton(canvas_modifier, variable=acces_internet_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][14] == "Oui":
        case_acces_internet_modifier.select()
    else:
        case_acces_internet_modifier.deselect()
    case_vpn_modifier = Checkbutton(canvas_modifier, variable=vpn_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][15] == "Oui":
        case_vpn_modifier.select()
    else:
        case_vpn_modifier.deselect()
    case_sap_modifier = Checkbutton(canvas_modifier, variable=sap_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][16] == "Oui":
        case_sap_modifier.select()
    else:
        case_sap_modifier.deselect()
    case_perif_modifier = Checkbutton(canvas_modifier, variable=perif_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][18] == "Oui":
        case_perif_modifier.select()
    else:
        case_perif_modifier.deselect()
    case_pc_old_modifier = Checkbutton(canvas_modifier, variable=pc_old_modifier, offvalue="Non", onvalue="Oui")
    if valeurs['values'][19] == "Oui":
        case_pc_old_modifier.select()
    else:
        case_pc_old_modifier.deselect()

    #on crée les listes déroulantes  en récupérant les valeurs de la ligne selectionnée
    liste_type_modifier = tix.ComboBox(canvas_modifier)
    liste_type_modifier.configure(value=valeurs['values'][0])
    liste_ouverture_statut_modifier = tix.ComboBox(canvas_modifier)
    liste_ouverture_statut_modifier.configure(value=valeurs['values'][3])
    liste_fermeture_statut_modifier = tix.ComboBox(canvas_modifier)
    liste_fermeture_statut_modifier.configure(value=valeurs['values'][5])
    liste_direction_modifier = tix.ComboBox(canvas_modifier)
    liste_direction_modifier.configure(value=valeurs['values'][7])
    liste_service_modifier = tix.ComboBox(canvas_modifier)
    liste_service_modifier.configure(value=valeurs['values'][8])
    liste_responsable_hierarchique_modifier = tix.ComboBox(canvas_modifier)
    liste_responsable_hierarchique_modifier.configure(value=valeurs['values'][10])
    liste_man_modifier = tix.ComboBox(canvas_modifier)
    liste_man_modifier.configure(value=valeurs['values'][11])

    #on rempli les listes déroulantes
    liste_type_modifier.insert(1, "AGE")
    liste_type_modifier.insert(2, "STG (Stagiaire)")
    liste_type_modifier.insert(3, "ADM (Compte administrateur)")
    liste_type_modifier.insert(4, "USR (Utilisateur domaine FR_PAPER)")
    liste_type_modifier.insert(5, "EXT (Utilisateur hors domaine)")
    liste_type_modifier.insert(6, "GEN (Compte générique)")

    liste_ouverture_statut_modifier.insert(1, "Ouvert")
    liste_ouverture_statut_modifier.insert(2, "Pas encore ouvert")

    liste_fermeture_statut_modifier.insert(1, "Fermé")
    liste_fermeture_statut_modifier.insert(2, "Pas encore fermé")

    #on affiche le canvas
    canvas_modifier.pack(expand="True", fill="both")

    #on affiche les titres des champs
    texte_compte_window_modifier.grid(row=0, column=1)
    texte_type_modifier.grid(row=0, column=2)
    texte_nom_modifier.grid(row=0, column=3)
    texte_prenom_modifier.grid(row=0, column=4)
    texte_ouverture_statut_modifier.grid(row=0, column=5)
    texte_ouverture_date_modifier.grid(row=0, column=6)
    texte_fermeture_statut_modifier.grid(row=0, column=7)
    texte_fermeture_date_modifier.grid(row=0, column=8)
    texte_direction_modifier.grid(row=2, column=1)
    texte_service_modifier.grid(row=2, column=2)
    taxte_srv_gespla_modifier.grid(row=2, column=3)
    texte_responsable_hierarchique_modifier.grid(row=2, column=4)
    texte_man_modifier.grid(row=2, column=5)
    texte_fonction_modifier.grid(row=2, column=6)
    texte_outlook_modifier.grid(row=2, column=7)
    texte_acces_internet_modifier.grid(row=2, column=8)
    texte_vpn_modifier.grid(row=4, column=1)
    texte_sap_modifier.grid(row=4, column=2)
    texte_code_sap_modifier.grid(row=4, column=3)
    texte_perif_modifier.grid(row=4, column=4)
    texte_pc_old_modifier.grid(row=4, column=5)
    texte_commentaire_modifier.grid(row=4, column=6)
    texte_statut_modifier.grid(row=4, column=7)
    texte_statut_modif_modifer.grid(row=4, column=8)
    texte_compte_oracle_modifier.grid(row=6, column=1)
    texte_groupe_gnao_modifier.grid(row=6, column=2)
    texte_sect_xna_modifier.grid(row=6, column=3)

    #on affiche les champs à completer
    champ_compte_window_modifier.grid(row=1, column=1, padx=5)
    liste_type_modifier.grid(row=1, column=2, padx=5)
    champ_nom_modifier.grid(row=1, column=3, padx=5)
    champ_prenom_modifier.grid(row=1, column=4, padx=5)
    liste_ouverture_statut_modifier.grid(row=1, column=5, padx=5)
    champ_ouverture_date_modifier.grid(row=1, column=6, padx=5)
    liste_fermeture_statut_modifier.grid(row=1, column=7, padx=5)
    champ_fermeture_date_modifier.grid(row=1, column=8, padx=5)
    liste_direction_modifier.grid(row=3, column=1, padx=5)
    liste_service_modifier.grid(row=3, column=2, padx=5)
    champ_srv_gespla_modifier.grid(row=3, column=3, padx=5)
    liste_responsable_hierarchique_modifier.grid(row=3, column=4, padx=5)
    liste_man_modifier.grid(row=3, column=5, padx=5)
    champ_fonction_modifier.grid(row=3, column=6, padx=5)
    case_outlook_modifier.grid(row=3, column=7, padx=5)
    case_acces_internet_modifier.grid(row=3, column=8, padx=5)
    case_vpn_modifier.grid(row=5, column=1, padx=5)
    case_sap_modifier.grid(row=5, column=2, padx=5)
    champ_code_sap_modifier.grid(row=5, column=3, padx=5)
    case_perif_modifier.grid(row=5, column=4, padx=5)
    case_pc_old_modifier.grid(row=5, column=5, padx=5)
    champ_commentaire_modifier.grid(row=5, column=6, padx=5)
    champ_statut_modifier.grid(row=5, column=7, padx=5)
    champ_statut_modif_modifier.grid(row=5, column=8, padx=5)
    champ_compte_oracle_modifier.grid(row=7, column=1, padx=5)
    champ_groupe_gnao_modifier.grid(row=7, column=2, padx=5)
    champ_sect_xna_modifier.grid(row=7, column=3, padx=5)

    #on affiche les boutons
    bouton_enregistrer_modifier.pack(side="left", anchor="nw")
    bouton_annuler_modifier.pack(side="right", anchor="ne")

    #on colorie le background de la fenêtre en gris
    fenetre_modifier.configure(background="grey")

#cette fonction permet d'insérer une nouvelle ligne
#elle est appeler lors du clic sur le bouton inserer
def inserer():

    #cette fonction permet d'anuler l'insertion en cours
    #elle est appeler lors du clic sur le bouton annuler
    def annulerInsertion():
        #on réactive tous les boutons de la fenetre_principale
        bouton_chercher.config(state=NORMAL)
        bouton_modifier.config(state=NORMAL)
        bouton_inserer.config(state=NORMAL)
        bouton_quitter.config(state=NORMAL)

        #on ferme la fenêtre fenetre_inserer
        fenetre_inserer.destroy()

    #cette fonction permet d'ajouter dans la base de donnée la nouvelle ligne enregistrer
    #elle est appeler lors du clic sur le bouton enregistrer
    def ajouterBD():
        global Outlook_inserer
        global acces_internet_inserer
        global vpn_inserer
        global sap_inserer
        global perif_inserer
        global pc_old_inserer
        #on vérifie que tous les champs obligatoire sont remplis
        if champ_compte_window_inserer.get() != "" and liste_type_inserer['selection'] != "" and champ_nom_inserer.get() != "" and champ_prenom_inserer.get() != "" and liste_ouverture_statut_inserer['selection'] != "" and champ_ouverture_date_inserer.get() != "" and liste_fermeture_statut_inserer['selection'] != "":
        #on vérifie que la date est au bon format
            if len(champ_ouverture_date_inserer.get()) == 10 and (len(champ_fermeture_date_inserer.get()) == 10 or len(champ_fermeture_date_inserer.get()) == 0):
                #on ajoute la nouvelle ligne dans le tableau
                treeview.insert("", "end", text=champ_compte_window_inserer.get(), values=(liste_type_inserer['selection'], champ_nom_inserer.get().upper(),
                                        champ_prenom_inserer.get().capitalize(), liste_ouverture_statut_inserer['selection'], champ_ouverture_date_inserer.get(),
                                        liste_fermeture_statut_inserer['selection'], champ_fermeture_date_inserer.get(), liste_direction_inserer['selection'],
                                        liste_service_inserer['selection'], champ_srv_gespla_inserer.get(), liste_responsable_hierarchique_inserer['selection'],
                                        liste_man_inserer['selection'], champ_fonction_inserer.get().capitalize(), Outlook_inserer.get(), acces_internet_inserer.get(),
                                        vpn_inserer.get(), sap_inserer.get(), champ_code_sap_inserer.get(), perif_inserer.get(), pc_old_inserer.get(),
                                        champ_commentaire_inserer.get().capitalize(), champ_statut_inserer.get().capitalize(), champ_statut_modif_inserer.get().capitalize(),
                                        champ_compte_oracle_inserer.get(), champ_groupe_gnao_inserer.get(), champ_sect_xna_inserer.get()))

                """ajouter le tuple dans la base de données sqlServer"""

                #on ferme la fenêtre fenetre_inserer
                fenetre_inserer.destroy()
                #on réactive tous les boutons de la fenetre_principale
                bouton_chercher.config(state=NORMAL)
                bouton_modifier.config(state=NORMAL)
                bouton_inserer.config(state=NORMAL)
                bouton_quitter.config(state=NORMAL)
            else:
                #on affiche un message d'erreur
                fenetre_erreur_date = tix.Toplevel()
                fenetre_erreur_date.title("Erreur")
                erreur = Label(fenetre_erreur_date, text = "La date doit être au format JJ/MM/AAAA ou nul", bg="grey", fg="blue", font=("liberation serif", 12))
                erreur.pack()
                bouton_ok = Button(fenetre_erreur_date, text="OK", command=lambda:fenetre_erreur_date.destroy(), bg="grey")
                bouton_ok.pack()
                fenetre_erreur_date.configure(background="grey")
        else:
            #on affiche un message d'erreur
            fenetre_erreur_champs_vide = tix.Toplevel()
            fenetre_erreur_champs_vide.title("Erreur")
            texte_erreur = Label(fenetre_erreur_champs_vide, text = "Les champs Cpte windows, Type, Nom, Prénom, Ouverture St, Ouverture date et Fermeture St doivent être remplis", bg="grey", fg="blue", font=("liberation serif", 12))
            texte_erreur.pack()
            bouton_ok = Button(fenetre_erreur_champs_vide, text="OK", command=lambda:fenetre_erreur_champs_vide.destroy(), bg="grey")
            bouton_ok.pack()
            fenetre_erreur_champs_vide.configure(background="grey")

    #on désactive les boutons de la fenetre_principale pour éviter les problèmes
    bouton_chercher.config(state=DISABLED)
    bouton_modifier.config(state=DISABLED)
    bouton_inserer.config(state=DISABLED)
    bouton_quitter.config(state=DISABLED)

    #on crée une fenêtre pour insérer un nouveau tuple
    fenetre_inserer = tix.Toplevel()
    fenetre_inserer.title("Insertion")

    #on crée un bouton de confirmation et un bouton d'annulation
    bouton_enregistrer_inserer = Button(fenetre_inserer, text="Enregistrer", command=lambda:ajouterBD(), font=("liberation serif", 12))
    bouton_annuler_inserer = Button(fenetre_inserer, text="Annuler", command=lambda:annulerInsertion(), font=("liberation serif", 12))

    #on crée un canvas pour contenir les champs à remplir
    canvas_insertion = Canvas(fenetre_inserer, width=100, height=100, bg="grey")

    #on crée les textes à afficher au dessus des champs à compléter
    texte_compte_window_inserer = Label(canvas_insertion, text="Cpte window", bg="grey", font=("liberation serif", 12))
    texte_type_inserer = Label(canvas_insertion, text="Type", bg="grey", font=("liberation serif", 12))
    texte_nom_inserer = Label(canvas_insertion, text="Nom", bg="grey", font=("liberation serif", 12))
    texte_prenom_inserer = Label(canvas_insertion, text="Prénom", bg="grey", font=("liberation serif", 12))
    texte_ouverture_statut_inserer = Label(canvas_insertion, text="Ouverture St", bg="grey", font=("liberation serif", 12))
    texte_ouverture_date_inserer = Label(canvas_insertion, text="Ouverture Date", bg="grey", font=("liberation serif", 12))
    texte_fermeture_statut_inserer = Label(canvas_insertion, text="Fermeture St", bg="grey", font=("liberation serif", 12))
    texte_fermeture_date_inserer = Label(canvas_insertion, text="Fermeture Date", bg="grey", font=("liberation serif", 12))
    texte_direction_inserer = Label(canvas_insertion, text="Direction", bg="grey", font=("liberation serif", 12))
    texte_service_inserer = Label(canvas_insertion, text="Service", bg="grey", font=("liberation serif", 12))
    taxte_srv_gespla_inserer = Label(canvas_insertion, text="Srv Gespla", bg="grey", font=("liberation serif", 12))
    texte_responsable_hierarchique_inserer = Label(canvas_insertion, text="Resp. Hiérar.", bg="grey", font=("liberation serif", 12))
    texte_man_inserer = Label(canvas_insertion, text="Man.", bg="grey", font=("liberation serif", 12))
    texte_fonction_inserer = Label(canvas_insertion, text="Fonction", bg="grey", font=("liberation serif", 12))
    texte_outlook_inserer = Label(canvas_insertion, text="Outlook", bg="grey", font=("liberation serif", 12))
    texte_acces_internet_inserer = Label(canvas_insertion, text="Accès Internet", bg="grey", font=("liberation serif", 12))
    texte_vpn_inserer = Label(canvas_insertion, text="VPN", bg="grey", font=("liberation serif", 12))
    texte_sap_inserer = Label(canvas_insertion, text="SAP", bg="grey", font=("liberation serif", 12))
    texte_code_sap_inserer = Label(canvas_insertion, text="code SAP", bg="grey", font=("liberation serif", 12))
    texte_perif_inserer = Label(canvas_insertion, text="Périf", bg="grey", font=("liberation serif", 12))
    texte_pc_old_inserer = Label(canvas_insertion, text="PC Old", bg="grey", font=("liberation serif", 12))
    texte_commentaire_inserer = Label(canvas_insertion, text="Commentaire", bg="grey", font=("liberation serif", 12))
    texte_statut_inserer = Label(canvas_insertion, text="Statut", bg="grey", font=("liberation serif", 12))
    texte_statut_modif_inserer = Label(canvas_insertion, text="Statut modif", bg="grey", font=("liberation serif", 12))
    texte_compte_oracle_inserer = Label(canvas_insertion, text="Cpte Oracle", bg="grey", font=("liberation serif", 12))
    texte_groupe_gnao_inserer = Label(canvas_insertion, text="Grp Gnoa", bg="grey", font=("liberation serif", 12))
    texte_sect_xna_inserer = Label(canvas_insertion, text="Sect Xnn", bg="grey", font=("liberation serif", 12))

    #on crée les zones à compléter
    champ_compte_window_inserer = Entry(canvas_insertion, width=20)
    champ_nom_inserer = Entry(canvas_insertion, width=20)
    champ_prenom_inserer = Entry(canvas_insertion, width=20)
    champ_ouverture_date_inserer = Entry(canvas_insertion, width=20)
    champ_fermeture_date_inserer = Entry(canvas_insertion, width=20)
    champ_srv_gespla_inserer = Entry(canvas_insertion, width=20)
    champ_fonction_inserer = Entry(canvas_insertion, width=20)
    champ_code_sap_inserer = Entry(canvas_insertion, width=20)
    champ_commentaire_inserer = Entry(canvas_insertion, width=20)
    champ_compte_oracle_inserer = Entry(canvas_insertion, width=20)
    champ_groupe_gnao_inserer = Entry(canvas_insertion, width=20)
    champ_sect_xna_inserer = Entry(canvas_insertion, width=20)
    champ_statut_inserer = Entry(canvas_insertion, width=20)
    champ_statut_modif_inserer = Entry(canvas_insertion, width=20)

    #on récupère la valeur des Checkbutton
    global Outlook_inserer
    global acces_internet_inserer
    global vpn_inserer
    global sap_inserer
    global perif_inserer
    global pc_old_inserer

    Outlook_inserer = StringVar()
    acces_internet_inserer = StringVar()
    vpn_inserer = StringVar()
    sap_inserer = StringVar()
    perif_inserer = StringVar()
    pc_old_inserer = StringVar()

    #on crée les cases à cocher décoché de base
    case_outlook_inserer = Checkbutton(canvas_insertion, variable=Outlook_inserer, offvalue="Non", onvalue="Oui")
    case_outlook_inserer.deselect()
    case_acces_internet_inserer = Checkbutton(canvas_insertion, variable=acces_internet_inserer, offvalue="Non", onvalue="Oui")
    case_acces_internet_inserer.deselect()
    case_vpn_inserer = Checkbutton(canvas_insertion, variable=vpn_inserer, offvalue="Non", onvalue="Oui")
    case_vpn_inserer.deselect()
    case_sap_inserer = Checkbutton(canvas_insertion, variable=sap_inserer, offvalue="Non", onvalue="Oui")
    case_sap_inserer.deselect()
    case_perif_inserer = Checkbutton(canvas_insertion, variable=perif_inserer, offvalue="Non", onvalue="Oui")
    case_perif_inserer.deselect()
    case_pc_old_inserer = Checkbutton(canvas_insertion, variable=pc_old_inserer, offvalue="Non", onvalue="Oui")
    case_pc_old_inserer.deselect()

    #on crée les listes déroulantes
    liste_type_inserer = tix.ComboBox(canvas_insertion)
    liste_ouverture_statut_inserer = tix.ComboBox(canvas_insertion)
    liste_fermeture_statut_inserer = tix.ComboBox(canvas_insertion)
    liste_direction_inserer = tix.ComboBox(canvas_insertion)
    liste_service_inserer = tix.ComboBox(canvas_insertion)
    liste_responsable_hierarchique_inserer = tix.ComboBox(canvas_insertion)
    liste_man_inserer = tix.ComboBox(canvas_insertion)

    #on rempli les listes déroulantes
    liste_type_inserer.insert(1, "AGE")
    liste_type_inserer.insert(2, "STG (Stagiaire)")
    liste_type_inserer.insert(3, "ADM (Compte administrateur)")
    liste_type_inserer.insert(4, "USR (Utilisateur domaine FR_PAPER)")
    liste_type_inserer.insert(5, "EXT (Utilisateur hors domaine)")
    liste_type_inserer.insert(6, "GEN (Compte générique)")


    liste_ouverture_statut_inserer.insert(1, "Ouvert")
    liste_ouverture_statut_inserer.insert(2, "Pas encore ouvert")

    liste_fermeture_statut_inserer.insert(1, "Fermé")
    liste_fermeture_statut_inserer.insert(2, "Pas encore fermé")

    #on affiche le canvas
    canvas_insertion.pack(expand="True", fill="both")

    #on affiche les titres des champs
    texte_compte_window_inserer.grid(row=0, column=1)
    texte_type_inserer.grid(row=0, column=2)
    texte_nom_inserer.grid(row=0, column=3)
    texte_prenom_inserer.grid(row=0, column=4)
    texte_ouverture_statut_inserer.grid(row=0, column=5)
    texte_ouverture_date_inserer.grid(row=0, column=6)
    texte_fermeture_statut_inserer.grid(row=0, column=7)
    texte_fermeture_date_inserer.grid(row=0, column=8)
    texte_direction_inserer.grid(row=2, column=1)
    texte_service_inserer.grid(row=2, column=2)
    taxte_srv_gespla_inserer.grid(row=2, column=3)
    texte_responsable_hierarchique_inserer.grid(row=2, column=4)
    texte_man_inserer.grid(row=2, column=5)
    texte_fonction_inserer.grid(row=2, column=6)
    texte_outlook_inserer.grid(row=2, column=7)
    texte_acces_internet_inserer.grid(row=2, column=8)
    texte_vpn_inserer.grid(row=4, column=1)
    texte_sap_inserer.grid(row=4, column=2)
    texte_code_sap_inserer.grid(row=4, column=3)
    texte_perif_inserer.grid(row=4, column=4)
    texte_pc_old_inserer.grid(row=4, column=5)
    texte_commentaire_inserer.grid(row=4, column=6)
    texte_statut_inserer.grid(row=4, column=7)
    texte_statut_modif_inserer.grid(row=4, column=8)
    texte_compte_oracle_inserer.grid(row=6, column=1)
    texte_groupe_gnao_inserer.grid(row=6, column=2)
    texte_sect_xna_inserer.grid(row=6, column=3)

    #on affiche les champs à completer
    champ_compte_window_inserer.grid(row=1, column=1, padx=5)
    liste_type_inserer.grid(row=1, column=2, padx=5)
    champ_nom_inserer.grid(row=1, column=3, padx=5)
    champ_prenom_inserer.grid(row=1, column=4, padx=5)
    liste_ouverture_statut_inserer.grid(row=1, column=5, padx=5)
    champ_ouverture_date_inserer.grid(row=1, column=6, padx=5)
    liste_fermeture_statut_inserer.grid(row=1, column=7, padx=5)
    champ_fermeture_date_inserer.grid(row=1, column=8, padx=5)
    liste_direction_inserer.grid(row=3, column=1, padx=5)
    liste_service_inserer.grid(row=3, column=2, padx=5)
    champ_srv_gespla_inserer.grid(row=3, column=3, padx=5)
    liste_responsable_hierarchique_inserer.grid(row=3, column=4, padx=5)
    liste_man_inserer.grid(row=3, column=5, padx=5)
    champ_fonction_inserer.grid(row=3, column=6, padx=5)
    case_outlook_inserer.grid(row=3, column=7, padx=5)
    case_acces_internet_inserer.grid(row=3, column=8, padx=5)
    case_vpn_inserer.grid(row=5, column=1, padx=5)
    case_sap_inserer.grid(row=5, column=2, padx=5)
    champ_code_sap_inserer.grid(row=5, column=3, padx=5)
    case_perif_inserer.grid(row=5, column=4, padx=5)
    case_pc_old_inserer.grid(row=5, column=5, padx=5)
    champ_commentaire_inserer.grid(row=5, column=6, padx=5)
    champ_statut_inserer.grid(row=5, column=7, padx=5)
    champ_statut_modif_inserer.grid(row=5, column=8, padx=5)
    champ_compte_oracle_inserer.grid(row=7, column=1, padx=5)
    champ_groupe_gnao_inserer.grid(row=7, column=2, padx=5)
    champ_sect_xna_inserer.grid(row=7, column=3, padx=5)

    #on affiche les boutons
    bouton_enregistrer_inserer.pack(side="left", anchor="nw")
    bouton_annuler_inserer.pack(side="right", anchor="ne")

    #on colorie le background de la fenêtre en gris
    fenetre_inserer.configure(background="grey")

#cette fonction à pour but de fermer et détruire la fenetre_principale lors de la confirmation de fermeture
def toutFermer():

    """se déconnecter de la table sqlServer"""

    #on ferme la fenêtre fenetre_principale
    fenetre_principale.quit()
    #on détruit la fenêtre fenetre_principale
    fenetre_principale.destroy()

#cette fonction permet de quitter l'application
def quitter():

    #cette fonction sert à rendre les bouttons de la fenêtre principal fonctionnel lorque l'on annule la fermeture de la page
    def annulerQuitter():
        #on détruit la fenêtre fenetre_quitter
        fenetre_quitter.destroy()
        #on réactive tous les boutons de la fenetre_principale
        bouton_chercher.config(state=NORMAL)
        bouton_modifier.config(state=NORMAL)
        bouton_inserer.config(state=NORMAL)
        bouton_quitter.config(state=NORMAL)

    #on désactive les boutons de la fenetre_principale pour éviter les problèmes
    bouton_chercher.config(state=DISABLED)
    bouton_modifier.config(state=DISABLED)
    bouton_inserer.config(state=DISABLED)
    bouton_quitter.config(state=DISABLED)

    #on crée une fenêtre de confirmation avant de quitter
    fenetre_quitter = Toplevel()
    fenetre_quitter.title("Confirmation de fermeture")

    #on demande à l'utilisateur confirmation de quitter l'application
    texte_confirmation = Label(fenetre_quitter, text="Etes-vous sûr de vouloir quitter USERSKCP ?", bg="grey", font=("liberation serif", 12))

    #on crée un bouton de confirmation et un bouton d'annulation
    bouton_confirmer = Button(fenetre_quitter, text="Confirmer", command=lambda:toutFermer(), font=("liberation serif", 12))
    bouton_annuler_quitter = Button(fenetre_quitter, text="Annuler", command=lambda:annulerQuitter(), font=("liberation serif", 12))

    #on affiche tous les widgets
    texte_confirmation.grid(row=0, column=2, padx=10, pady=5)
    bouton_confirmer.grid(row=1, column=1, padx=10, pady=5)
    bouton_annuler_quitter.grid(row=1, column=3, padx=10, pady=5)

    #on colorie le background de la fenêtre en bleu
    fenetre_quitter.configure(background="grey")

"""---déclaration des variables---"""
#on crée la fenêtre principale
fenetre_principale = tix.Tk()
#on donne un titre à cette fenêtre
fenetre_principale.title("USERSKCP")

#on crée une variable date qui récupère la date et l'heure actuelle
date = datetime.datetime.now()
#on met toute la phrase dans une variable date_complete pour l'afficher dans le label
date_complete = "Le:", date.strftime("%d/%m/%Y"), "à:", date.strftime("%H:%M")

"""se connecter à la base sqlServer"""

#on crée les textes à afficher en entête
texte_userskcp = Label(fenetre_principale, text="USERSKCP", bg="grey", font=("liberation serif", 12))
texte_smurfit = Label(fenetre_principale, text="SMURFIT-Cellulose du Pin", bg="grey", font=("liberation serif", 12))
texte_date_heure = Label(fenetre_principale, text=date_complete, bg="grey", font=("liberation serif", 12))
texte_titre = Label(fenetre_principale, text="Gestion des utilisateurs", bg="grey", font=("liberation serif", 12))
texte_informatique = Label(fenetre_principale, text="INFORMATIQUE", bg="grey", font=("liberation serif", 12))

#on crée un canvas pour séparé l'entête du reste de la fenêtre
canvas_ligne = Canvas(fenetre_principale, width=1250, height=5, bg="grey")

#on crée les textes à afficher au dessus des champs à compléter
texte_compte_window = Label(fenetre_principale, text="Compte Window", bg="grey", font=("liberation serif", 12))
texte_nom = Label(fenetre_principale, text="Nom", bg="grey", font=("liberation serif", 12))
texte_direction = Label(fenetre_principale, text="Direction", bg="grey", font=("liberation serif", 12))
texte_service = Label(fenetre_principale, text="Service", bg="grey", font=("liberation serif", 12))
texte_responsable_hierarchique = Label(fenetre_principale, text="Responsable hiérarchique", bg="grey", font=("liberation serif", 12))
texte_statut_compte = Label(fenetre_principale, text="Statut du compte", bg="grey", font=("liberation serif", 12))

#on crée les champs à compléter pour la recherche
champ_compte_window = Entry(fenetre_principale, textvariable=str, width=20)
champ_nom = Entry(fenetre_principale, textvariable=str, width=20)

#on crée les listes déroulantes pour les champs direction, service et responsable hiérarchique
liste_direction = tix.ComboBox(fenetre_principale)
liste_service = tix.ComboBox(fenetre_principale)
liste_responsable_hierarchique = tix.ComboBox(fenetre_principale)
liste_statut_compte = tix.ComboBox(fenetre_principale)

#on rempli la liste de statut du compte
liste_statut_compte.insert(1, "Ouvert")
liste_statut_compte.insert(2, "Fermé")
liste_statut_compte.insert(3, "Tous")

#on crée un canvas pour l'ensemble du treeview avec les scrollBar
canvas_centre = Canvas(fenetre_principale, width=1200, height=450, bg="grey")

#on crée un canvas pour le treeview
canvas_tableau = Canvas(canvas_centre, width=100, height=450, bg="grey")

#on crée les deux scrollbar pour naviguer dans le treeview
scrollbar_horizontal = Scrollbar(canvas_centre, orient=HORIZONTAL)
scrollbar_vertical = Scrollbar(canvas_centre, orient=VERTICAL)

#on crée les boutons
bouton_chercher = Button(fenetre_principale, text="Chercher", command=lambda:recherche(), font=("liberation serif", 12))
bouton_inserer = Button(fenetre_principale, text="Insérer", command=lambda:inserer(), font=("liberation serif", 12))
bouton_modifier = Button(fenetre_principale, text="Modifier", command=lambda:modifier(), font=("liberation serif", 12))
bouton_quitter = Button(fenetre_principale, text="Quitter", command=lambda:quitter(), font=("liberation serif", 12))

#personnalisation de l'entête du treeview
style = ttk.Style()
style.configure("treeview.Treeview.Heading", font=("liberation serif", 12), foreground="blue")
style.configure("treeview.Treeview", font=("liberation serif", 12))

#création du treeview
treeview = ttk.Treeview(canvas_tableau, style="treeview.Treeview")

#on configure la navigation avec scrollBar
treeview.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

#on configure les scrollbar
scrollbar_vertical.configure(command=treeview.yview)
scrollbar_horizontal.configure(command=treeview.xview)

"""---placement des différents éléments---"""
#placement des textes dans l'entête de l'application
texte_userskcp.grid(row=0, column=1, padx=10, pady=5)
texte_smurfit.grid(row=0, column=3, padx=10, pady=5)
texte_date_heure.grid(row=0, column=6, padx=10, pady=5)
texte_titre.grid(row=1, column=1, padx=10, pady=10)
texte_informatique.grid(row=1, column=6, padx=10, pady=10)

#placement du canvas_ligne de façon à ce qu'il occupe toute la largeur de la fenêtre
canvas_ligne.grid(row=2, column=0, columnspan=8, padx=10, pady=5)

#trace des lignes avec comme paramètre les coordonnées x1, y1, x2, y2 des deux points de la ligne
canvas_ligne.create_line(0, 5, 20000, 5)
canvas_ligne.create_line(0, 4, 20000, 4)
canvas_ligne.create_line(0, 3, 20000, 3)
canvas_ligne.create_line(0, 2, 20000, 2)
canvas_ligne.create_line(0, 1, 20000, 1)

#placement des textes au dessus des champs à remplir
texte_compte_window.grid(row=3, column=1, padx=0, pady=5)
texte_nom.grid(row=3, column=2, padx=0, pady=5)
texte_direction.grid(row=3, column=3, padx=0, pady=5)
texte_service.grid(row=3, column=4, padx=0, pady=5)
texte_responsable_hierarchique.grid(row=3, column=5, padx=0, pady=5)
texte_statut_compte.grid(row=3, column=6, padx=0, pady=5)

#placement des champs à compléter
champ_compte_window.grid(row=4, column=1, padx=0, pady=5)
champ_nom.grid(row=4, column=2, padx=0, pady=5)

#placement des listes
liste_direction.grid(row=4, column=3, padx=0, pady=5)
liste_service.grid(row=4, column=4, padx=0, pady=5)
liste_responsable_hierarchique.grid(row=4, column=5, padx=0, pady=5)
liste_statut_compte.grid(row=4, column=6, padx=0, pady=5)

#placement du canvas_centre de façon à ce qu'il occupe la partie du milieu de l'écran
canvas_centre.grid(row=5, column=1, rowspan=5, columnspan=7)

#on déclare les colonnes du treeview
treeview["columns"]=("texte_tab_cpte_window", "texte_tab_type", "texte_tab_nom", "texte_tab_prenom", "texte_tab_ouverture_statut",
                            "texte_tab_ouverture_date", "texte_tab_fermeture_statut", "texte_tab_fermeture_date", "texte_tab_direction",
                            "texte_tab_service", "texte_tab_srv_gespla", "texte_tab_responsable", "texte_tab_man", "texte_tab_fonction",
                            "texte_tab_outlook", "texte_tab_acces_internet", "texte_tab_vpn", "texte_tab_sap", "texte_tab_code_sap",
                            "texte_tab_perif", "texte_tab_pc_old", "texte_tab_commentaire", "texte_tab_statut", "texte_tab_statut_modif",
                            "texte_tab_compte_oracle", "texte_tab_groupe_gnao", "texte_tab_sect_xna")

#on configure les colonnes du treeview
treeview.column("#0", width=120, stretch=False)
treeview.column("#1", width=120, stretch=False)
treeview.column("#2", width=120, stretch=False)
treeview.column("#3", width=120, stretch=False)
treeview.column("#4", width=100, stretch=False)
treeview.column("#5", width=120, stretch=False)
treeview.column("#6", width=100, stretch=False)
treeview.column("#7", width=120, stretch=False)
treeview.column("#8", width=120, stretch=False)
treeview.column("#9", width=120, stretch=False)
treeview.column("#10", width=100, stretch=False)
treeview.column("#11", width=120, stretch=False)
treeview.column("#12", width=100, stretch=False)
treeview.column("#13", width=120, stretch=False)
treeview.column("#14", width=100, stretch=False)
treeview.column("#15", width=100, stretch=False)
treeview.column("#16", width=100, stretch=False)
treeview.column("#17", width=100, stretch=False)
treeview.column("#18", width=100, stretch=False)
treeview.column("#19", width=100, stretch=False)
treeview.column("#20", width=100, stretch=False)
treeview.column("#21", width=120, stretch=False)
treeview.column("#22", width=100, stretch=False)
treeview.column("#23", width=100, stretch=False)
treeview.column("#24", width=120, stretch=False)
treeview.column("#25", width=100, stretch=False)
treeview.column("#26", width=100, stretch=False)

#on nome les colonnes du treeview
treeview.heading("#0", text="Cpte window")
treeview.heading("#1", text="Type")
treeview.heading("#2", text="Nom")
treeview.heading("#3", text="Prénom")
treeview.heading("#4", text="Ouverture St")
treeview.heading("#5", text="Ouverture Date")
treeview.heading("#6", text="Fermeture St")
treeview.heading("#7", text="Fermeture Date")
treeview.heading("#8", text="Direction")
treeview.heading("#9", text="Service")
treeview.heading("#10", text="Srv Gespla")
treeview.heading("#11", text="Resp. Hiérar.")
treeview.heading("#12", text="Man.")
treeview.heading("#13", text="Fonction")
treeview.heading("#14", text="Outlook")
treeview.heading("#15", text="Accès Internet")
treeview.heading("#16", text="VPN")
treeview.heading("#17", text="SAP")
treeview.heading("#18", text="code SAP")
treeview.heading("#19", text="Périf")
treeview.heading("#20", text="PC Old")
treeview.heading("#21", text="Commentaire")
treeview.heading("#22", text="Statut")
treeview.heading("#23", text="Statut modi")
treeview.heading("#24", text="Cpte Oracle")
treeview.heading("#25", text="Grp Gnoa")
treeview.heading("#26", text="Sect Xnn")

#placement des scrollbar
scrollbar_vertical.pack(side="left", fill=Y)
scrollbar_horizontal.pack(side="bottom", fill=X)

#placement du canvas_tableau dans canvas_centre
canvas_tableau.pack(expand="True", fill="both")

#on affiche le treeview
treeview.pack(expand="True", fill="both")

#placement des boutons
bouton_chercher.grid(row=4, column=7, padx=5, pady=5)
bouton_inserer.grid(row=10, column=1, padx=5, pady=5)
bouton_modifier.grid(row=10, column=2, padx=5, pady=5)
bouton_quitter.grid(row=10, column=3, padx=5, pady=5)

#affiche la fenetre_principale en pleine écran à l'ouverture
fenetre_principale.attributes("-fullscreen", 1)

#on colorie le background de la fenêtre en gris
fenetre_principale.configure(background="grey")

#on empêche les canvas_centre de s'aggrandir en fonction de la taille du treeview
canvas_centre.propagate(False)

#on démarre la boucle tKinter pour conserver la fenêtre ouverte
fenetre_principale.mainloop()
