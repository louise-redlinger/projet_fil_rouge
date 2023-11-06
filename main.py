from demineur import Demineur
from niveau import Niveau

if __name__ == "__main__":
    
    print("Bienvenue dans le super mega trop génial jeu Démineur!")
    
    niv = float(input("Voici les différents niveaux :\n1 : niveau Timide\n2 : niveau Curieux\n3 : niveau Aventureux\n4 : niveau Téméraire\n Quel niveau souhaitez vous tenter ?\n"))

    niveau = Niveau(niv)
    
    jeu = Demineur(niveau)
    
    while True:
        
        choix = input("1. Démarrer une nouvelle partie\n2. Je n'ai plus envie de jouer...\nVotre choix:")
        
        if choix == "1":
            jeu.jouer()
            print("Partie commencée, bon chance!")
            
            while not jeu.verifier_victoire():
                
                #Afficher la grille
                jeu.afficher_grille()
                
                #Demander quelle est la prochaine action
                action = input("Votre prochaine action (D pour marquer d'un drapeau, R pour révéler une case et Q pour Rage Quit)?")
                
                if action == "Q":
                    break
                
                elif action == "R":
                    x=int(input("Quelle ligne ?"))
                    y=int(input("Quelle colonne ?"))
                    jeu.reveler_case(x, y)
                    
        

