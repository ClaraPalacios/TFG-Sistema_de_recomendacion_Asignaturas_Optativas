# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class TerceroCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(TerceroCurso, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_tercero()
        
    def semestres_tercero(self):
        """
        Método que establece en la interfaz gráfica las asignaturas del tercer curso
        introduciendo las asignaturas en la leyenda
        """
        self.tercero_frame = QtWidgets.QFrame()

        
        self.label_t_p_asig1 = QtWidgets.QLabel("A1: "+self.dicc.tercero_semestre1p_p_asig1, self)
        self.label_t_p_asig1.setToolTip('Pulsa para entrar')
        self.label_t_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig1.setFont(fontTex)  
        self.label_t_p_asig1.setWordWrap(True)
       

        self.label_t_p_asig2 = QtWidgets.QLabel("A2: "+self.dicc.tercero_semestre1p_p_asig2, self)
        self.label_t_p_asig2.setToolTip('Pulsa para entrar')
        self.label_t_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig2.setFont(fontTex)  
        self.label_t_p_asig2.setWordWrap(True)
       
        
        self.label_t_p_asig3 = QtWidgets.QLabel("A3: "+self.dicc.tercero_semestre1p_p_asig3, self)
        self.label_t_p_asig3.setToolTip('Pulsa para entrar')
        self.label_t_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig3.setFont(fontTex)  
        self.label_t_p_asig3.setWordWrap(True)
       

        self.label_t_p_asig4 = QtWidgets.QLabel("A4: "+self.dicc.tercero_semestre1p_p_asig4, self)
        self.label_t_p_asig4.setToolTip('Pulsa para entrar')
        self.label_t_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig4.setFont(fontTex)  
        self.label_t_p_asig4.setWordWrap(True)
         
       
        self.label_t_p_asig5 = QtWidgets.QLabel("A5: "+self.dicc.tercero_semestre1p_p_asig5, self)
        self.label_t_p_asig5.setToolTip('Pulsa para entrar')
        self.label_t_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig5.setFont(fontTex)  
        self.label_t_p_asig5.setWordWrap(True)
       
        
        self.label_t_asig1 = QtWidgets.QLabel("A6: "+self.dicc.tercero_semestre2_s_asig1, self)
        self.label_t_asig1.setToolTip('Pulsa para entrar')
        self.label_t_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig1.setFont(fontTex)
        self.label_t_asig1.setWordWrap(True)
  

        self.label_t_asig2 = QtWidgets.QLabel("A7: "+self.dicc.tercero_semestre2_s_asig2, self)
        self.label_t_asig2.setToolTip('Pulsa para entrar')
        self.label_t_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig2.setFont(fontTex)  
        self.label_t_asig2.setWordWrap(True)
     
        
        self.label_t_asig3 = QtWidgets.QLabel("A8: "+self.dicc.tercero_semestre2_s_asig3, self)
        self.label_t_asig3.setToolTip('Pulsa para entrar')
        self.label_t_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig3.setFont(fontTex)
        self.label_t_asig3.setWordWrap(True)  

        
        self.label_t_asig4 = QtWidgets.QLabel("A9: "+self.dicc.tercero_semestre2_s_asig4, self)
        self.label_t_asig4.setToolTip('Pulsa para entrar')
        self.label_t_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig4.setFont(fontTex)  
        self.label_t_asig4.setWordWrap(True)
      
        
        self.label_t_asig5 = QtWidgets.QLabel("A10: "+self.dicc.tercero_semestre2_s_asig5, self)
        self.label_t_asig5.setToolTip('Pulsa para entrar')
        self.label_t_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig5.setFont(fontTex)  
        self.label_t_asig5.setWordWrap(True)
        
        self.tercero_groupBox = QtWidgets.QVBoxLayout()
        self.tercero_groupBox.addWidget(self.label_t_p_asig1)         
        self.tercero_groupBox.addWidget(self.label_t_p_asig2)         
        self.tercero_groupBox.addWidget(self.label_t_p_asig3)         
        self.tercero_groupBox.addWidget(self.label_t_p_asig4)         
        self.tercero_groupBox.addWidget(self.label_t_p_asig5)         
        self.tercero_groupBox.addWidget(self.label_t_asig1)         
        self.tercero_groupBox.addWidget(self.label_t_asig2)         
        self.tercero_groupBox.addWidget(self.label_t_asig3)         
        self.tercero_groupBox.addWidget(self.label_t_asig4)         
        self.tercero_groupBox.addWidget(self.label_t_asig5)         


      
        self.tercero_layout = QtWidgets.QHBoxLayout()
        self.tercero_layout.addLayout(self.tercero_groupBox)         
      
        self.tercero_frame.setLayout(self.tercero_layout)