# -*- coding: latin1 -*-
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from proyecto.dicc.Dicc import Dicc
import requests

# from proyecto.gui.VisorHtml import VisorHtml
# from proyecto.gui.Window import Window
class Registrar(QtWidgets.QMainWindow):

    def __init__(self,idioma_path, parent=None):
        super(Registrar, self).__init__(parent)
        self.dicc = Dicc()
        self.resize(800, 300)
        self.setWindowTitle(self.dicc.registrar)
        
        self.cerrar_all = QtWidgets.QAction("salir", self)
        self.cerrar_all.setShortcut("ini_o_salir")
        self.cerrar_all.setStatusTip("ini_p_salir")
        self.cerrar_all.triggered.connect(self.cerrar)       
        
        ##Barratareas de arriba
        main_menu = self.menuBar()
        #menu1 barra de tareas
        self.file_menu = main_menu.addMenu(self.dicc.vn_opciones) 
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
        self.user_M = QtWidgets.QLabel(self.dicc.usuario, self)
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
        
        self.password_M = QtWidgets.QLabel(self.dicc.contraseña, self)
        self.password_M.setAlignment(QtCore.Qt.AlignLeft)
        self.password_M.setStyleSheet('color: red')
        font = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.password_M.setFont(font)
        
        self.passwordTexArea = QtWidgets.QLineEdit(self)
        self.passwordTexArea.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordTexArea.setAlignment(QtCore.Qt.AlignRight)
        self.passwordTexArea.setStyleSheet('color: black')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.passwordTexArea.setFont(fontTex)
        
        #         email: texbox
        
        self.email_M = QtWidgets.QLabel(self.dicc.email, self)
        self.email_M.setAlignment(QtCore.Qt.AlignLeft)
        self.email_M.setStyleSheet('color: red')
        font = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.email_M.setFont(font)
        
        self.emailTexArea = QtWidgets.QLineEdit(self)
        self.emailTexArea.setAlignment(QtCore.Qt.AlignRight)
        self.emailTexArea.setStyleSheet('color: black')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.emailTexArea.setFont(fontTex)        

        
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
        
       
        #layouthorizontal for email label and data.
        self.email_layout = QtWidgets.QHBoxLayout()
        self.email_layout.addStretch(1)  
        self.email_layout.addWidget(self.email_M)  
        self.email_layout.addWidget(self.emailTexArea) 
        self.email_layout.addStretch(1)       
        self.email_layout.setAlignment(QtCore.Qt.AlignLeft)        
        
        #         Button : Entrar y salir
        self.entrar_B = QtWidgets.QPushButton(self.dicc.registr, self)
        self.entrar_B.setToolTip('Pulsa para entrar')
        self.entrar_B.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.entrar_B.setFont(fontTex)
         
        
        self.salir_B = QtWidgets.QPushButton(self.dicc.salir_reg, self)
        self.salir_B.setStyleSheet('color: black; ')
        self.salir_B.setToolTip('Pulsa para entrar')
        fontTex = QtGui.QFont("ini_time", 35, QtGui.QFont.Bold, True)
        self.salir_B.setFont(fontTex)
        
        self.salir_B.clicked.connect(self.cerrar)
        self.entrar_B.clicked.connect(self.registro)


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
        self.Loggin_layout.addLayout(self.email_layout)    
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
    
    
    def registro(self):
        usuario=self.User_TexArea.text()
        email=self.emailTexArea.text()
        password= self.passwordTexArea.text()
        rol="Usuario"
        ##/User_Add   Añadir un usuario
        r = requests.post("http://claratfg2.pythonanywhere.com/User_Add",json={
          "email": email,
          "password": password,
          "rol": rol,
          "username": usuario
        })
        if r.json()==True:            
            self.showdialog(self.dicc.creado_exito)
            self.close()

        else:
            self.showdialog(self.dicc.usuario_existente)

        
    def cerrar(self):
  
        self.close()

    def showdialog(self,i):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        msg.setText(self.dicc.val_registro)
        msg.setInformativeText(str(i))
        msg.setWindowTitle(self.dicc.val_registro_estado)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
         
        msg.exec_()
