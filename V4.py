#Ce programme est l'interface de l'application USERSKCDP
#date de création : 25/05/19 par : Quentin Dhersin
#dernière modification le : 27/05/19 par : Quentin Dhersin

#Ceci est la version finale de l'application se basant sur la base de données test basé sur Oracle

#la ligne ci dessous indique l'encodage utilisé, Latin1 pour windows en général
# -*-coding:Latin-1 -*

"""---Déclaration des import---"""
#import du module tkinter qui sert à la programmation graphique
from tkinter import *
#import du packtage messagebox appartenant à tkinter qui sert à afficher des fenêtres avec message
from tkinter import messagebox
#import du module datetime pour avoir la date et l'heure actuelle
import datetime
#import de ttk pour créer des treeview
import tkinter.ttk as ttk
#import du package pour se connecter à la BD
import cx_Oracle
#import du packtage tix appartenant à tkinter pour créer des listes déroulantes
from tkinter import tix
#import du module os pour utiliser la fonction getenv qui indique l'Utilisateur actuel
import os

"""déclaration des fonctions"""
#cette fonction permet d'afficher tous les tuples correspondant aux critères entré
#elle est appeler lors du clic sur le bouton chercher
def recherche():
    #on vide le treeview
    for i in treeview.get_children():
        treeview.delete(i)
    #on crée la requête
    if liste_direction['selection']=="":
        liste_direction['selection']="%"
    if liste_service['selection']=="":
        liste_service['selection']="%"
    if liste_responsable_hierarchique['selection']=="":
        liste_responsable_hierarchique['selection']="%"
    if liste_statut_compte['selection']=="Tous" or liste_statut_compte['selection']=="":
        requete = "SELECT * FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\'"
        compteur_requete = "SELECT count(*) FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\'"

    elif liste_statut_compte['selection']=="Ouvert":
        requete = "SELECT * FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\' AND STATUT_OUV LIKE \'T\' AND (STATUT_FERM LIKE \'% %\' OR STATUT_FERM IS NULL)"
        compteur_requete = "SELECT count(*) FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\' AND STATUT_OUV LIKE \'T\' AND (STATUT_FERM LIKE \'% %\' OR STATUT_FERM IS NULL)"

    elif liste_statut_compte['selection']=="Fermé":
        requete = "SELECT * FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\' AND STATUT_OUV LIKE \'T\' AND STATUT_FERM LIKE \'T\'"
        compteur_requete = "SELECT count(*) FROM user_skcdp WHERE CPTWIN LIKE \'%" + champ_compte_windows.get().upper() + "%\' AND NOM LIKE \'%" + champ_nom.get().upper() + "%\' AND DIRECTION LIKE \'" + liste_direction['selection'] + "\' AND SERVICE LIKE \'" + liste_service['selection'] + "\' AND RHIERAR LIKE \'" + liste_responsable_hierarchique['selection'] + "\' AND STATUT_OUV LIKE \'T\' AND STATUT_FERM LIKE \'T\'"
    #on lance la requête
    cursor.execute(compteur_requete)
    #on vérifie que la requete retourne au moins un résultat
    for compteur in cursor:
        if compteur[0] > 0:
	#on lance la recherche
            cursor.execute(requete)
            #on affiche les résultats dans le Treeview
            for row in cursor:
                #on modifie la forme des dates
                date_ouverture_recherche=row[10]
                if len(date_ouverture_recherche) == 8:
                    annee_ouverture_recherche=date_ouverture_recherche[:4]
                    mois_ouverture_recherche=date_ouverture_recherche[4:6]
                    jour_ouverture_recherche=date_ouverture_recherche[6:]
                    date_ouverture_recherche=jour_ouverture_recherche + '/' + mois_ouverture_recherche + '/' + annee_ouverture_recherche

                date_fermeture_recherche=row[11]
                if len(date_fermeture_recherche) == 8:
                    annee_fermeture_recherche=date_fermeture_recherche[:4]
                    mois_fermeture_recherche=date_fermeture_recherche[4:6]
                    jour_fermeture_recherche=date_fermeture_recherche[6:]
                    date_fermeture_recherche=jour_fermeture_recherche + '/' + mois_fermeture_recherche + '/' + annee_fermeture_recherche

	        #on insère les valeurs dans le treeview
                treeview.insert("", "end", text=row[0], values=(row[1], row[2],  row[3], row[13], date_ouverture_recherche, row[15], date_fermeture_recherche, row[4], row[7], row[31], row[5], row[32], row[8],
                row[16], row[17], row[18], row[20], row[22], row[19], row[30], row[23], row[9], row[14], row[27], row[29]))
        else:
            #on affiche un message si aucun résultat n'a été trouvé
            messagebox.showinfo("Vide", "Aucun résultat trouvé")

    #on reinitialise les champs pour la recherche
    champ_compte_windows.delete(0, "end")
    champ_nom.delete(0, "end")
    liste_direction['selection']=""
    liste_service['selection']=""
    liste_responsable_hierarchique['selection']=""
    liste_statut_compte['selection']=""

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
        if champ_compte_windows_modifier.get() != "" and champ_nom_modifier.get() != "":
            #on vérifie que la date est au bon format
            if (len(champ_ouverture_date_modifier.get()) == 10 or len(champ_ouverture_date_modifier.get()) == 0) and (len(champ_fermeture_date_modifier.get()) == 10 or len(champ_fermeture_date_modifier.get()) == 0):
                #on modifie la valeur de liste_ouverture_statut_modifier pour qu'elle corresponde à celle attendu dans la BD
                if liste_ouverture_statut_modifier['selection']=="Ouvert":
                    liste_ouverture_statut_modifier['selection']="T"
                if liste_ouverture_statut_modifier['selection']=="Pas encore ouvert":
                    liste_ouverture_statut_modifier['selection']=""
                if liste_fermeture_statut_modifier['selection']=="Fermé":
                    liste_fermeture_statut_modifier['selection']="T"
                if liste_fermeture_statut_modifier['selection']=="Pas encore fermé":
                    liste_fermeture_statut_modifier['selection']=""
                if liste_man_modifier['selection']=='Oui':
                    liste_man_modifier['selection']='O'
                else:
                    liste_man_modifier['selection']='N'
                #on ajoute la nouvelle ligne dans le tableau
                treeview.insert("", 0, text=champ_compte_windows_modifier.get().upper(), values=(liste_type_modifier['selection'], champ_nom_modifier.get().upper(),
                                champ_prenom_modifier.get().upper(), liste_ouverture_statut_modifier['selection'], champ_ouverture_date_modifier.get(),
                                liste_fermeture_statut_modifier['selection'], champ_fermeture_date_modifier.get(), liste_direction_modifier['selection'],
                                liste_service_modifier['selection'], champ_srv_gespla_modifier.get(), liste_responsable_hierarchique_modifier['selection'],
                                liste_man_modifier['selection'], champ_fonction_modifier.get().capitalize(), Outlook_modifier.get(), acces_internet_modifier.get(),
                                vpn_modifier.get(), sap_modifier.get(), champ_code_sap_modifier.get(), perif_modifier.get(), pc_old_modifier.get(),
                                champ_commentaire_modifier.get().capitalize(), champ_statut_modifier.get().upper(), champ_statut_modif_modifier.get().capitalize(),
                                champ_compte_oracle_modifier.get(), champ_sect_xng_modifier.get()))

                #on met la date au bon format pour la BD
                if len(champ_ouverture_date_modifier.get()) == 10:
                    date_ouverture_modifier=champ_ouverture_date_modifier.get()
                    jour_ouverture_modifier=date_ouverture_modifier[:2]
                    mois_ouverture_modifier=date_ouverture_modifier[3:5]
                    annee_ouverture_modifier=date_ouverture_modifier[6:]
                    date_ouverture_modifier=annee_ouverture_modifier+mois_ouverture_modifier+jour_ouverture_modifier
                else:
                    date_ouverture_modifier=champ_ouverture_date_modifier.get()

                if len(champ_fermeture_date_modifier.get()) == 10:
                    date_fermeture_modifier=champ_fermeture_date_modifier.get()
                    jour_fermeture_modifier=date_fermeture_modifier[:2]
                    mois_fermeture_modifier=date_fermeture_modifier[3:5]
                    annee_fermeture_modifier=date_fermeture_modifier[6:]
                    date_fermeture_modifier=annee_fermeture_modifier+mois_fermeture_modifier+jour_fermeture_modifier
                else:
                    date_fermeture_modifier=champ_fermeture_date_modifier.get()

                #on récupère l'utilisateur qui effectue les modifications
                utilisateur_modifier=os.getenv("USERNAME")
                #on récupère la date et l'heure actuelle
                date=datetime.datetime.today()
                jour_modifier=date.strftime('%Y%m%d')
                heure_modifier=date.strftime('%H%M%S')
                #on modifie le tuple dans la table
                cursor.execute("update user_skcdp set CPTWIN=\'" + champ_compte_windows_modifier.get().upper() + "\', TYPCPTE=\'" + liste_type_modifier['selection'] + "\', NOM=\'" + champ_nom_modifier.get().upper() + "\', PRENOM=\'" + champ_prenom_modifier.get().upper() + "\', DIRECTION=\'" + liste_direction_modifier['selection'] + "\', RHIERAR=\'" + liste_responsable_hierarchique_modifier['selection'] + "\', DATEDEMANDE=\' \', SERVICE=\'" + liste_service_modifier['selection'] + "\', FONCTION=\'" + champ_fonction_modifier.get().upper() + "\', STATUT_CPTE=\'" + champ_statut_modifier.get().upper() + "\', DATEOUVERT=\'" + date_ouverture_modifier + "\', DATEFERMET=\'" + date_fermeture_modifier + "\', DATEDESACT=\' \', STATUT_OUV=\'" + liste_ouverture_statut_modifier['selection'] + "\', STATUT_MOD=\'" + champ_statut_modif_modifier.get().upper() + "\', STATUT_FERM=\'" + liste_fermeture_statut_modifier['selection'] + "\', OUTLOOK=\'" + Outlook_modifier.get() + "\', INTERNET=\'" + acces_internet_modifier.get() + "\', VPN=\'" + vpn_modifier.get() + "\', ACCESPERIF=\'" + perif_modifier.get() + "\', CPTESAP=\'" + sap_modifier.get() + "\', REUTILPC=\' \', CPTE_VMS_INTER=\'" + pc_old_modifier.get() + "\', LIEUINSTAL=\'" + champ_code_sap_modifier.get().upper() + "\', COMMENTAIRE=\'" + champ_commentaire_modifier.get().capitalize() + "\', MODINAME=\'" + utilisateur_modifier + "\', MODIDATE=\'" + jour_modifier + "\', MODITIME=\'" + heure_modifier + "\', CPTEORA=\'" + champ_compte_oracle_modifier.get() + "\', GRPT_GP=\'\', SEC_CODE=\'" + champ_sect_xng_modifier.get() + "\', SRV_GESPLA=\'" + champ_srv_gespla_modifier.get() + "\', MANAGER=\'" + liste_man_modifier['selection'] + "\' where CPTWIN=\'" + valeurs['text'] + "\'")
                """---A optimiser---"""
                #on modifie tous les champs nul pour éviter les erreurs
                cursor.execute("update user_skcdp set TYPCPTE=\' \' where TYPCPTE IS NULL")
                cursor.execute("update user_skcdp set PRENOM=\' \' where PRENOM IS NULL")
                cursor.execute("update user_skcdp set DIRECTION=\' \' where DIRECTION IS NULL")
                cursor.execute("update user_skcdp set RHIERAR=\' \' where RHIERAR IS NULL")
                cursor.execute("update user_skcdp set SERVICE=\' \' where SERVICE IS NULL")
                cursor.execute("update user_skcdp set FONCTION=\' \' where FONCTION IS NULL")
                cursor.execute("update user_skcdp set STATUT_CPTE=\' \' where STATUT_CPTE IS NULL")
                cursor.execute("update user_skcdp set DATEOUVERT=\' \' where DATEOUVERT IS NULL")
                cursor.execute("update user_skcdp set DATEFERMET=\' \' where DATEFERMET IS NULL")
                cursor.execute("update user_skcdp set STATUT_OUV=\' \' where STATUT_OUV IS NULL")
                cursor.execute("update user_skcdp set STATUT_MOD=\' \' where STATUT_MOD IS NULL")
                cursor.execute("update user_skcdp set STATUT_FERM=\' \' where STATUT_FERM IS NULL")
                cursor.execute("update user_skcdp set LIEUINSTAL=\' \' where LIEUINSTAL IS NULL")
                cursor.execute("update user_skcdp set COMMENTAIRE=\' \' where COMMENTAIRE IS NULL")
                cursor.execute("update user_skcdp set CPTEORA=\' \' where CPTEORA IS NULL")
                cursor.execute("update user_skcdp set SEC_CODE=\' \' where SEC_CODE IS NULL")
                cursor.execute("update user_skcdp set SRV_GESPLA=\' \' where SRV_GESPLA IS NULL")

                #on enregistre les modification de la BD
                connexion_BD.commit()
                #on supprime la ligne sélectionnée
                treeview.delete(ligne_selectionnee)
                #on selectionne la ligne ajouté
                id = treeview.get_children()[0]
                treeview.selection_set(id)
                #on ferme la fenêtre fenetre_modifier
                fenetre_modifier.destroy()
                #on réactive tous les boutons de la fenetre_principale
                bouton_chercher.config(state=NORMAL)
                bouton_modifier.config(state=NORMAL)
                bouton_inserer.config(state=NORMAL)
                bouton_quitter.config(state=NORMAL)
            else:
                #on affiche un message d'erreur
				#on utilise des fenêtres Toplevel et pas des messagesbox pour éviter  que la fenêtre d'inserttion passe en arrière plan
                fenetre_erreur_date = tix.Toplevel()
                fenetre_erreur_date.title("Erreur")
                erreur = Label(fenetre_erreur_date, text = "La date doit être au format JJ/MM/AAAA ou nul", bg="#D7D8D8", fg="#E81616", font=("Arial", 12))
                erreur.pack()
                bouton_ok = Button(fenetre_erreur_date, text="OK", command=lambda:fenetre_erreur_date.destroy(), bg="#D7D8D8")
                bouton_ok.pack()
                fenetre_erreur_date.configure(background="#D7D8D8")

        else:
            #on affiche un message d'erreur
			#on utilise des fenêtres Toplevel et pas des messagesbox pour éviter  que la fenêtre d'inserttion passe en arrière plan
            fenetre_erreur_champs_vide = tix.Toplevel()
            fenetre_erreur_champs_vide.title("Erreur")
            erreur = Label(fenetre_erreur_champs_vide, text = "Les champs Cpte windowss et Nom doivent être remplis", bg="#D7D8D8", fg="#E81616", font=("Arial", 12))
            erreur.pack()
            bouton_ok = Button(fenetre_erreur_champs_vide, text="OK", command=lambda:fenetre_erreur_champs_vide.destroy(), bg="#D7D8D8")
            bouton_ok.pack()
            fenetre_erreur_champs_vide.configure(background="#D7D8D8")


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
    bouton_enregistrer_modifier = Button(fenetre_modifier, text="Enregistrer", command=lambda:modifierBD(), font=("Arial", 12))
    bouton_annuler_modifier = Button(fenetre_modifier, text="Annuler", command=lambda:annulerModification(), font=("Arial", 12))

    #on crée un canvas pour contenir les champs à modifier
    canvas_modifier = Canvas(fenetre_modifier, width=100, height=100, bg="#D7D8D8", highlightthickness=0)

    #on crée les textes à afficher au dessus des champs à compléter
    texte_compte_windows_modifier = Label(canvas_modifier, text="Cpte windows", bg="#D7D8D8", font=("Arial", 12))
    texte_type_modifier = Label(canvas_modifier, text="Type", bg="#D7D8D8", font=("Arial", 12))
    texte_nom_modifier = Label(canvas_modifier, text="Nom", bg="#D7D8D8", font=("Arial", 12))
    texte_prenom_modifier = Label(canvas_modifier, text="Prénom", bg="#D7D8D8", font=("Arial", 12))
    texte_ouverture_statut_modifier = Label(canvas_modifier, text="Ouverture St", bg="#D7D8D8", font=("Arial", 12))
    texte_ouverture_date_modifier = Label(canvas_modifier, text="Ouverture Date", bg="#D7D8D8", font=("Arial", 12))
    texte_fermeture_statut_modifier = Label(canvas_modifier, text="Fermeture St", bg="#D7D8D8", font=("Arial", 12))
    texte_fermeture_date_modifier = Label(canvas_modifier, text="Fermeture Date", bg="#D7D8D8", font=("Arial", 12))
    texte_direction_modifier = Label(canvas_modifier, text="Direction", bg="#D7D8D8", font=("Arial", 12))
    texte_service_modifier = Label(canvas_modifier, text="Service", bg="#D7D8D8", font=("Arial", 12))
    taxte_srv_gespla_modifier = Label(canvas_modifier, text="Srv Gespla", bg="#D7D8D8", font=("Arial", 12))
    texte_responsable_hierarchique_modifier = Label(canvas_modifier, text="Resp. Hiérar.", bg="#D7D8D8", font=("Arial", 12))
    texte_man_modifier = Label(canvas_modifier, text="Man.", bg="#D7D8D8", font=("Arial", 12))
    texte_fonction_modifier = Label(canvas_modifier, text="Fonction", bg="#D7D8D8", font=("Arial", 12))
    texte_outlook_modifier = Label(canvas_modifier, text="Outlook", bg="#D7D8D8", font=("Arial", 12))
    texte_acces_internet_modifier = Label(canvas_modifier, text="Accès Internet", bg="#D7D8D8", font=("Arial", 12))
    texte_vpn_modifier = Label(canvas_modifier, text="VPN", bg="#D7D8D8", font=("Arial", 12))
    texte_sap_modifier = Label(canvas_modifier, text="SAP", bg="#D7D8D8", font=("Arial", 12))
    texte_code_sap_modifier = Label(canvas_modifier, text="code SAP", bg="#D7D8D8", font=("Arial", 12))
    texte_perif_modifier = Label(canvas_modifier, text="Périf", bg="#D7D8D8", font=("Arial", 12))
    texte_pc_old_modifier = Label(canvas_modifier, text="PC Old", bg="#D7D8D8", font=("Arial", 12))
    texte_commentaire_modifier = Label(canvas_modifier, text="Commentaire", bg="#D7D8D8", font=("Arial", 12))
    texte_statut_modifier = Label(canvas_modifier, text="Statut", bg="#D7D8D8", font=("Arial", 12))
    texte_statut_modif_modifer = Label(canvas_modifier, text="Statut modif", bg="#D7D8D8", font=("Arial", 12))
    texte_compte_oracle_modifier = Label(canvas_modifier, text="Cpte Oracle", bg="#D7D8D8", font=("Arial", 12))
    texte_sect_xng_modifier = Label(canvas_modifier, text="Sect Xng", bg="#D7D8D8", font=("Arial", 12))

    #on crée les zones de texte à compléter
    champ_compte_windows_modifier = Entry(canvas_modifier, width=20)
    champ_nom_modifier = Entry(canvas_modifier, width=20)
    champ_prenom_modifier = Entry(canvas_modifier, width=20)
    champ_ouverture_date_modifier = Entry(canvas_modifier, width=20)
    champ_fermeture_date_modifier = Entry(canvas_modifier, width=20)
    champ_srv_gespla_modifier = Entry(canvas_modifier, width=20)
    champ_fonction_modifier = Entry(canvas_modifier, width=20)
    champ_code_sap_modifier = Entry(canvas_modifier, width=20)
    champ_commentaire_modifier = Entry(canvas_modifier, width=20)
    champ_compte_oracle_modifier = Entry(canvas_modifier, width=20)
    champ_sect_xng_modifier = Entry(canvas_modifier, width=20)
    champ_statut_modifier = Entry(canvas_modifier, width=20)
    champ_statut_modif_modifier = Entry(canvas_modifier, width=20)

    #on affiche les valeurs de la ligne sélectionnée dans les champs
    champ_compte_windows_modifier.insert(END, valeurs['text'])
    champ_nom_modifier.insert(END, valeurs['values'][1])
    if valeurs['values'][2] == ' ':
        champ_prenom_modifier.delete(0, "end")
    else:
        champ_prenom_modifier.insert(END, valeurs['values'][2])
    if valeurs['values'][4] == ' ':
        champ_ouverture_date_modifier.delete(0, "end")
    else:
        champ_ouverture_date_modifier.insert(END, valeurs['values'][4])
    if valeurs['values'][6] == ' ':
        champ_fermeture_date_modifier.delete(0, "end")
    else:
        champ_fermeture_date_modifier.insert(END, valeurs['values'][6])
    if valeurs['values'][9] == ' ':
        champ_srv_gespla_modifier.delete(0, "end")
    else:
        champ_srv_gespla_modifier.insert(END, valeurs['values'][9])
    if valeurs['values'][12] == ' ':
        champ_fonction_modifier.delete(0, "end")
    else:
	    champ_fonction_modifier.insert(END, valeurs['values'][12])
    if valeurs['values'][17] == ' ':
        champ_code_sap_modifier.delete(0, "end")
    else:
        champ_code_sap_modifier.insert(END, valeurs['values'][17])
    if valeurs['values'][20] == ' ':
        champ_commentaire_modifier.delete(0, "end")
    else:
        champ_commentaire_modifier.insert(END, valeurs['values'][20])
    if valeurs['values'][23] == ' ':
        champ_compte_oracle_modifier.delete(0, "end")
    else:
        champ_compte_oracle_modifier.insert(END, valeurs['values'][23])
    if valeurs['values'][24] == ' ':
        champ_sect_xng_modifier.delete(0, "end")
    else:
        champ_sect_xng_modifier.insert(END, valeurs['values'][24])
    if valeurs['values'][21] == ' ':
        champ_statut_modifier.delete(0, "end")
    else:
        champ_statut_modifier.insert(END, valeurs['values'][21])
    if valeurs['values'][22] == ' ':
        champ_statut_modif_modifier.delete(0, "end")
    else:
        champ_statut_modif_modifier.insert(END, valeurs['values'][22])

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
    case_outlook_modifier = Checkbutton(canvas_modifier, variable=Outlook_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][13] == "O":
        case_outlook_modifier.select()
    else:
        case_outlook_modifier.deselect()
    case_acces_internet_modifier = Checkbutton(canvas_modifier, variable=acces_internet_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][14] == "O":
        case_acces_internet_modifier.select()
    else:
        case_acces_internet_modifier.deselect()
    case_vpn_modifier = Checkbutton(canvas_modifier, variable=vpn_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][15] == "O":
        case_vpn_modifier.select()
    else:
        case_vpn_modifier.deselect()
    case_sap_modifier = Checkbutton(canvas_modifier, variable=sap_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][16] == "O":
        case_sap_modifier.select()
    else:
        case_sap_modifier.deselect()
    case_perif_modifier = Checkbutton(canvas_modifier, variable=perif_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][18] == "O":
        case_perif_modifier.select()
    else:
        case_perif_modifier.deselect()
    case_pc_old_modifier = Checkbutton(canvas_modifier, variable=pc_old_modifier, offvalue="N", onvalue="O")
    if valeurs['values'][19] == "O":
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

    #on rempli la liste type
    liste_type_modifier.insert(1, "AGE")
    liste_type_modifier.insert(2, "STG")
    liste_type_modifier.insert(3, "ADM")
    liste_type_modifier.insert(4, "USR")
    liste_type_modifier.insert(5, "EXT")
    liste_type_modifier.insert(6, "GEN")

	#on rempli la liste ouverture st
    liste_ouverture_statut_modifier.insert(1, "Ouvert")
    liste_ouverture_statut_modifier.insert(2, "Pas encore ouvert")

	#on rempli la liste fermeture st
    liste_fermeture_statut_modifier.insert(1, "Fermé")
    liste_fermeture_statut_modifier.insert(2, "Pas encore fermé")

	#on rempli la liste manager
    liste_man_modifier.insert(1, "Oui")
    liste_man_modifier.insert(2, "Non")

	#on rempli la liste direction
    cursor.execute("select distinct DIRECTION from user_skcdp")
    compteur_direction_modifier=1
    for modification_direction in cursor:
        liste_direction_modifier.insert(compteur_direction_modifier, modification_direction[0])
        compteur_direction_modifier+=1

	#on rempli la liste service
    cursor.execute("select distinct SERVICE from user_skcdp")
    compteur_service_modifier=1
    for modification_service in cursor:
        liste_service_modifier.insert(compteur_service_modifier, modification_service[0])
        compteur_service_modifier+=1

    #on rempli la liste responsable hiérarchique
    cursor.execute("select distinct RHIERAR from user_skcdp")
    compteur_responsable_hierarchique_modifier=1
    for modification_responsable_hierarchique in cursor:
        liste_responsable_hierarchique_modifier.insert(compteur_responsable_hierarchique_modifier, modification_responsable_hierarchique[0])
        compteur_responsable_hierarchique_modifier+=1

    #on affiche le canvas
    canvas_modifier.pack(expand="True", fill="both")

    #on affiche les titres des champs
    texte_compte_windows_modifier.grid(row=0, column=1, pady=5)
    texte_type_modifier.grid(row=0, column=2, pady=5)
    texte_nom_modifier.grid(row=0, column=3, pady=5)
    texte_prenom_modifier.grid(row=0, column=4, pady=5)
    texte_ouverture_statut_modifier.grid(row=0, column=5, pady=5)
    texte_ouverture_date_modifier.grid(row=0, column=6, pady=5)
    texte_fermeture_statut_modifier.grid(row=0, column=7, pady=5)
    texte_fermeture_date_modifier.grid(row=0, column=8, pady=5)
    texte_direction_modifier.grid(row=2, column=1, pady=5)
    texte_service_modifier.grid(row=2, column=2, pady=5)
    taxte_srv_gespla_modifier.grid(row=2, column=3, pady=5)
    texte_responsable_hierarchique_modifier.grid(row=2, column=4, pady=5)
    texte_man_modifier.grid(row=2, column=5, pady=5)
    texte_fonction_modifier.grid(row=2, column=6, pady=5)
    texte_outlook_modifier.grid(row=2, column=7, pady=5)
    texte_acces_internet_modifier.grid(row=2, column=8, pady=5)
    texte_vpn_modifier.grid(row=4, column=1, pady=5)
    texte_sap_modifier.grid(row=4, column=2, pady=5)
    texte_code_sap_modifier.grid(row=4, column=3, pady=5)
    texte_perif_modifier.grid(row=4, column=4, pady=5)
    texte_pc_old_modifier.grid(row=4, column=5, pady=5)
    texte_commentaire_modifier.grid(row=4, column=6, pady=5)
    texte_statut_modifier.grid(row=4, column=7, pady=5)
    texte_statut_modif_modifer.grid(row=4, column=8, pady=5)
    texte_compte_oracle_modifier.grid(row=6, column=1, pady=5)
    texte_sect_xng_modifier.grid(row=6, column=2, pady=5)

    #on affiche les champs à completer
    champ_compte_windows_modifier.grid(row=1, column=1, padx=5, pady=5)
    liste_type_modifier.grid(row=1, column=2, padx=5, pady=5)
    champ_nom_modifier.grid(row=1, column=3, padx=5, pady=5)
    champ_prenom_modifier.grid(row=1, column=4, padx=5, pady=5)
    liste_ouverture_statut_modifier.grid(row=1, column=5, padx=5, pady=5)
    champ_ouverture_date_modifier.grid(row=1, column=6, padx=5, pady=5)
    liste_fermeture_statut_modifier.grid(row=1, column=7, padx=5, pady=5)
    champ_fermeture_date_modifier.grid(row=1, column=8, padx=5, pady=5)
    liste_direction_modifier.grid(row=3, column=1, padx=5, pady=5)
    liste_service_modifier.grid(row=3, column=2, padx=5, pady=5)
    champ_srv_gespla_modifier.grid(row=3, column=3, padx=5, pady=5)
    liste_responsable_hierarchique_modifier.grid(row=3, column=4, padx=5, pady=5)
    liste_man_modifier.grid(row=3, column=5, padx=5, pady=5)
    champ_fonction_modifier.grid(row=3, column=6, padx=5, pady=5)
    case_outlook_modifier.grid(row=3, column=7, padx=5, pady=5)
    case_acces_internet_modifier.grid(row=3, column=8, padx=5, pady=5)
    case_vpn_modifier.grid(row=5, column=1, padx=5, pady=5)
    case_sap_modifier.grid(row=5, column=2, padx=5, pady=5)
    champ_code_sap_modifier.grid(row=5, column=3, padx=5, pady=5)
    case_perif_modifier.grid(row=5, column=4, padx=5, pady=5)
    case_pc_old_modifier.grid(row=5, column=5, padx=5, pady=5)
    champ_commentaire_modifier.grid(row=5, column=6, padx=5, pady=5)
    champ_statut_modifier.grid(row=5, column=7, padx=5, pady=5)
    champ_statut_modif_modifier.grid(row=5, column=8, padx=5, pady=5)
    champ_compte_oracle_modifier.grid(row=7, column=1, padx=5, pady=5)
    champ_sect_xng_modifier.grid(row=7, column=2, padx=5, pady=5)

    #on affiche les boutons
    bouton_enregistrer_modifier.pack(side="left", anchor="nw", padx=10, pady=5)
    bouton_annuler_modifier.pack(side="right", anchor="ne", padx=10, pady=5)

    #on colorie le background de la fenêtre en gris
    fenetre_modifier.configure(background="#D7D8D8")

	#on réactive les boutons si la fenêtre est fermé en cliquant sur la croix en haut à droite
    fenetre_modifier.protocol("WM_DELETE_WINDOW", lambda:annulerModification())

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
        if champ_compte_windows_inserer.get() != "" and champ_nom_inserer.get() != "":
        #on vérifie que la date est au bon format
            if (len(champ_ouverture_date_inserer.get()) == 10 or len(champ_ouverture_date_inserer.get()) == 0) and (len(champ_fermeture_date_inserer.get()) == 10 or len(champ_fermeture_date_inserer.get()) == 0):
                if liste_ouverture_statut_inserer['selection']=="Ouvert":
                    liste_ouverture_statut_inserer['selection']="T"
                if liste_ouverture_statut_inserer['selection']=="Pas encore ouvert":
                    liste_ouverture_statut_inserer['selection']=""
                if liste_fermeture_statut_inserer['selection']=="Fermé":
                    liste_fermeture_statut_inserer['selection']="T"
                if liste_fermeture_statut_inserer['selection']=="Pas encore fermé":
                    liste_fermeture_statut_inserer['selection']=""
                if liste_man_inserer['selection']=='Oui':
                    liste_man_inserer['selection']='O'
                else:
                    liste_man_inserer['selection']='N'
                #on ajoute la nouvelle ligne dans le tableau
                treeview.insert("", 0, text=champ_compte_windows_inserer.get().upper(), values=(liste_type_inserer['selection'], champ_nom_inserer.get().upper(),
                                        champ_prenom_inserer.get().upper(), liste_ouverture_statut_inserer['selection'], champ_ouverture_date_inserer.get(),
                                        liste_fermeture_statut_inserer['selection'], champ_fermeture_date_inserer.get(), liste_direction_inserer['selection'],
                                        liste_service_inserer['selection'], champ_srv_gespla_inserer.get(), liste_responsable_hierarchique_inserer['selection'],
                                        liste_man_inserer['selection'], champ_fonction_inserer.get().upper(), Outlook_inserer.get(), acces_internet_inserer.get(),
                                        vpn_inserer.get(), sap_inserer.get(), champ_code_sap_inserer.get(), perif_inserer.get(), pc_old_inserer.get(),
                                        champ_commentaire_inserer.get().capitalize(), champ_statut_inserer.get().upper(), champ_statut_modif_inserer.get().upper(),
                                        champ_compte_oracle_inserer.get(), champ_sect_xng_inserer.get()))
                #on met la date au bon format pour la BD
                if len(champ_ouverture_date_inserer.get()) == 10:
                    date_ouverture_inserer=champ_ouverture_date_inserer.get()
                    jour_ouverture_inserer=date_ouverture_inserer[:2]
                    mois_ouverture_inserer=date_ouverture_inserer[3:5]
                    annee_ouverture_inserer=date_ouverture_inserer[6:]
                    date_ouverture_inserer=annee_ouverture_inserer+mois_ouverture_inserer+jour_ouverture_inserer
                else:
                    date_ouverture_inserer=champ_ouverture_date_inserer.get()

                if len(champ_fermeture_date_inserer.get()) == 10:
                    date_fermeture_inserer=champ_fermeture_date_inserer.get()
                    jour_fermeture_inserer=date_fermeture_inserer[:2]
                    mois_fermeture_inserer=date_fermeture_inserer[3:5]
                    annee_fermeture_inserer=date_fermeture_inserer[6:]
                    date_fermeture_inserer=annee_fermeture_inserer+mois_fermeture_inserer+jour_fermeture_inserer
                else:
                    date_fermeture_inserer=champ_fermeture_date_inserer.get()

                #on récupère l'utilisateur qui effectue les modifications
                utilisateur_inserer=os.getenv("USERNAME")
                #on récupère la date et l'heure actuelle
                date=datetime.datetime.today()
                jour_inserer=date.strftime('%Y%m%d')
                heure_inserer=date.strftime('%H%M%S')
                #on modifie le tuple dans la table
                cursor.execute("insert into user_skcdp values(\'" + champ_compte_windows_inserer.get().upper() + "\', \'" + liste_type_inserer['selection'] + "\', \'" + champ_nom_inserer.get().upper() + "\', \'" + champ_prenom_inserer.get().upper() + "\', \'" + liste_direction_inserer['selection'] + "\', \'" + liste_responsable_hierarchique_inserer['selection'] + "\', \' \', \'" + liste_service_inserer['selection'] + "\', \'" + champ_fonction_inserer.get().upper() + "\', \'" + champ_statut_inserer.get().upper() + "\', \'" + date_ouverture_inserer + "\', \'" + date_fermeture_inserer + "\', \' \', \'" + liste_ouverture_statut_inserer['selection'] + "\', \'" + champ_statut_modif_inserer.get().upper() + "\', \'" + liste_fermeture_statut_inserer['selection'] + "\', \'" + Outlook_inserer.get() + "\', \'" + acces_internet_inserer.get() + "\', \'" + vpn_inserer.get() + "\', \'" + perif_inserer.get() + "\', \'" + sap_inserer.get() + "\', \' \', \'" + champ_code_sap_inserer.get().upper() + "\', \'" + champ_commentaire_inserer.get().capitalize() + "\', \'" + utilisateur_inserer + "\', \'" + jour_inserer + "\', \'" + heure_inserer + "\', \'" + champ_compte_oracle_inserer.get() + "\', \'\', \'" + champ_sect_xng_inserer.get() + "\', \'" + pc_old_inserer.get() + "\', \'" + champ_srv_gespla_inserer.get() + "\', \'" + liste_man_inserer['selection'] + "\')")
                #on modifie tous les champs nul pour éviter les erreurs
                cursor.execute("update user_skcdp set TYPCPTE=\' \' where TYPCPTE IS NULL")
                cursor.execute("update user_skcdp set PRENOM=\' \' where PRENOM IS NULL")
                cursor.execute("update user_skcdp set DIRECTION=\' \' where DIRECTION IS NULL")
                cursor.execute("update user_skcdp set RHIERAR=\' \' where RHIERAR IS NULL")
                cursor.execute("update user_skcdp set SERVICE=\' \' where SERVICE IS NULL")
                cursor.execute("update user_skcdp set FONCTION=\' \' where FONCTION IS NULL")
                cursor.execute("update user_skcdp set STATUT_CPTE=\' \' where STATUT_CPTE IS NULL")
                cursor.execute("update user_skcdp set DATEOUVERT=\' \' where DATEOUVERT IS NULL")
                cursor.execute("update user_skcdp set DATEFERMET=\' \' where DATEFERMET IS NULL")
                cursor.execute("update user_skcdp set STATUT_OUV=\' \' where STATUT_OUV IS NULL")
                cursor.execute("update user_skcdp set STATUT_MOD=\' \' where STATUT_MOD IS NULL")
                cursor.execute("update user_skcdp set STATUT_FERM=\' \' where STATUT_FERM IS NULL")
                cursor.execute("update user_skcdp set LIEUINSTAL=\' \' where LIEUINSTAL IS NULL")
                cursor.execute("update user_skcdp set COMMENTAIRE=\' \' where COMMENTAIRE IS NULL")
                cursor.execute("update user_skcdp set CPTEORA=\' \' where CPTEORA IS NULL")
                cursor.execute("update user_skcdp set SEC_CODE=\' \' where SEC_CODE IS NULL")
                cursor.execute("update user_skcdp set SRV_GESPLA=\' \' where SRV_GESPLA IS NULL")
                #on enregistre les modification de la BD
                connexion_BD.commit()
                #on selectionne la ligne ajouté
                id = treeview.get_children()[0]
                treeview.selection_set(id)
                #on ferme la fenêtre fenetre_inserer
                fenetre_inserer.destroy()
                #on réactive tous les boutons de la fenetre_principale
                bouton_chercher.config(state=NORMAL)
                bouton_modifier.config(state=NORMAL)
                bouton_inserer.config(state=NORMAL)
                bouton_quitter.config(state=NORMAL)
            else:
                #on affiche un message d'erreur
                #on utilise des fenêtres Toplevel et pas des messagesbox pour éviter  que la fenêtre d'inserttion passe en arrière plan
                fenetre_erreur_date = tix.Toplevel()
                fenetre_erreur_date.title("Erreur")
                erreur = Label(fenetre_erreur_date, text = "La date doit être au format JJ/MM/AAAA ou nul", bg="#D7D8D8", fg="#E81616", font=("Arial", 12))
                erreur.pack()
                bouton_ok = Button(fenetre_erreur_date, text="OK", command=lambda:fenetre_erreur_date.destroy(), bg="#D7D8D8")
                bouton_ok.pack()
                fenetre_erreur_date.configure(background="#D7D8D8")
        else:
            #on affiche un message d'erreur
            #on utilise des fenêtres Toplevel et pas des messagesbox pour éviter  que la fenêtre d'inserttion passe en arrière plan
            fenetre_erreur_champs_vide = tix.Toplevel()
            fenetre_erreur_champs_vide.title("Erreur")
            texte_erreur = Label(fenetre_erreur_champs_vide, text = "Les champs Cpte windows et Nom doivent être remplis", bg="#D7D8D8", fg="#E81616", font=("Arial", 12))
            texte_erreur.pack()
            bouton_ok = Button(fenetre_erreur_champs_vide, text="OK", command=lambda:fenetre_erreur_champs_vide.destroy(), bg="#D7D8D8")
            bouton_ok.pack()
            fenetre_erreur_champs_vide.configure(background="#D7D8D8")

    #on désactive les boutons de la fenetre_principale pour éviter les problèmes
    bouton_chercher.config(state=DISABLED)
    bouton_modifier.config(state=DISABLED)
    bouton_inserer.config(state=DISABLED)
    bouton_quitter.config(state=DISABLED)

    #on crée une fenêtre pour insérer un nouveau tuple
    fenetre_inserer = tix.Toplevel()
    fenetre_inserer.title("Insertion")

    #on crée un bouton de confirmation et un bouton d'annulation
    bouton_enregistrer_inserer = Button(fenetre_inserer, text="Enregistrer", command=lambda:ajouterBD(), font=("Arial", 12))
    bouton_annuler_inserer = Button(fenetre_inserer, text="Annuler", command=lambda:annulerInsertion(), font=("Arial", 12))

    #on crée un canvas pour contenir les champs à remplir
    canvas_insertion = Canvas(fenetre_inserer, width=100, height=100, bg="#D7D8D8", highlightthickness=0)

    #on crée les textes à afficher au dessus des champs à compléter
    texte_compte_windows_inserer = Label(canvas_insertion, text="Cpte windows", bg="#D7D8D8", font=("Arial", 12))
    texte_type_inserer = Label(canvas_insertion, text="Type", bg="#D7D8D8", font=("Arial", 12))
    texte_nom_inserer = Label(canvas_insertion, text="Nom", bg="#D7D8D8", font=("Arial", 12))
    texte_prenom_inserer = Label(canvas_insertion, text="Prénom", bg="#D7D8D8", font=("Arial", 12))
    texte_ouverture_statut_inserer = Label(canvas_insertion, text="Ouverture St", bg="#D7D8D8", font=("Arial", 12))
    texte_ouverture_date_inserer = Label(canvas_insertion, text="Ouverture Date", bg="#D7D8D8", font=("Arial", 12))
    texte_fermeture_statut_inserer = Label(canvas_insertion, text="Fermeture St", bg="#D7D8D8", font=("Arial", 12))
    texte_fermeture_date_inserer = Label(canvas_insertion, text="Fermeture Date", bg="#D7D8D8", font=("Arial", 12))
    texte_direction_inserer = Label(canvas_insertion, text="Direction", bg="#D7D8D8", font=("Arial", 12))
    texte_service_inserer = Label(canvas_insertion, text="Service", bg="#D7D8D8", font=("Arial", 12))
    taxte_srv_gespla_inserer = Label(canvas_insertion, text="Srv Gespla", bg="#D7D8D8", font=("Arial", 12))
    texte_responsable_hierarchique_inserer = Label(canvas_insertion, text="Resp. Hiérar.", bg="#D7D8D8", font=("Arial", 12))
    texte_man_inserer = Label(canvas_insertion, text="Man.", bg="#D7D8D8", font=("Arial", 12))
    texte_fonction_inserer = Label(canvas_insertion, text="Fonction", bg="#D7D8D8", font=("Arial", 12))
    texte_outlook_inserer = Label(canvas_insertion, text="Outlook", bg="#D7D8D8", font=("Arial", 12))
    texte_acces_internet_inserer = Label(canvas_insertion, text="Accès Internet", bg="#D7D8D8", font=("Arial", 12))
    texte_vpn_inserer = Label(canvas_insertion, text="VPN", bg="#D7D8D8", font=("Arial", 12))
    texte_sap_inserer = Label(canvas_insertion, text="SAP", bg="#D7D8D8", font=("Arial", 12))
    texte_code_sap_inserer = Label(canvas_insertion, text="code SAP", bg="#D7D8D8", font=("Arial", 12))
    texte_perif_inserer = Label(canvas_insertion, text="Périf", bg="#D7D8D8", font=("Arial", 12))
    texte_pc_old_inserer = Label(canvas_insertion, text="PC Old", bg="#D7D8D8", font=("Arial", 12))
    texte_commentaire_inserer = Label(canvas_insertion, text="Commentaire", bg="#D7D8D8", font=("Arial", 12))
    texte_statut_inserer = Label(canvas_insertion, text="Statut", bg="#D7D8D8", font=("Arial", 12))
    texte_statut_modif_inserer = Label(canvas_insertion, text="Statut modif", bg="#D7D8D8", font=("Arial", 12))
    texte_compte_oracle_inserer = Label(canvas_insertion, text="Cpte Oracle", bg="#D7D8D8", font=("Arial", 12))
    texte_sect_xng_inserer = Label(canvas_insertion, text="Sect Xng", bg="#D7D8D8", font=("Arial", 12))

    #on crée les zones à compléter
    champ_compte_windows_inserer = Entry(canvas_insertion, width=20)
    champ_nom_inserer = Entry(canvas_insertion, width=20)
    champ_prenom_inserer = Entry(canvas_insertion, width=20)
    champ_ouverture_date_inserer = Entry(canvas_insertion, width=20)
    champ_fermeture_date_inserer = Entry(canvas_insertion, width=20)
    champ_srv_gespla_inserer = Entry(canvas_insertion, width=20)
    champ_fonction_inserer = Entry(canvas_insertion, width=20)
    champ_code_sap_inserer = Entry(canvas_insertion, width=20)
    champ_commentaire_inserer = Entry(canvas_insertion, width=20)
    champ_compte_oracle_inserer = Entry(canvas_insertion, width=20)
    champ_sect_xng_inserer = Entry(canvas_insertion, width=20)
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
    case_outlook_inserer = Checkbutton(canvas_insertion, variable=Outlook_inserer, offvalue="N", onvalue="O")
    case_outlook_inserer.deselect()
    case_acces_internet_inserer = Checkbutton(canvas_insertion, variable=acces_internet_inserer, offvalue="N", onvalue="O")
    case_acces_internet_inserer.deselect()
    case_vpn_inserer = Checkbutton(canvas_insertion, variable=vpn_inserer, offvalue="N", onvalue="O")
    case_vpn_inserer.deselect()
    case_sap_inserer = Checkbutton(canvas_insertion, variable=sap_inserer, offvalue="N", onvalue="O")
    case_sap_inserer.deselect()
    case_perif_inserer = Checkbutton(canvas_insertion, variable=perif_inserer, offvalue="N", onvalue="O")
    case_perif_inserer.deselect()
    case_pc_old_inserer = Checkbutton(canvas_insertion, variable=pc_old_inserer, offvalue="N", onvalue="O")
    case_pc_old_inserer.deselect()

    #on crée les listes déroulantes
    liste_type_inserer = tix.ComboBox(canvas_insertion)
    liste_ouverture_statut_inserer = tix.ComboBox(canvas_insertion)
    liste_fermeture_statut_inserer = tix.ComboBox(canvas_insertion)
    liste_direction_inserer = tix.ComboBox(canvas_insertion)
    liste_service_inserer = tix.ComboBox(canvas_insertion)
    liste_responsable_hierarchique_inserer = tix.ComboBox(canvas_insertion)
    liste_man_inserer = tix.ComboBox(canvas_insertion)

    #on rempli la liste type
    liste_type_inserer.insert(1, "AGE")
    liste_type_inserer.insert(2, "STG")
    liste_type_inserer.insert(3, "ADM")
    liste_type_inserer.insert(4, "USR")
    liste_type_inserer.insert(5, "EXT")
    liste_type_inserer.insert(6, "GEN")

	#on rempli la liste ouverture st
    liste_ouverture_statut_inserer.insert(1, "Ouvert")
    liste_ouverture_statut_inserer.insert(2, "Pas encore ouvert")

	#on rempli la lisste fermeture st
    liste_fermeture_statut_inserer.insert(1, "Fermé")
    liste_fermeture_statut_inserer.insert(2, "Pas encore fermé")

	#on rempli la liste manager
    liste_man_inserer.insert(1, "Oui")
    liste_man_inserer.insert(2, "Non")

	#on rempli la liste direction
    cursor.execute("select distinct DIRECTION from user_skcdp")
    compteur_direction_inserer=1
    for insertion_direction in cursor:
        liste_direction_inserer.insert(compteur_direction_inserer, insertion_direction[0])
        compteur_direction_inserer+=1

    #on rempli la liste service
    cursor.execute("select distinct SERVICE from user_skcdp")
    compteur_service_inserer=1
    for insertion_service in cursor:
        liste_service_inserer.insert(compteur_service_inserer, insertion_service[0])
        compteur_service_inserer+=1

    #on rempli la liste responsable hiérarchique
    cursor.execute("select distinct RHIERAR from user_skcdp")
    compteur_responsable_hierarchique_inserer=1
    for insertion_responsable_hierarchique in cursor:
        liste_responsable_hierarchique_inserer.insert(compteur_responsable_hierarchique_inserer, insertion_responsable_hierarchique[0])
        compteur_responsable_hierarchique_inserer+=1

    #on affiche le canvas
    canvas_insertion.pack(expand="True", fill="both")

    #on affiche les titres des champs
    texte_compte_windows_inserer.grid(row=0, column=1, pady=5)
    texte_type_inserer.grid(row=0, column=2, pady=5)
    texte_nom_inserer.grid(row=0, column=3, pady=5)
    texte_prenom_inserer.grid(row=0, column=4, pady=5)
    texte_ouverture_statut_inserer.grid(row=0, column=5, pady=5)
    texte_ouverture_date_inserer.grid(row=0, column=6, pady=5)
    texte_fermeture_statut_inserer.grid(row=0, column=7, pady=5)
    texte_fermeture_date_inserer.grid(row=0, column=8, pady=5)
    texte_direction_inserer.grid(row=2, column=1, pady=5)
    texte_service_inserer.grid(row=2, column=2, pady=5)
    taxte_srv_gespla_inserer.grid(row=2, column=3, pady=5)
    texte_responsable_hierarchique_inserer.grid(row=2, column=4, pady=5)
    texte_man_inserer.grid(row=2, column=5, pady=5)
    texte_fonction_inserer.grid(row=2, column=6, pady=5)
    texte_outlook_inserer.grid(row=2, column=7, pady=5)
    texte_acces_internet_inserer.grid(row=2, column=8, pady=5)
    texte_vpn_inserer.grid(row=4, column=1, pady=5)
    texte_sap_inserer.grid(row=4, column=2, pady=5)
    texte_code_sap_inserer.grid(row=4, column=3, pady=5)
    texte_perif_inserer.grid(row=4, column=4, pady=5)
    texte_pc_old_inserer.grid(row=4, column=5, pady=5)
    texte_commentaire_inserer.grid(row=4, column=6, pady=5)
    texte_statut_inserer.grid(row=4, column=7, pady=5)
    texte_statut_modif_inserer.grid(row=4, column=8, pady=5)
    texte_compte_oracle_inserer.grid(row=6, column=1, pady=5)
    texte_sect_xng_inserer.grid(row=6, column=2, pady=5)

    #on affiche les champs à completer
    champ_compte_windows_inserer.grid(row=1, column=1, padx=5, pady=5)
    liste_type_inserer.grid(row=1, column=2, padx=5, pady=5)
    champ_nom_inserer.grid(row=1, column=3, padx=5, pady=5)
    champ_prenom_inserer.grid(row=1, column=4, padx=5, pady=5)
    liste_ouverture_statut_inserer.grid(row=1, column=5, padx=5, pady=5)
    champ_ouverture_date_inserer.grid(row=1, column=6, padx=5, pady=5)
    liste_fermeture_statut_inserer.grid(row=1, column=7, padx=5, pady=5)
    champ_fermeture_date_inserer.grid(row=1, column=8, padx=5, pady=5)
    liste_direction_inserer.grid(row=3, column=1, padx=5, pady=5)
    liste_service_inserer.grid(row=3, column=2, padx=5, pady=5)
    champ_srv_gespla_inserer.grid(row=3, column=3, padx=5, pady=5)
    liste_responsable_hierarchique_inserer.grid(row=3, column=4, padx=5, pady=5)
    liste_man_inserer.grid(row=3, column=5, padx=5, pady=5)
    champ_fonction_inserer.grid(row=3, column=6, padx=5, pady=5)
    case_outlook_inserer.grid(row=3, column=7, padx=5, pady=5)
    case_acces_internet_inserer.grid(row=3, column=8, padx=5, pady=5)
    case_vpn_inserer.grid(row=5, column=1, padx=5, pady=5)
    case_sap_inserer.grid(row=5, column=2, padx=5, pady=5)
    champ_code_sap_inserer.grid(row=5, column=3, padx=5, pady=5)
    case_perif_inserer.grid(row=5, column=4, padx=5, pady=5)
    case_pc_old_inserer.grid(row=5, column=5, padx=5, pady=5)
    champ_commentaire_inserer.grid(row=5, column=6, padx=5, pady=5)
    champ_statut_inserer.grid(row=5, column=7, padx=5, pady=5)
    champ_statut_modif_inserer.grid(row=5, column=8, padx=5, pady=5)
    champ_compte_oracle_inserer.grid(row=7, column=1, padx=5, pady=5)
    champ_sect_xng_inserer.grid(row=7, column=2, padx=5, pady=5)

    #on affiche les boutons
    bouton_enregistrer_inserer.pack(side="left", anchor="nw", padx=10, pady=5)
    bouton_annuler_inserer.pack(side="right", anchor="ne", padx=10, pady=5)

    #on colorie le background de la fenêtre en gris
    fenetre_inserer.configure(background="#D7D8D8")

	#on réactive les boutons si la fenêtre est fermé en cliquant sur la croix en haut à droite
    fenetre_inserer.protocol("WM_DELETE_WINDOW", lambda:annulerInsertion())

#cette fonction à pour but de fermer et détruire la fenetre_principale lors de la confirmation de fermeture
def toutFermer():
    #on ferme le curseur
    cursor.close()
    #on se déconnecte de BD
    connexion_BD.close()
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
    texte_confirmation = Label(fenetre_quitter, text="Etes-vous sûr de vouloir quitter USERSKCDP ?", bg="#D7D8D8", font=("Arial", 12))

    #on crée un bouton de confirmation et un bouton d'annulation
    bouton_confirmer = Button(fenetre_quitter, text="Confirmer", command=lambda:toutFermer(), font=("Arial", 12))
    bouton_annuler_quitter = Button(fenetre_quitter, text="Annuler", command=lambda:annulerQuitter(), font=("Arial", 12))

    #on affiche tous les widgets
    texte_confirmation.grid(row=0, column=2, padx=10, pady=5)
    bouton_confirmer.grid(row=1, column=1, padx=10, pady=5)
    bouton_annuler_quitter.grid(row=1, column=3, padx=10, pady=5)

    #on colorie le background de la fenêtre en bleu
    fenetre_quitter.configure(background="#D7D8D8")

	#on réactive les boutons si la fenêtre est fermé en cliquant sur la croix en haut à droite
    fenetre_quitter.protocol("WM_DELETE_WINDOW", lambda:annulerQuitter())

"""---déclaration des variables---"""
#on crée la fenêtre principale
fenetre_principale = tix.Tk()
#on donne un titre à cette fenêtre
fenetre_principale.title("USERSKCDP")

try:
    #on se connecte à la BD
    connexion_BD = cx_Oracle.connect('id/password@serveur')
	#on crée un curseur pour effectuer les requêtes
    cursor = connexion_BD.cursor()
except:
    messagebox.showerror("Erreur de connexion", "Impossible de se connecter à la base de données prod_servau")
    quit()

#on crée un canvas pour placer le texte en entête de l'application
canvas_entete = Canvas(fenetre_principale, width=1250, height=5, bg="black", highlightthickness=0)

#on crée une variable date qui récupère la date et l'heure actuelle
date = datetime.datetime.now()
#on met toute la phrase dans une variable date_complete pour l'afficher dans le label
date_complete = "Connexion débutée le : " + date.strftime("%d/%m/%Y") +  " à : " + date.strftime("%H:%M")
#on crée les textes à afficher en entête
texte_date_heure = Label(canvas_entete, text=date_complete, bg="black", fg="#D7D8D8", font=("Arial", 12))
utilisateur_connecte="connecté(e) en tant que " + os.getenv("USERNAME")
texte_utilissateur = Label(canvas_entete, text=utilisateur_connecte, bg="black", fg="#D7D8D8", font=("Arial", 12))

#on crée le logo à afficher
photo=PhotoImage(file='logo.png')
logo=Label(fenetre_principale, image=photo)

#on crée un canvas pour séparé l'entête du reste de la fenêtre
canvas_ligne = Canvas(fenetre_principale, width=100, height=5, bg="black", highlightthickness=0)

#on crée un canvas pour placer les champs à completer et leur titres
canvas_recherche = Canvas(fenetre_principale, width=1250, height=5, bg="#D7D8D8", highlightthickness=0)

#on crée les textes à afficher au dessus des champs à compléter
texte_compte_windows = Label(canvas_recherche, text="Compte windows", bg="#D7D8D8", fg="black", font=("Arial", 12))
texte_nom = Label(canvas_recherche, text="Nom", bg="#D7D8D8", fg="black", font=("Arial", 12))
texte_direction = Label(canvas_recherche, text="Direction", bg="#D7D8D8", fg="black", font=("Arial", 12))
texte_service = Label(canvas_recherche, text="Service", bg="#D7D8D8", fg="black", font=("Arial", 12))
texte_responsable_hierarchique = Label(canvas_recherche, text="Responsable hiérarchique", bg="#D7D8D8", fg="black", font=("Arial", 12))
texte_statut_compte = Label(canvas_recherche, text="Statut du compte", bg="#D7D8D8", fg="black", font=("Arial", 12))

#on crée les champs à compléter pour la recherche
champ_compte_windows = Entry(canvas_recherche, width=20)
champ_nom = Entry(canvas_recherche, width=20)

#on crée les listes déroulantes pour les champs direction, service et responsable hiérarchique
liste_direction = tix.ComboBox(canvas_recherche)
liste_service = tix.ComboBox(canvas_recherche)
liste_responsable_hierarchique = tix.ComboBox(canvas_recherche)
liste_statut_compte = tix.ComboBox(canvas_recherche)

#on rempli la liste de statut du compte
liste_statut_compte.insert(1, "Ouvert")
liste_statut_compte.insert(2, "Fermé")
liste_statut_compte.insert(3, "Tous")

#on rempli la liste direction
cursor.execute("select distinct DIRECTION from user_skcdp")
compteur_direction_recherche=1
for recherche_direction in cursor:
    liste_direction.insert(compteur_direction_recherche, recherche_direction[0])
    compteur_direction_recherche+=1

#on rempli la liste service
cursor.execute("select distinct SERVICE from user_skcdp")
compteur_service_recherche=1
for recherche_service in cursor:
    liste_service.insert(compteur_service_recherche, recherche_service[0])
    compteur_service_recherche+=1

#on rempli la liste responsable hiérarchique
cursor.execute("select distinct RHIERAR from user_skcdp")
compteur_responsable_hierarchique_recherche=1
for recherche_responsable_hierarchique in cursor:
    liste_responsable_hierarchique.insert(compteur_responsable_hierarchique_recherche, recherche_responsable_hierarchique[0])
    compteur_responsable_hierarchique_recherche+=1

#on crée un canvas pour l'ensemble du treeview avec les scrollBar
canvas_centre = Canvas(fenetre_principale, width=1200, height=450, bg="white", highlightthickness=0)

#on crée un canvas pour le treeview
canvas_tableau = Canvas(canvas_centre, width=100, height=450, bg="white", highlightthickness=0)

#on crée les deux scrollbar pour naviguer dans le treeview
scrollbar_horizontal = Scrollbar(canvas_centre, orient=HORIZONTAL)
scrollbar_vertical = Scrollbar(canvas_centre, orient=VERTICAL)

#on crée un canvas pour les boutons
canvas_bouton = Canvas(fenetre_principale, width=100, height=100, bg="white", highlightthickness=0)

#on crée les boutons
bouton_chercher = Button(canvas_recherche, text="Chercher", command=lambda:recherche(), font=("Arial", 12))
bouton_inserer = Button(canvas_bouton, text="Insérer", command=lambda:inserer(), font=("Arial", 12))
bouton_modifier = Button(canvas_bouton, text="Modifier", command=lambda:modifier(), font=("Arial", 12))
bouton_quitter = Button(canvas_bouton, text="Quitter", command=lambda:quitter(), font=("Arial", 12))

#personnalisation de l'entête du treeview
style = ttk.Style()
style.configure("treeview.Treeview.Heading", font=("Arial", 12), foreground="#00AAD0")
style.configure("treeview.Treeview", font=("Arial", 12))

#création du treeview
treeview = ttk.Treeview(canvas_tableau, style="treeview.Treeview")

#on configure la navigation avec scrollBar
treeview.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

#on configure les scrollbar
scrollbar_vertical.configure(command=treeview.yview)
scrollbar_horizontal.configure(command=treeview.xview)

"""---placement des différents éléments---"""
#placement de l'entête
canvas_entete.pack(fill=X)

#placement des textes dans l'entête de l'application
texte_date_heure.pack(side="left", anchor="ne", padx=5)
texte_utilissateur.pack(side="right", anchor="nw", padx=5)

#placement du canvas_ligne de façon à ce qu'il occupe toute la largeur de la fenêtre
canvas_ligne.pack(fill=X)

#trace des lignes avec comme paramètre les coordonnées x1, y1, x2, y2 des deux points de la ligne
canvas_ligne.create_line(0, 9, 20000, 9, fill="#00AAD0")
canvas_ligne.create_line(0, 8, 20000, 8, fill="#00AAD0")
canvas_ligne.create_line(0, 7, 20000, 7, fill="#00AAD0")
canvas_ligne.create_line(0, 6, 20000, 6, fill="#00AAD0")
canvas_ligne.create_line(0, 5, 20000, 5, fill="#00AAD0")
canvas_ligne.create_line(0, 4, 20000, 4, fill="#00AAD0")
canvas_ligne.create_line(0, 3, 20000, 3, fill="#00AAD0")
canvas_ligne.create_line(0, 2, 20000, 2, fill="#00AAD0")
canvas_ligne.create_line(0, 1, 20000, 1, fill="#00AAD0")

#on affcihe le logo
logo.pack(anchor="w")

#placement du canvas pour effectuer la recherche
canvas_recherche.pack(fill=X)

#placement des textes au dessus des champs à remplir
texte_compte_windows.grid(row=3, column=1, padx=20, pady=5)
texte_nom.grid(row=3, column=2, padx=20, pady=5)
texte_direction.grid(row=3, column=3, padx=20, pady=5)
texte_service.grid(row=3, column=4, padx=20, pady=5)
texte_responsable_hierarchique.grid(row=3, column=5, padx=20, pady=5)
texte_statut_compte.grid(row=3, column=6, padx=20, pady=5)

#on affiche le bouton de Recherche
bouton_chercher.grid(row=4, column=7, padx=20, pady=5)

#placement des champs à compléter
champ_compte_windows.grid(row=4, column=1, padx=20, pady=5)
champ_nom.grid(row=4, column=2, padx=20, pady=5)

#placement des listes
liste_direction.grid(row=4, column=3, padx=20, pady=5)
liste_service.grid(row=4, column=4, padx=20, pady=5)
liste_responsable_hierarchique.grid(row=4, column=5, padx=20, pady=5)
liste_statut_compte.grid(row=4, column=6, padx=20, pady=5)


#placement du canvas_centre de façon à ce qu'il occupe la partie du milieu de l'écran
canvas_centre.pack(fill=X)

#on déclare les colonnes du treeview
treeview["columns"]=("texte_tab_cpte_windows", "texte_tab_type", "texte_tab_nom", "texte_tab_prenom", "texte_tab_ouverture_statut",
                            "texte_tab_ouverture_date", "texte_tab_fermeture_statut", "texte_tab_fermeture_date", "texte_tab_direction",
                            "texte_tab_service", "texte_tab_srv_gespla", "texte_tab_responsable", "texte_tab_man", "texte_tab_fonction",
                            "texte_tab_outlook", "texte_tab_acces_internet", "texte_tab_vpn", "texte_tab_sap", "texte_tab_code_sap",
                            "texte_tab_perif", "texte_tab_pc_old", "texte_tab_commentaire", "texte_tab_statut", "texte_tab_statut_modif",
                            "texte_tab_compte_oracle", "texte_tab_sect_xng")

#on configure les colonnes du treeview
treeview.column("#0", width=150, stretch=False)
treeview.column("#1", width=130, stretch=False)
treeview.column("#2", width=120, stretch=False)
treeview.column("#3", width=120, stretch=False)
treeview.column("#4", width=130, stretch=False)
treeview.column("#5", width=130, stretch=False)
treeview.column("#6", width=130, stretch=False)
treeview.column("#7", width=130, stretch=False)
treeview.column("#8", width=180, stretch=False)
treeview.column("#9", width=180, stretch=False)
treeview.column("#10", width=100, stretch=False)
treeview.column("#11", width=120, stretch=False)
treeview.column("#12", width=100, stretch=False)
treeview.column("#13", width=120, stretch=False)
treeview.column("#14", width=100, stretch=False)
treeview.column("#15", width=120, stretch=False)
treeview.column("#16", width=100, stretch=False)
treeview.column("#17", width=100, stretch=False)
treeview.column("#18", width=100, stretch=False)
treeview.column("#19", width=100, stretch=False)
treeview.column("#20", width=100, stretch=False)
treeview.column("#21", width=200, stretch=False)
treeview.column("#22", width=100, stretch=False)
treeview.column("#23", width=100, stretch=False)
treeview.column("#24", width=150, stretch=False)
treeview.column("#25", width=100, stretch=False)

#on nome les colonnes du treeview
treeview.heading("#0", text="Cpte windows")
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
treeview.heading("#25", text="Sect Xng")

#placement des scrollbar
scrollbar_vertical.pack(side="left", fill=Y)
scrollbar_horizontal.pack(side="bottom", fill=X)

#placement du canvas_tableau dans canvas_centre
canvas_tableau.pack(expand="True", fill="both")

#on affiche le treeview
treeview.pack(expand="True", fill="both")

#on affiche le canvas des bouttons
canvas_bouton.pack(pady=5)

#placement des boutons
bouton_inserer.grid(row=1, column=1, padx=100, pady=10)
bouton_modifier.grid(row=1, column=2, padx=100, pady=10)
bouton_quitter.grid(row=1, column=3, padx=100, pady=10)

#affiche la fenetre_principale en pleine écran à l'ouverture
#fenetre_principale.attributes("-fullscreen", 1)

#on colorie le background de la fenêtre en gris
fenetre_principale.configure(background="white")

#on empêche les canvas_centre de s'aggrandir en fonction de la taille du treeview
canvas_centre.propagate(False)

#on démarre la boucle tKinter pour conserver la fenêtre ouverte
fenetre_principale.mainloop()

#on se déconnecte de la BD si la fenêtre est fermé en cliquant sur la croix en haut à droite
fenetre_principale.protocol("WM_DELETE_WINDOW", lambda:toutFermer())
