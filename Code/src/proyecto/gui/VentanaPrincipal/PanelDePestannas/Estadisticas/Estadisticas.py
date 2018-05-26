from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui



class Estadisticas(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Estadisticas, self).__init__(parent)
        self.dicc = Dicc()
        self.tab3UI()
        
    def tab3UI(self):
    #         Button : Entrar y salir
        self.graficas = QtWidgets.QPushButton(self.dicc.graficas, self)
        self.graficas.setToolTip('Pulsa para entrar')
        self.graficas.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.graficas.setFont(fontTex)
        
        self.pestanna3 = QtWidgets.QVBoxLayout()
        self.pestanna3.addWidget(self.graficas)
