# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class PrimeroCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(PrimeroCurso, self).__init__(parent)
        self.dicc = Dicc()

        self.semestres_primero()
        
    def semestres_primero(self):
        """
        Método que establece en la interfaz gráfica las asignaturas del primer curso
        introduciendo las asignaturas en la leyenda
        """
        self.primero_frame = QtWidgets.QFrame()

        #         Button : Entrar y salir
        
        self.labelp_p_asig1 = QtWidgets.QLabel("A1: "+self.dicc.primero_semestre1p_p_asig1, self)
        self.labelp_p_asig1.setToolTip('Pulsa para entrar')
        self.labelp_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.labelp_p_asig1.setFont(fontTex)  
        self.labelp_p_asig1.setWordWrap(True) 


        
        self.labelp_p_asig2 = QtWidgets.QLabel("A2: "+self.dicc.primero_semestre1p_p_asig2, self)
        self.labelp_p_asig2.setToolTip('Pulsa para entrar')
        self.labelp_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.labelp_p_asig2.setFont(fontTex)  
        self.labelp_p_asig2.setWordWrap(True) 

        
        
        self.labelp_p_asig3 = QtWidgets.QLabel("A3: "+self.dicc.primero_semestre1p_p_asig3, self)
        self.labelp_p_asig3.setToolTip('Pulsa para entrar')
        self.labelp_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.labelp_p_asig3.setFont(fontTex)  
        self.labelp_p_asig3.setWordWrap(True) 

        
        
        self.labelp_p_asig4 = QtWidgets.QLabel("A4: "+self.dicc.primero_semestre1p_p_asig4, self)
        self.labelp_p_asig4.setToolTip('Pulsa para entrar')
        self.labelp_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.labelp_p_asig4.setFont(fontTex)  
        self.labelp_p_asig4.setWordWrap(True) 

       
        self.labelp_p_asig5 = QtWidgets.QLabel("A5: "+self.dicc.primero_semestre1p_p_asig5, self)
        self.labelp_p_asig5.setToolTip('Pulsa para entrar')
        self.labelp_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.labelp_p_asig5.setFont(fontTex)  
        self.labelp_p_asig5.setWordWrap(True) 

    
        self.label_s_asig1 = QtWidgets.QLabel("A6: "+self.dicc.primero_semestre2_s_asig1, self)
        self.label_s_asig1.setToolTip('Pulsa para entrar')
        self.label_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig1.setFont(fontTex)  
        self.label_s_asig1.setWordWrap(True) 

   
        

        self.label_s_asig2 = QtWidgets.QLabel("A7: "+self.dicc.primero_semestre2_s_asig2, self)
        self.label_s_asig2.setToolTip('Pulsa para entrar')
        self.label_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig2.setFont(fontTex)  
        self.label_s_asig2.setWordWrap(True) 
                      
      
        
        self.label_s_asig3 = QtWidgets.QLabel("A8: "+self.dicc.primero_semestre2_s_asig3, self)
        self.label_s_asig3.setToolTip('Pulsa para entrar')
        self.label_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig3.setFont(fontTex)  
        self.label_s_asig3.setWordWrap(True) 
         
       
        
        self.label_s_asig4 = QtWidgets.QLabel("A9: "+self.dicc.primero_semestre2_s_asig4, self)
        self.label_s_asig4.setToolTip('Pulsa para entrar')
        self.label_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig4.setFont(fontTex)  
        self.label_s_asig4.setWordWrap(True) 
        
        
        self.label_s_asig5 = QtWidgets.QLabel("A10: "+self.dicc.primero_semestre2_s_asig5, self)
        self.label_s_asig5.setToolTip('Pulsa para entrar')
        self.label_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig5.setFont(fontTex)  
        self.label_s_asig5.setWordWrap(True) 
      
      
      
        self.primero_groupBox = QtWidgets.QVBoxLayout()
        self.primero_groupBox.addWidget(self.labelp_p_asig1)         
        self.primero_groupBox.addWidget(self.labelp_p_asig2)         
        self.primero_groupBox.addWidget(self.labelp_p_asig3)         
        self.primero_groupBox.addWidget(self.labelp_p_asig4)         
        self.primero_groupBox.addWidget(self.labelp_p_asig5)         
        self.primero_groupBox.addWidget(self.label_s_asig1)         
        self.primero_groupBox.addWidget(self.label_s_asig2)         
        self.primero_groupBox.addWidget(self.label_s_asig3)         
        self.primero_groupBox.addWidget(self.label_s_asig4)         
        self.primero_groupBox.addWidget(self.label_s_asig5)         


      
        self.primero_layout = QtWidgets.QHBoxLayout()
        self.primero_layout.addLayout(self.primero_groupBox)         
      
        self.primero_frame.setLayout(self.primero_layout)
