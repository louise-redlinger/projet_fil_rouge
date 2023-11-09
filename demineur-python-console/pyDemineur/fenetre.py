import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)


# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = QWidget()


# titre de la fenêtre
fen.setWindowTitle("Démineur")


# la fenêtre est rendue visible
fen.show()

# exécution de l'application
app.exec_()
