# les fonction sont finies n'y touchez surtout pas !!!!!!!!

import csv
fichier = open("movies.csv","r",encoding="utf8")
table = list(csv.DictReader(fichier,delimiter=","))
#print(table[0])
def recherche(truc,categorie):
    """
    Settings
    ----------
    truc : c'est ce que tu veux rechercher'
    categorie : c'est dans quoi tu veux le rechercher (une categorie du tableau)'

    Return le nom de tout les film qui corespondant a l'unique rencherche'
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
    Settings
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
<<<<<<< Updated upstream
#print(rechercheFilm("Avatar"))
=======
print(rechercheFilm("Avatar"))
>>>>>>> Stashed changes

def plusieursRecherches(list_de_recherche):
    """
    

    Parameters
    ----------
    list_de_recherche : doit etre sous forme liste de liste type a = [[truc,categorie][truc,categorie]...]
        DESCRIPTION.
        la fonction va faire les recherches et garder uniquement ce qui correspond a toutes les recherches

    Returns 
    une liste avec tout les nom des film qui correspondent aux multiples recherches

    """
    list_film = []
    final = []
    for i in list_de_recherche:
        list_film.append(recherche(i[0],i[1]))
<<<<<<< Updated upstream
    #la ligne suivante a ete recherché et sert a trouver tout les elements communs aux multiples listes
    elements_communs = list(set(list_film[0]).intersection(*list_film[1:]))
    return elements_communs
#exemple d'utilisation de la fonction
#print(plusieursRecherches([["en","original_language"],["Cru","cast"],["2015","release_date"]]))
=======
    for i in list_film:
        for k in i:
            if i == k:
                final.append(i)
            else:
                pass
    return final
# exemple d'utilisation de la fonction
print(plusieursRecherches([["en","original_language"],["trou du cul","director"]]))
>>>>>>> Stashed changes
