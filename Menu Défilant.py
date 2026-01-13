#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *


# Création de la fenêtre

fen_princ = Tk()

fen_princ.title("Mon application à moi que j'ai")

fen_princ.geometry("900x600")


# Création du cadre-conteneur pour les menus

zoneMenu = Frame(fen_princ, borderwidth=3, bg='#557788')

zoneMenu.grid(row=0,column=0)


# Création de l'onglet Fichier

menuFichier = Menubutton(zoneMenu, text='Fichier', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuFichier.grid(row=0,column=0)


# Création de l'onglet Edition

menuEdit = Menubutton(zoneMenu, text='Editer', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuEdit.grid(row=0,column=1)


# Création de l'onglet Format

menuFormat = Menubutton(zoneMenu, text='Format', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)

menuFormat.grid(row=0,column=2)

# Création de l'onglet Affichage

menuAffichage = Menubutton(zoneMenu, text='Affichage', width='20', borderwidth=2, bg='white', activebackground='darkorange',relief = RAISED)

menuAffichage.grid(row=1,column=3)

# Création d'un menu défilant
# Définitions des fonctions

def petitFormat():

    print("Petit format")


def formatNormal():

    print("Format Normal")


def grandFormat():

    print("Grand format")


def fondClair():

    print("Fond Clair")


def fondSombre():

    print("Fond Sombre")

menuDeroulant1 = Menu(menuAffichage)

menuDeroulant1.add_command(label='Petit format', command = petitFormat)

menuDeroulant1.add_command(label="Normal", command = formatNormal)

menuDeroulant1.add_command(label="Grand format", command = grandFormat)

menuDeroulant1.add_command(label="Fond clair", command = fondClair)

menuDeroulant1.add_command(label="Fond sombre", command = fondSombre)

# Attribution du menu déroulant au menu Affichage

menuAffichage.configure(menu=menuDeroulant1)
menuDeroulant1.add_command(label="Fond sombre", command = fondSombre)


# Attribution du menu déroulant au menu Affichage

menuAffichage.configure(menu=menuDeroulant1)

fen_princ.mainloop()