from case import Case


class Grille:
    
    def __init__(self, taille, nb_mines):
        self.taille = taille
        self.cases = [[Case() for _ in range(taille[1])] for _ in range(taille[0])]
        self.nb_mines = nb_mines

    def generer_grille(self):
        return #générer la grille avec les cases et placer les mines aléatoirement
    
    def placer_mines(self):
        return #placer les mines dans la grille
    
    def reveler_case(self):
        return #logique pour révéler une case
    
    def reveler_mines(self):
        return #revèle toutes les mines en cas de défaite


