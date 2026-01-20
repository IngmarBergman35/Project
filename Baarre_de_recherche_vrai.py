import tkinter as tk
from fonction import *

#creation de la fenetre principale

app = tk.Tk()
app.title("Moteur de recherche")
app.resizable(True, True)   #autorise le  redimensionnement
app.config(bg="#8B008B")  #fond violet foncé 

interesant=[
    'title',
    'original_title',                    
    'release_date',
    'genres',
    'overview',
    'tagline',
    'vote_average',
    'vote_count',
    'cast',
    'director',
    'runtime',
    'production_companies',
    'production_countries',            #info qu'on veut
    'budget',
    'homepage']
#Frame principale
frame = tk.Frame(app, bg="#FFC0CB", padx=20, pady=20)  #rose clair
frame.grid(row=0, column=0)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1) 
frame.grid(row=0, column=0, sticky="nsew")
#Titre
lab1 = tk.Label(
    frame,
    text="Moteur de recherche",
    font=("Cambria", 22, "bold"),
    bg="#FF69B4",  #rose vif
    fg="white",
    padx=10,
    pady=10
)
lab1.grid(row=0, column=0, pady=10)

#Champ de recherche
entry1 = tk.Entry(
    frame,
    width=40,
    font=("Cambria", 14),
    bg="#C8FACC",  #vert clair
    fg="#4B0082",  #texte violet foncé 
    relief="flat",
    bd=5,
)
entry1.grid(row=1, column=0, pady=5)

#Zone d'affichage des résultats
resultats = tk.Text(
    frame,
    width=45,
    height=10,
    font=("Cambria", 12),
    bg="#E8F9E9",  #vert very clair
    fg="#4B0082",  #texte violet foncéé
    bd=3,
    relief="sunken"
)
resultats.grid(row=3, column=0, pady=10)
entry1.bind("<Return>", lambda event: lancer_recherche())
entry1.focus()

#Fonction de recherche
def lancer_recherche():
    """IN: le nom du film entré par l'utilisateur,
   appelle la fonction rechercheFilm()
   OUT: affiche les résultats dans la zone de texte."""
    film = entry1.get().strip()  #Recup texte entrée
    resultats.delete("1.0", tk.END) #Nettoyage zone rés

    if film == "":   #Vérif champ vide
        resultats.insert(tk.END, "Veuillez entrer un nom de film.")
        return

    films_trouves = rechercheFilm(film)

    if not films_trouves:
        resultats.insert(tk.END, "Aucun film trouvé.")
    else: #Affichage des champs souhaitées
        for champ in interesant:
            if champ in films_trouves and films_trouves[champ]:
                resultats.insert(
                    tk.END,
                    f"{champ.replace('_', ' ').title()} : {films_trouves[champ]}\n\n"
                )

#Bouton
button1 = tk.Button(
    frame,
    text="Rechercher",
    font=("Cambria", 14, "bold"),
    bg="#FF69B4",  #rose vif
    fg="#C8FACC",  #vert clair
    activebackground="#FF1493",  #rose foncé au clic
    activeforeground="white",
    relief="raised",
    padx=10,
    pady=5,
    command=lancer_recherche   #Lance recherche au clic
)
button1.grid(row=2, column=0, pady=10)
#PRIMORDIAL ----> LANCE L'APP
app.mainloop()
