class Chrono:
    
    def __init__(self):
        self.temps_debut = None
        self.temps_fin = None
        
    def demarrer_chrono(self):
        import time
        self.temps_debut = time.time()
        
    def arreter_chrono(self):
        import time
        self.temps_fin = time.time()
    
    def obtenir_temps_ecoule(self):
        if self.temps_debut is None or self.temps_fin is None:
            return 0
        return self.temps_fin - self.temps_début
    