from grille import Grille
from joueur import Joueur
from chrono import Chrono
import numpy as np

class Demineur:
    
    def __init__(self, niveau):
        self.niveau = niveau
        self.grille = Grille(niveau.taille_grille,niveau.nb_mines)
        self.joueur = Joueur("Nom du joueur")
        self.chrono = Chrono()
    
    def jouer(self):
        self.chrono.demarrer_chrono()
        self.grille.generer_grille()
        self.grille.placer_mines()
    
    def terminer_partie(self):
        self.chrono.arreter_chrono()
        temps_ecoule = self.chrono.obtenir_temps_ecoule()
        #affichage de fin de partie
        
    def verifier_victoire(self):
        return #true si on a trouvé toutes les mines
    
    def afficher_grille(self):
        for ligne in self.grille.cases:
            ligne_affichee = []
            for case in ligne:
                if case.est_revelee:
                    if case.est_minee:
                        ligne_affichee.append("*")
                    else:
                        ligne_affichee.append(str(case.nombre_de_mines_voisines))
                elif 
                        
                    
        
    def reveler_case(self, x, y):
        self.grille.reveler_case(x, y)
        #révélation de la case
    
    def changer_niveau(self, nv_niveau):
        
        self.niveau = nv_niveau
        self.grille = Grille(nv_niveau.taille_grille,nv_niveau.nombre_mines)
        
        
