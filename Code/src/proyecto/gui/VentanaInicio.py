# -*- coding: latin1 -*-
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import os
# from proyecto.gui.VisorHtml import VisorHtml
# from proyecto.gui.Window import Window
class VentanaInicio(QtWidgets.QMainWindow):

    def __init__(self,idioma_path, parent=None):
        super(VentanaInicio, self).__init__(parent)

        self.resize(800, 300)
        self.setWindowTitle("TFG CLARA")

      
        
        self.cerrar_all = QtWidgets.QAction("salir", self)
        self.cerrar_all.setShortcut("ini_o_salir")
        self.cerrar_all.setStatusTip("ini_p_salir")
        self.cerrar_all.triggered.connect(self.cerrar)       
        

        ##Barratareas de arriba
        main_menu = self.menuBar()
        #menu1 barra de tareas
        self.file_menu = main_menu.addMenu("Opciones") 
        self.file_menu.addAction(self.cerrar_all)
        
        self.inicioSesion()

        laout_principal = QtWidgets.QVBoxLayout()
        laout_principal.addLayout(self.Loggin_layout)        
        laout_principal.setAlignment(QtCore.Qt.AlignLeft)

        
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(laout_principal)
        self.setCentralWidget(central_widget)
    def inicioSesion(self):
        
#         usuario: texbox
        self.user_M = QtWidgets.QLabel("Usuario             ", self)
        self.user_M.setAlignment(QtCore.Qt.AlignLeft)
        self.user_M.setStyleSheet('color: red')
        font = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.user_M.setFont(font)
        
        self.User_TexArea = QtWidgets.QLineEdit(self)
        self.User_TexArea.setAlignment(QtCore.Qt.AlignRight)
        self.User_TexArea.setStyleSheet('color: black')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.User_TexArea.setFont(fontTex)
        
        #         Password: texbox
        
        self.password_M = QtWidgets.QLabel("Contraseña       ", self)
        self.password_M.setAlignment(QtCore.Qt.AlignLeft)
        self.password_M.setStyleSheet('color: red')
        font = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.password_M.setFont(font)
        
#         self.register_m = QtWidgets.QLabel("Nuevo usuario  ", self)
#         self.register_m.setAlignment(QtCore.Qt.AlignLeft)
#         self.register_m.setStyleSheet('color: blue')
#         font = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
#         self.register_m.setFont(font)
        
        self.register_b = QtWidgets.QLabel("Registrarse  ", self)
        self.register_b.setAlignment(QtCore.Qt.AlignCenter)
        self.clickables(self.register_b).connect(self.cerrar)
        self.register_b.setStyleSheet('color: blue')
        font = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.register_b.setFont(font)
        
        self.passwordTexArea = QtWidgets.QLineEdit(self)
        self.passwordTexArea.setAlignment(QtCore.Qt.AlignRight)
        self.passwordTexArea.setStyleSheet('color: black')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.passwordTexArea.setFont(fontTex)
        
        #layouthorizontal for user label and data.        
        self.User_layout = QtWidgets.QHBoxLayout()
        self.User_layout.addStretch(1)  
        self.User_layout.addWidget(self.user_M)        
        self.User_layout.addWidget(self.User_TexArea)  
        self.User_layout.addStretch(1) 
        self.User_layout.setAlignment(QtCore.Qt.AlignLeft)
        
        #layouthorizontal for user label and data.
        self.Password_layout = QtWidgets.QHBoxLayout()
        self.Password_layout.addStretch(1)  
        self.Password_layout.addWidget(self.password_M)        
        self.Password_layout.addWidget(self.passwordTexArea) 
        self.Password_layout.addStretch(1)       
        self.Password_layout.setAlignment(QtCore.Qt.AlignLeft)
        
       
        #layouthorizontal for user label and data.
        self.register_layaot = QtWidgets.QHBoxLayout()
        self.register_layaot.addStretch(1) 
        self.register_layaot.addWidget(self.register_b)     
        self.register_layaot.addStretch(1) 
        self.register_layaot.setAlignment(QtCore.Qt.AlignLeft)
        
        
        #         Button : Entrar y salir
        self.entrar_B = QtWidgets.QPushButton(" Entrar  ", self)
        self.entrar_B.setToolTip('Pulsa para entrar')
        self.entrar_B.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.entrar_B.setFont(fontTex)
         
        
        self.salir_B = QtWidgets.QPushButton(" Salir  ", self)
        self.salir_B.setStyleSheet('color: black; ')
        self.salir_B.setToolTip('Pulsa para entrar')
        fontTex = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.salir_B.setFont(fontTex)
        
        self.salir_B.clicked.connect(self.cerrar)
        self.entrar_B.clicked.connect(self.cerrar)


        #layout for buttons
        self.Butons_layout = QtWidgets.QHBoxLayout()
        self.Butons_layout.addStretch(1) 
        self.Butons_layout.addWidget(self.entrar_B)   
        self.Butons_layout.addStretch(1) 
        self.Butons_layout.addWidget(self.salir_B)     
        self.Butons_layout.addStretch(1) 
   
        self.Butons_layout.setAlignment(QtCore.Qt.AlignLeft)
        
        
        self.Loggin_layout = QtWidgets.QVBoxLayout()
        self.Loggin_layout.addLayout(self.User_layout)        
        self.Loggin_layout.addLayout(self.Password_layout)    
        self.Loggin_layout.addLayout(self.register_layaot)               
        self.Loggin_layout.addLayout(self.Butons_layout)        
        self.Loggin_layout.setAlignment(QtCore.Qt.AlignLeft)

        
    def clickables(self,widget):
        """
        Metodo que habilita a la pantalla de inicio a dar funcionalidad
        a los labels que nos indican abrir o cargar proyectos.
        """

        class Filter(QtCore.QObject):
        
            clicked = QtCore.pyqtSignal()
            
            def eventFilter(self, obj, event):
            
                if obj == widget and event.type() == QtCore.QEvent.MouseButtonRelease and obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True
                
                return False
        
        filters = Filter(widget)
        widget.installEventFilter(filters)
        return filters.clicked    
    
    def cerrar(self):
        """
        
        """   

        app = QtWidgets.QApplication(sys.argv)
        print(os.getcwd())
        main = self.VentanaInicio(os.getcwd())
        main.show()
        sys.exit(app.exec_())

