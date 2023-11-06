import pandas as pd

niveaux = pd.read_csv("niveaux.csv",delimiter=';',header=0)

class Niveau:
    
    def __init__(self, niv):
        self.nom = niveaux.loc[niv-1,"nom"]
        self.taille_grille = [niveaux.loc[niv-1,"nb_ligne"],niveaux.loc[niv-1,"nb_colonne"]]
        self.nb_mines = niveaux.loc[niv-1,"nb_mines"]
        

    
    
        

