import tkinter 
from customtkinter import *
from PIL import Image
#ajouter image

app=tkinter.Tk()
app.geometry("500x400")


#set_appearance_mode("dark")

#img=Image.open("loupe-fond-quadrille_1262-6424.avif")
#ajouter image
btn=CTkButton(master=app, text="rechercher", corner_radius=32, fg_color="#000000",
               hover_color="#CF40C0",border_color="#FFFFFF",
               border_width=1,)
#image pour ajouter sur le bouton

btn.place(relx=0.5,rely=0.5,anchor="center")


app.mainloop()
#################################################################################################
#écrire
from customtkinter import*

app=CTk()
app.geometry("500x400")

label=CTkLabel(master=app, text="rechercher", font=("Arial",20),text_color="#CF40C0")

label.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()

#################################################################################################


app=CTk()
app.geometry("500x400")

combobox=CTkComboBox(master=app, values=["Action","Romance","Drame","Comedie",".",","], fg_color="#34828C",
                     border_color="#439177", dropdown_fg_color="#439177")

combobox.place(relx=0.5,rely=0.5, anchor="center")
               
               
app.mainloop()
#################################################################################################
"""from customtkinter import *
from PIL import Image, ImageTk

app = CTk()
app.geometry("400x400")

img = Image.open("loupe-fond-quadrille_1262-6424.png")
img_small = img.resize((200, 200))
img_zoom = img.resize((300, 300))

img_small_tk = ImageTk.PhotoImage(img_small)
img_zoom_tk = ImageTk.PhotoImage(img_zoom)

label = CTkLabel(app, image=img_small_tk, text="")
label.pack(expand=True)

label.bind("<Enter>", lambda e: label.configure(image=img_zoom_tk))
label.bind("<Leave>", lambda e: label.configure(image=img_small_tk))

app.mainloop()"""
#################################################################################################
def rechercher(event=None):
    recherche = search_entry.get()
    categorie = combobox.get()
    print(f"Recherche : {recherche} | Catégorie : {categorie}")
search_entry = CTkEntry(
    fen_princ,
    width=350,
    height=40,
    placeholder_text="Rechercher un film...",
    fg_color="#1E1E1E",
    text_color="white",
    border_color="#CF40C0",
    corner_radius=20
)
search_entry.grid(row=2, column=0, padx=20, pady=20, sticky="w")

# Appui sur Entrée
search_entry.bind("<Return>", rechercher)
