import csv
fichier = open("movies.csv","r",encoding="utf8")
table = list(csv.DictReader(fichier,delimiter=","))

def recherche(truc,categorie):
    """
    Parameters
    ----------
    truc : c'est ce que tu veux rechercher'
    categorie : c'est dans quoi yu veux le rechercher une categorie du tableau'

    Returns le nom de tout les film qui corespondant a l'unique rencherche'
    -------
    None.

    """
    bonfilm = []
    for i in range(len(table)):
        if table[i][categorie] == truc or truc in table[i][categorie]:
            bonfilm.append(table[i]["original_title"])
    return bonfilm
# exemple d'utilisation de la fonction 
# print(recherche("en","original_language"))
    
def rechercheFilm(film):
    """
    Parameters
    ----------
    film: nom du film rechercher

    Returns toutes les info du film rechercher
    -------
    None.

    """
    for i in range(len(table)):
        if film in table[i]["original_title"]:
            return table[i]
# exemple d'utilisation de la fonction
# print(rechercheFilm("Avatar"))
