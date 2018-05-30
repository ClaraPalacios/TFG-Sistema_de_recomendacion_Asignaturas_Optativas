# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Panel_de_pestannas import Panel_de_pestannas
# from proyecto.gui.VisorHtml import VisorHtml
# from proyecto.gui.Window import Window
class ValoracionesAsignaturas(QtWidgets.QMainWindow):

    def __init__(self,idioma_path, parent=None):
        super(ValoracionesAsignaturas, self).__init__(parent)
        self.dicc = Dicc()
        self.setWindowTitle(self.dicc.vn_proyecto)
        self.resize(1450, 700)

        #Show/hide frame 0=hide 1=show
        self.show_semestres=1;
        
        self.cerrar_all = QtWidgets.QAction(self.dicc.vn_salir, self)
        self.cerrar_all.setShortcut("ini_o_salir")
        self.cerrar_all.setStatusTip("ini_p_salir")
        self.cerrar_all.triggered.connect(self.cerrar)       
        

        ##Barratareas de arriba
        main_menu = self.menuBar()
        #menu1 barra de tareas
        self.file_menu = main_menu.addMenu(self.dicc.vn_opciones) 
        self.file_menu.addAction(self.cerrar_all)
        
        self.menuPrincipal()
#         self.cursos()
#         self.semestres()

        laout_principal = QtWidgets.QHBoxLayout()
#         laout_principal.addLayout(self.principal_layaout)
        laout_principal.addWidget(self.panel_de_pestannas)
 
#         laout_principal.addLayout(self.asignaturas_layout) 
#         laout_principal.addWidget(self.semestres_frame) 
        laout_principal.setAlignment(QtCore.Qt.AlignLeft)

        
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(laout_principal)
        self.setCentralWidget(central_widget)
        self.centerOnScreen()

    def menuPrincipal(self):

        self.panel_de_pestannas = Panel_de_pestannas(self)

        
    def centerOnScreen (self):
        '''centerOnScreen()
        Centers the window on the screen.
        '''
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
        
        


    def cerrar(self):
        """
        
        """   
        self.close()

        self.main = ValoracionesAsignaturas(os.getcwd())
        self.main.setWindowTitle(self.dicc.vn_proyecto)

        self.main.show()

