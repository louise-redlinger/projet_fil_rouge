from case import Case
import random

class Grille:
    
    def __init__(self, taille, nb_mines):
        self.taille = taille
        self.cases = [[Case() for _ in range(taille[1])] for _ in range(taille[0])]
        self.nb_mines = nb_mines

    def generer_grille(self):
        
        #Initialisation de la grille
        for ligne in self.cases:
            for case in ligne:
                case.est_minee = False
        
        #Placer les mines aléatoirement
        mines_places = 0
        while mines_places < self.nb_mines:
            x = random.randint(0,self.taille[0]-1)
            y = random.randint(0,self.taille[1]-1)
            case = self.cases[x][y]
            
            if not case.est_minee:
                case.est_minee = True
                mines_places+=1
        
        voisins_indices = [
                    (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x, y - 1),                     (x, y + 1),
                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
                ]
        
        #Calcul du nombre de voisins
        for i in self.cases:
            for j in i:
                
                case = self.cases[i][j]
                
                voisins_indices = [
                            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                            (i, j - 1),                     (i, j + 1),
                            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                        ]
                
                # Filtrer les indices pour les voisins valides dans la grille
                voisins_valides = [(x, y) for x, y in voisins_indices if 0 <= x < self.taille[0] and 0 <= y < self.taille[1]]

                # Attribuer les cases valides à la liste des voisins de la case actuelle
                case.voisins = [self.cases[x][y] for x, y in voisins_valides]
                
                for voisin in case.voisins :
                    
                    if voisin.est_minee :
                        
                        case.nb_mines_voisines += 1
                    
    
    def reveler_case(self):
        return #logique pour révéler une case
    
    def reveler_mines(self):
        return #revèle toutes les mines en cas de défaite


