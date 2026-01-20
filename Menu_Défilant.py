from tkinter import *
from customtkinter import*
import difflib


# Création de la fenêtre
fen_princ = CTk()
fen_princ.title("Search Movies")
fen_princ.geometry("900x600")

combobox=CTkComboBox(master=zoneMenu, values=["Action","Romance","Drame","Comedie"],text_color="#FFFFFF", fg_color="#000000",
                     border_color="#CF40C0", dropdown_fg_color="#FFFFFF")

#combobox.place(relx=0.5,rely=0.5, anchor="center")
combobox.grid(row=1,column=3)              

categories = ["Action", "Romance", "Drame", "Comedie"]
def corriger_texte(event=None):
    texte = combobox.get()

    if texte == "":
        return

    correspondance = difflib.get_close_matches(
        texte,
        categories,
        n=1,
        cutoff=0.5   # tolérance aux fautes (0.0 → très large / 1.0 → strict)
    )

    if correspondance:
        combobox.set(correspondance[0])
combobox.bind("<Return>", corriger_texte)
combobox.bind("<FocusOut>", corriger_texte)


fen_princ.mainloop()