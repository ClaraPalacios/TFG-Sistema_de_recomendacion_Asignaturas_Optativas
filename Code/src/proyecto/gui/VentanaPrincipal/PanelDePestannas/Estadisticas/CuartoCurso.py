# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class CuartoCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(CuartoCurso, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_cuarto()
        
    def semestres_cuarto(self):
        """
        Método que establece en la interfaz gráfica las asignaturas del cuarto curso
        introduciendo las asignaturas en la leyenda
        """
        self.cuarto_frame = QtWidgets.QFrame()
        self.label_c_p_asig1 = QtWidgets.QLabel("A1: "+self.dicc.cuarto_semestre1p_p_asig1, self)
        self.label_c_p_asig1.setToolTip('Pulsa para entrar')
        self.label_c_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig1.setFont(fontTex)
        self.label_c_p_asig1.setWordWrap(True)  
     

        self.label_c_p_asig2 = QtWidgets.QLabel("A2: "+self.dicc.cuarto_semestre1p_p_asig2, self)
        self.label_c_p_asig2.setToolTip('Pulsa para entrar')
        self.label_c_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig2.setFont(fontTex)  
        self.label_c_p_asig2.setWordWrap(True)
         
      
        self.label_c_p_asig3 = QtWidgets.QLabel("A3: "+self.dicc.cuarto_semestre1p_p_asig3, self)
        self.label_c_p_asig3.setToolTip('Pulsa para entrar')
        self.label_c_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig3.setFont(fontTex)  
        self.label_c_p_asig3.setWordWrap(True)
       

        self.label_c_p_asig4 = QtWidgets.QLabel("A4: "+self.dicc.cuarto_semestre1p_p_asig4, self)
        self.label_c_p_asig4.setToolTip('Pulsa para entrar')
        self.label_c_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig4.setFont(fontTex) 
        self.label_c_p_asig4.setWordWrap(True) 
         
       
        
        self.label_c_p_asig5 = QtWidgets.QLabel("A5: "+self.dicc.cuarto_semestre1p_p_asig5, self)
        self.label_c_p_asig5.setToolTip('Pulsa para entrar')
        self.label_c_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig5.setFont(fontTex) 
        self.label_c_p_asig5.setWordWrap(True) 
       
        self.label_c_p_asig6 = QtWidgets.QLabel("A6: "+self.dicc.cuarto_semestre1p_p_asig6, self)
        self.label_c_p_asig6.setToolTip('Pulsa para entrar')
        self.label_c_p_asig6.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig6.setFont(fontTex) 
        self.label_c_p_asig6.setWordWrap(True) 
       
        
        
        self.label_c_p_asig7 = QtWidgets.QLabel("A7: "+self.dicc.cuarto_semestre1p_p_asig7, self)
        self.label_c_p_asig7.setToolTip('Pulsa para entrar')
        self.label_c_p_asig7.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig7.setFont(fontTex) 
        self.label_c_p_asig7.setWordWrap(True) 
       
        self.label_c_p_asig8 = QtWidgets.QLabel("A8: "+self.dicc.cuarto_semestre1p_p_asig8, self)
        self.label_c_p_asig8.setToolTip('Pulsa para entrar')
        self.label_c_p_asig8.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig8.setFont(fontTex) 
        self.label_c_p_asig8.setWordWrap(True) 
         
       
        
        self.label_c_p_asig9 = QtWidgets.QLabel("A9: "+self.dicc.cuarto_semestre1p_p_asig9, self)
        self.label_c_p_asig9.setToolTip('Pulsa para entrar')
        self.label_c_p_asig9.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig9.setFont(fontTex) 
        self.label_c_p_asig9.setWordWrap(True) 
         
       
        
        self.label_c_p_asig10 = QtWidgets.QLabel("A10: "+self.dicc.cuarto_semestre1p_p_asig10, self)
        self.label_c_p_asig10.setToolTip('Pulsa para entrar')
        self.label_c_p_asig10.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig10.setFont(fontTex) 
        self.label_c_p_asig10.setWordWrap(True) 
         
       
       
       
        self.label_c_asig1 = QtWidgets.QLabel("A11: "+self.dicc.cuarto_semestre2_s_asig1, self)
        self.label_c_asig1.setToolTip('Pulsa para entrar')
        self.label_c_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig1.setFont(fontTex)  
        self.label_c_asig1.setWordWrap(True)
       

        self.label_c_asig2 = QtWidgets.QLabel("A12: "+self.dicc.cuarto_semestre2_s_asig2, self)
        self.label_c_asig2.setToolTip('Pulsa para entrar')
        self.label_c_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig2.setFont(fontTex)
        self.label_c_asig2.setWordWrap(True)  
      
        self.label_c_asig3 = QtWidgets.QLabel("A13: "+self.dicc.cuarto_semestre2_s_asig3, self)
        self.label_c_asig3.setToolTip('Pulsa para entrar')
        self.label_c_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig3.setFont(fontTex)  
        self.label_c_asig3.setWordWrap(True)
         
       
        
        self.label_c_asig4 = QtWidgets.QLabel("A14: "+self.dicc.cuarto_semestre2_s_asig4, self)
        self.label_c_asig4.setToolTip('Pulsa para entrar')
        self.label_c_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig4.setFont(fontTex)  
        self.label_c_asig4.setWordWrap(True)
         
        
        self.label_c_asig5 = QtWidgets.QLabel("A15: "+self.dicc.cuarto_semestre2_s_asig5, self)
        self.label_c_asig5.setToolTip('Pulsa para entrar')
        self.label_c_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig5.setFont(fontTex)  
        self.label_c_asig5.setWordWrap(True)
         
       

        self.label_c_asig6 = QtWidgets.QLabel("A16: "+self.dicc.cuarto_semestre2_s_asig6, self)
        self.label_c_asig6.setToolTip('Pulsa para entrar')
        self.label_c_asig6.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_asig6.setFont(fontTex)  
        self.label_c_asig6.setWordWrap(True)

        self.cuarto_groupBox = QtWidgets.QVBoxLayout()
        self.cuarto_groupBox.addWidget(self.label_c_p_asig1)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig2)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig3)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig4)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig5) 
        self.cuarto_groupBox.addWidget(self.label_c_p_asig6)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig7)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig8)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig9)         
        self.cuarto_groupBox.addWidget(self.label_c_p_asig10)
        self.cuarto_groupBox.addWidget(self.label_c_asig1)         
        self.cuarto_groupBox.addWidget(self.label_c_asig2)         
        self.cuarto_groupBox.addWidget(self.label_c_asig3)         
        self.cuarto_groupBox.addWidget(self.label_c_asig4)         
        self.cuarto_groupBox.addWidget(self.label_c_asig5)         
        self.cuarto_groupBox.addWidget(self.label_c_asig6)         


      
        self.cuarto_layout = QtWidgets.QHBoxLayout()
        self.cuarto_layout.addLayout(self.cuarto_groupBox)         
      
        self.cuarto_frame.setLayout(self.cuarto_layout)