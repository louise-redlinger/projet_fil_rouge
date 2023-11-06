class Case:
    
    def __init__(self):
        self.est_minee = False
        self.est_revelee = False
        self.nb_mines_voisines = 0
        self.voisins = []
    
    def reveler(self):
        self.est_revelee = True
        