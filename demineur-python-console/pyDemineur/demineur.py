import argparse
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pyDemineur.core.partie import Partie

if __name__ == "__main__":
    print("Lancement du démineur en mode console")
    print("Difficultée souhaitée ? 0 facile, 1 moyen, 2 difficle")
    try:
        difficulté = int(input())
        if difficulté == 0:
            partie = Partie(10, [8, 8])
        elif difficulté == 1:
            partie = Partie(40, [14, 14])
        elif difficulté == 2:
            partie = Partie(99, [20, 20])
        else:
            print("difficulté inconnue, facile par défaut")
            partie = Partie(10, [8, 8])
    except:
        print("difficulté inconnue, facile par défaut")
        partie = Partie(10, [8, 8])
    partie.jouer()