import customtkinter as ctk
from fonctionNew import *

# -------- Configuration globale --------
ctk.set_appearance_mode("light")  # "dark" ou "light"

# -------- Fenêtre principale --------
app = ctk.CTk()
app.title("Moteur de recherche")
app.resizable(False, False)
app.configure(fg_color="#FF87DF")  # violet clair

interesant = [
    'title', 'original_title', 'release_date', 'genres', 'overview', 'tagline',
    'vote_average', 'vote_count', 'cast', 'director', 'runtime',
    'production_companies', 'production_countries', 'budget', 'homepage'
]

# -------- Frame principale --------
frame = ctk.CTkFrame(
    app,
    fg_color="#FF87DF",
    corner_radius=20,
    border_color="#FF1493",
    border_width=3
)
frame.grid(row=0, column=0, padx=20, pady=20)

# -------- Titre --------
lab1 = ctk.CTkButton(
    frame,
    text="Moteur de recherche",
    font=("Cambria", 22, "bold"),
    fg_color="#FF87DF",border_color="#FFFFFF",hover_color="#0B801B",
    text_color="white",
    corner_radius=15
)
lab1.grid(row=0, column=0, padx=15, pady=10)

# -------- Champ de recherche --------
entry1 = ctk.CTkEntry(
    frame,
    width=350,
    height=35,
    font=("Cambria", 14),
    fg_color="#C8FACC",     # vert clair
    text_color="#4B0082",   # violet foncé
    corner_radius=10
)
entry1.grid(row=1, column=0, pady=5)

# -------- Zone d'affichage des résultats --------
resultats = ctk.CTkTextbox(
    frame,
    width=400,
    height=200,
    font=("Cambria", 12),
    fg_color="#E8F9E9",     # vert très clair
    text_color="#4B0082",
    corner_radius=10
)
resultats.grid(row=3, column=0, pady=10)
entry1.bind("<Return>", lambda event: lancer_recherche())
entry1.focus()

# -------- Fonction de recherche --------
def lancer_recherche():
    film = entry1.get().strip()
    resultats.delete("1.0", "end")

    if film == "":
        resultats.insert("end", "Veuillez entrer un nom de film.")
        return

    films_trouves = rechercheFilm(film)

    if not films_trouves:
        resultats.insert("end", "Aucun film trouvé.")
    else:
        for champ in interesant:
            if champ in films_trouves and films_trouves[champ]:
                resultats.insert(
                    "end",
                    f"{champ.replace('_', ' ').title()} : {films_trouves[champ]}\n\n"
                )

# -------- Bouton --------
button1 = ctk.CTkButton(
    frame,
    text="Rechercher",
    font=("Cambria", 14, "bold"),
    fg_color="#FF69B4",
    hover_color="#FF1493",
    text_color="#C8FACC",
    corner_radius=15,
    command=lancer_recherche
)
button1.grid(row=2, column=0, pady=10)

app.mainloop()

