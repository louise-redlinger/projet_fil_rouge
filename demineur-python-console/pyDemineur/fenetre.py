import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Démineur")
        
        # creation du premier bouton
        self.bouton1 = QPushButton("mon premier bouton dans un QVBoxLayout")
        # creation du deuxieme bouton
        self.bouton2 = QPushButton("mon deuxieme bouton dans un QVBoxLayout")
        
        # on connecte le signal "clicked" qui correspond au clic gauche a la methode appui_bouton
        self.bouton1.clicked.connect(self.appui_bouton)
        
        # on connecte le signal qui correspond au clic droit a la methode marquer_drapeau
        self.bouton1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.bouton1.customContextMenuRequested.connect(self.marquer_drapeau)
        
        self.bouton2.clicked.connect(self.appui_bouton)
 
        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout()
        # ajout du premier bouton au gestionnaire de mise en forme
        layout.addWidget(self.bouton1)
        # ajout du deuxieme bouton au gestionnaire de mise en forme
        layout.addWidget(self.bouton2)
        # on fixe le gestionnaire de mise en forme de la fenetre
        self.setLayout(layout)
        

        
        
    def appui_bouton(self):
        print("Découvrir")
        
    def marquer_drapeau(self):
        print("Marquer")


app = QApplication.instance() 

if not app:
    app = QApplication(sys.argv)


# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = Fenetre()


# la fenêtre est rendue visible
fen.show()

# exécution de l'application
app.exec_()
