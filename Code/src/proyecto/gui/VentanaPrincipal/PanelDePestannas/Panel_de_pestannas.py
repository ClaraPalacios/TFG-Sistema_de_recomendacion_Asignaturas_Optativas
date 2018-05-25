from PyQt5 import QtWidgets
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Estadisticas.Estadisticas import Estadisticas
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Modelos.Modelos import Modelos
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Asignaturas.Asignaturas import Asignaturas

class Panel_de_pestannas(QtWidgets.QTabWidget):
           
    def __init__(self, parent = None):
        super(Panel_de_pestannas, self).__init__(parent)
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
          
        self.addTab(self.tab1,"Valoraciones")
        self.addTab(self.tab2,"Modelos")
        self.addTab(self.tab3,"Estadisticas")
        
        self.pest1= Asignaturas()
        self.tab1.setLayout(self.pest1.pestanna1_layout) 
        
        self.pest2= Modelos()
        self.tab2.setLayout(self.pest2.pestanna2)
        
        self.pest3= Estadisticas()
        self.tab3.setLayout(self.pest3.pestanna3)
