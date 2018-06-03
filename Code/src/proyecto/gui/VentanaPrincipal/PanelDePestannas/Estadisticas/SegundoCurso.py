# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class SegundoCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(SegundoCurso, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_segundo()
        
    def semestres_segundo(self):
        """
        Método que establece en la interfaz gráfica las asignaturas del segundo curso
        introduciendo las asignaturas en la leyenda
        """
        self.segundo_frame = QtWidgets.QFrame()

        self.label_s_p_asig1 = QtWidgets.QLabel("A1: "+self.dicc.segundo_semestre1p_p_asig1, self)
        self.label_s_p_asig1.setToolTip('Pulsa para entrar')
        self.label_s_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig1.setFont(fontTex)  
        self.label_s_p_asig1.setWordWrap(True) 

       
        self.label_s_p_asig2 = QtWidgets.QLabel("A2: "+self.dicc.segundo_semestre1p_p_asig2, self)
        self.label_s_p_asig2.setToolTip('Pulsa para entrar')
        self.label_s_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig2.setFont(fontTex)
        self.label_s_p_asig2.setWordWrap(True) 
  
        self.label_s_p_asig3 = QtWidgets.QLabel("A3: "+self.dicc.segundo_semestre1p_p_asig3, self)
        self.label_s_p_asig3.setToolTip('Pulsa para entrar')
        self.label_s_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig3.setFont(fontTex) 
        self.label_s_p_asig3.setWordWrap(True) 
     

        self.label_s_p_asig4 = QtWidgets.QLabel("A4: "+self.dicc.segundo_semestre1p_p_asig4, self)
        self.label_s_p_asig4.setToolTip('Pulsa para entrar')
        self.label_s_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig4.setFont(fontTex) 
        self.label_s_p_asig4.setWordWrap(True) 
         
        
        self.label_s_p_asig5 = QtWidgets.QLabel("A5: "+self.dicc.segundo_semestre1p_p_asig5, self)
        self.label_s_p_asig5.setToolTip('Pulsa para entrar')
        self.label_s_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig5.setFont(fontTex)  
        self.label_s_p_asig5.setWordWrap(True)
    
        self.label_s_asig1 = QtWidgets.QLabel("A6: "+self.dicc.segundo_semestre2_s_asig1, self)
        self.label_s_asig1.setToolTip('Pulsa para entrar')
        self.label_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig1.setFont(fontTex)  
        self.label_s_asig1.setWordWrap(True)
         
       
        self.label_s_asig2 = QtWidgets.QLabel("A7: "+self.dicc.segundo_semestre2_s_asig2, self)
        self.label_s_asig2.setToolTip('Pulsa para entrar')
        self.label_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig2.setFont(fontTex)  
        self.label_s_asig2.setWordWrap(True)
         
      
        self.label_s_asig3 = QtWidgets.QLabel("A8: "+self.dicc.segundo_semestre2_s_asig3, self)
        self.label_s_asig3.setToolTip('Pulsa para entrar')
        self.label_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig3.setFont(fontTex)  
        self.label_s_asig3.setWordWrap(True)
         
      
        self.label_s_asig4 = QtWidgets.QLabel("A9: "+self.dicc.segundo_semestre2_s_asig4, self)
        self.label_s_asig4.setToolTip('Pulsa para entrar')
        self.label_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig4.setFont(fontTex)  
        self.label_s_asig4.setWordWrap(True)
     

        self.label_s_asig5 = QtWidgets.QLabel("A10: "+self.dicc.segundo_semestre2_s_asig5, self)
        self.label_s_asig5.setToolTip('Pulsa para entrar')
        self.label_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig5.setFont(fontTex)  
        self.label_s_asig5.setWordWrap(True)
     

        self.segundo_groupBox = QtWidgets.QVBoxLayout()
        self.segundo_groupBox.addWidget(self.label_s_p_asig1)         
        self.segundo_groupBox.addWidget(self.label_s_p_asig2)         
        self.segundo_groupBox.addWidget(self.label_s_p_asig3)         
        self.segundo_groupBox.addWidget(self.label_s_p_asig4)         
        self.segundo_groupBox.addWidget(self.label_s_p_asig5)         
        self.segundo_groupBox.addWidget(self.label_s_asig1)         
        self.segundo_groupBox.addWidget(self.label_s_asig2)         
        self.segundo_groupBox.addWidget(self.label_s_asig3)         
        self.segundo_groupBox.addWidget(self.label_s_asig4)         
        self.segundo_groupBox.addWidget(self.label_s_asig5)         


      
        self.segundo_layout = QtWidgets.QHBoxLayout()
        self.segundo_layout.addLayout(self.segundo_groupBox)         
      
        self.segundo_frame.setLayout(self.segundo_layout)
