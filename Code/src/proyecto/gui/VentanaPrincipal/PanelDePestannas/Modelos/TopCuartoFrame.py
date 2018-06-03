# -*- coding: latin1 -*-
from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure

class TopCuartoFrame(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(TopCuartoFrame, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_top_cuarto()
        
    def semestres_top_cuarto(self):
        """
        Método que pinta el top pinta las asignaturas del top 10 de las asignaturas
        del cuarto curso, así como los valores de las mismas. 
        """
        
        self.top_cuarto_semestres_frame = QtWidgets.QFrame()

        #         Button : Entrar y salir
        self.top_cuarto_semestre1_vert = QtWidgets.QVBoxLayout()
        self.top_cuarto_semestre1 = QtWidgets.QLabel(self.dicc.top_asignaturas1, self)
        self.top_cuarto_semestre1.setToolTip('Pulsa para entrar')
        self.top_cuarto_semestre1.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.top_cuarto_semestre1.setFont(fontTex)
        self.top_cuarto_semestre1.setAlignment( QtCore.Qt.AlignHCenter)
        
        self.label_top_c_p_asig1 = QtWidgets.QLabel("c_p_asig1", self)
        self.label_top_c_p_asig1.setToolTip('Pulsa para entrar')
        self.label_top_c_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_p_asig1.setFont(fontTex)  
        self.label_top_c_p_asig1.setWordWrap(True) 
         

        self.label_value_top_c_p_asig1 = QtWidgets.QLabel(str(3), self)
        self.label_value_top_c_p_asig1.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_p_asig1.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_p_asig1.setFont(fontTex)  
        
        self.top_cuarto_semestre1p_p_asig1 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre1p_p_asig1.addWidget(self.label_top_c_p_asig1)
        self.top_cuarto_semestre1p_p_asig1.addWidget(self.label_value_top_c_p_asig1)

        self.label_top_c_p_asig2 = QtWidgets.QLabel("c_p_asig2", self)
        self.label_top_c_p_asig2.setToolTip('Pulsa para entrar')
        self.label_top_c_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_p_asig2.setFont(fontTex)  
        self.label_top_c_p_asig2.setWordWrap(True) 

         
        self.label_value_top_c_p_asig2 = QtWidgets.QLabel(str(3), self)
        self.label_value_top_c_p_asig2.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_p_asig2.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_p_asig2.setFont(fontTex) 
        
        self.top_cuarto_semestre1p_p_asig2 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre1p_p_asig2.addWidget(self.label_top_c_p_asig2)
        self.top_cuarto_semestre1p_p_asig2.addWidget(self.label_value_top_c_p_asig2)
        
        self.label_top_c_p_asig3 = QtWidgets.QLabel("c_p_asig3", self)
        self.label_top_c_p_asig3.setToolTip('Pulsa para entrar')
        self.label_top_c_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_p_asig3.setFont(fontTex)  
        self.label_top_c_p_asig3.setWordWrap(True) 


        self.label_value_top_c_p_asig3 = QtWidgets.QLabel(str(3), self)
        self.label_value_top_c_p_asig3.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_p_asig3.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_p_asig3.setFont(fontTex)   
                           
        self.top_cuarto_semestre1p_p_asig3 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre1p_p_asig3.addWidget(self.label_top_c_p_asig3)
        self.top_cuarto_semestre1p_p_asig3.addWidget(self.label_value_top_c_p_asig3)

        self.label_top_c_p_asig4 = QtWidgets.QLabel("c_p_asig4", self)
        self.label_top_c_p_asig4.setToolTip('Pulsa para entrar')
        self.label_top_c_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_p_asig4.setFont(fontTex)  
        self.label_top_c_p_asig4.setWordWrap(True) 

        self.label_value_top_c_p_asig4 = QtWidgets.QLabel(str(3), self)
        self.label_value_top_c_p_asig4.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_p_asig4.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_p_asig4.setFont(fontTex)   
                            
        self.top_cuarto_semestre1p_p_asig4 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre1p_p_asig4.addWidget(self.label_top_c_p_asig4)
        self.top_cuarto_semestre1p_p_asig4.addWidget(self.label_value_top_c_p_asig4)
        
        self.label_top_c_p_asig5 = QtWidgets.QLabel("c_p_asig5", self)
        self.label_top_c_p_asig5.setToolTip('Pulsa para entrar')
        self.label_top_c_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_p_asig5.setFont(fontTex)  
        self.label_top_c_p_asig5.setWordWrap(True) 


        self.label_value_top_c_p_asig5 = QtWidgets.QLabel(str(3), self)
        self.label_value_top_c_p_asig5.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_p_asig5.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_p_asig5.setFont(fontTex)  

        self.top_cuarto_semestre1p_p_asig5 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre1p_p_asig5.addWidget(self.label_top_c_p_asig5)
        self.top_cuarto_semestre1p_p_asig5.addWidget(self.label_value_top_c_p_asig5)

        self.top_cuarto_semestre1_vert.addWidget(self.top_cuarto_semestre1)
        self.top_cuarto_semestre1_vert.addStretch(1.3)  
        self.top_cuarto_semestre1_vert.addLayout(self.top_cuarto_semestre1p_p_asig1)
        self.top_cuarto_semestre1_vert.addStretch(1)        
        self.top_cuarto_semestre1_vert.addLayout(self.top_cuarto_semestre1p_p_asig2)
        self.top_cuarto_semestre1_vert.addStretch(1)        
        self.top_cuarto_semestre1_vert.addLayout(self.top_cuarto_semestre1p_p_asig3)
        self.top_cuarto_semestre1_vert.addStretch(1)        
        self.top_cuarto_semestre1_vert.addLayout(self.top_cuarto_semestre1p_p_asig4)
        self.top_cuarto_semestre1_vert.addStretch(1)        
        self.top_cuarto_semestre1_vert.addLayout(self.top_cuarto_semestre1p_p_asig5)
        self.top_cuarto_semestre1_vert.addStretch(1)        


        #         Button : Entrar y salir
        self.top_cuarto_semestre2_vert = QtWidgets.QVBoxLayout()
        self.top_cuarto_semestre2 = QtWidgets.QLabel(self.dicc.top_asignaturas2, self)
        self.top_cuarto_semestre2.setToolTip('Pulsa para entrar')
        self.top_cuarto_semestre2.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.top_cuarto_semestre2.setFont(fontTex)
        self.top_cuarto_semestre2.setAlignment( QtCore.Qt.AlignHCenter)
        
        self.label_top_c_asig1 = QtWidgets.QLabel("c_s_asig1", self)
        self.label_top_c_asig1.setToolTip('Pulsa para entrar')
        self.label_top_c_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_asig1.setFont(fontTex)  
        self.label_top_c_asig1.setWordWrap(True) 
         
        self.label_value_top_c_s_asig1 = QtWidgets.QLabel(str(4), self)
        self.label_value_top_c_s_asig1.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_s_asig1.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_s_asig1.setFont(fontTex)                    
                    
        self.top_cuarto_semestre2_s_asig1 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre2_s_asig1.addWidget(self.label_top_c_asig1)
        self.top_cuarto_semestre2_s_asig1.addWidget(self.label_value_top_c_s_asig1)

        self.label_top_c_asig2 = QtWidgets.QLabel("c_s_asig2", self)
        self.label_top_c_asig2.setToolTip('Pulsa para entrar')
        self.label_top_c_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_asig2.setFont(fontTex)  
        self.label_top_c_asig2.setWordWrap(True) 

        self.label_value_top_c_s_asig2 = QtWidgets.QLabel(str(4), self)
        self.label_value_top_c_s_asig2.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_s_asig2.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_s_asig2.setFont(fontTex) 
                            
        self.top_cuarto_semestre2_s_asig2 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre2_s_asig2.addWidget(self.label_top_c_asig2)
        self.top_cuarto_semestre2_s_asig2.addWidget(self.label_value_top_c_s_asig2)
        
        self.label_top_c_asig3 = QtWidgets.QLabel("c_s_asig3", self)
        self.label_top_c_asig3.setToolTip('Pulsa para entrar')
        self.label_top_c_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_asig3.setFont(fontTex)  
        self.label_top_c_asig3.setWordWrap(True) 

        self.label_value_top_c_s_asig3 = QtWidgets.QLabel(str(4), self)
        self.label_value_top_c_s_asig3.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_s_asig3.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_s_asig3.setFont(fontTex) 
                            
        self.top_cuarto_semestre2_s_asig3 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre2_s_asig3.addWidget(self.label_top_c_asig3)
        self.top_cuarto_semestre2_s_asig3.addWidget(self.label_value_top_c_s_asig3)
        
        self.label_top_c_asig4 = QtWidgets.QLabel("c_s_asig4", self)
        self.label_top_c_asig4.setToolTip('Pulsa para entrar')
        self.label_top_c_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_asig4.setFont(fontTex)  
        self.label_top_c_asig4.setWordWrap(True) 


        self.label_value_top_c_s_asig4 = QtWidgets.QLabel(str(4), self)
        self.label_value_top_c_s_asig4.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_s_asig4.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_s_asig4.setFont(fontTex)  
                           
        self.top_cuarto_semestre2_s_asig4 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre2_s_asig4.addWidget(self.label_top_c_asig4)
        self.top_cuarto_semestre2_s_asig4.addWidget(self.label_value_top_c_s_asig4)
        
        self.label_top_c_asig5 = QtWidgets.QLabel("c_s_asig5", self)
        self.label_top_c_asig5.setToolTip('Pulsa para entrar')
        self.label_top_c_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_top_c_asig5.setFont(fontTex)  
        self.label_top_c_asig5.setWordWrap(True) 

        self.label_value_top_c_s_asig5 = QtWidgets.QLabel(str(4), self)
        self.label_value_top_c_s_asig5.setAlignment(QtCore.Qt.AlignRight)
        self.label_value_top_c_s_asig5.setStyleSheet('color: green; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_top_c_s_asig5.setFont(fontTex)  
                            
        self.top_cuarto_semestre2_s_asig5 = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestre2_s_asig5.addWidget(self.label_top_c_asig5)
        self.top_cuarto_semestre2_s_asig5.addWidget(self.label_value_top_c_s_asig5)
        
        
        self.top_cuarto_semestre2_vert.addWidget(self.top_cuarto_semestre2)
        self.top_cuarto_semestre2_vert.addStretch(1.3)        
        self.top_cuarto_semestre2_vert.addLayout(self.top_cuarto_semestre2_s_asig1)
        self.top_cuarto_semestre2_vert.addStretch(1)        
        self.top_cuarto_semestre2_vert.addLayout(self.top_cuarto_semestre2_s_asig2)
        self.top_cuarto_semestre2_vert.addStretch(1)        
        self.top_cuarto_semestre2_vert.addLayout(self.top_cuarto_semestre2_s_asig3)
        self.top_cuarto_semestre2_vert.addStretch(1)        
        self.top_cuarto_semestre2_vert.addLayout(self.top_cuarto_semestre2_s_asig4)
        self.top_cuarto_semestre2_vert.addStretch(1)        
        self.top_cuarto_semestre2_vert.addLayout(self.top_cuarto_semestre2_s_asig5)
        self.top_cuarto_semestre2_vert.addStretch(1)        

        self.graph_layout = QtWidgets.QVBoxLayout() 
        
        self.label_graficas = QtWidgets.QLabel(self.dicc.graficas, self)
        self.label_graficas.setToolTip('Pulsa para entrar')
        self.label_graficas.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_graficas.setFont(fontTex) 
        self.label_graficas.setAlignment( QtCore.Qt.AlignHCenter)

        self.graph_layout.addStretch(2)
        self.graph_layout.addWidget(self.label_graficas)

        
        self.static_canvas = FigureCanvas(Figure(figsize=(4, 3),dpi=100))
        self._static_ax = self.static_canvas.figure.subplots(  sharey=True)

        self.graph_layout.addWidget(self.static_canvas)
 
#         self.pinta_primera_grafica(self.names,self.values)
 
 
        self.pie_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.graph_layout.addWidget(self.pie_canvas)
 
 
        self._static_ax2 = self.pie_canvas.figure.subplots(  sharey=True)
    
        self.graph_layout.addStretch(1)


        self.top_cuarto_semestres1_groupBox = QtWidgets.QGroupBox()
        self.top_cuarto_semestres1_groupBox.setTitle(self.dicc.top_1_5) 
        self.top_cuarto_semestres1_groupBox.setLayout(self.top_cuarto_semestre1_vert)
        
                
        self.top_cuarto_semestres2_groupBox = QtWidgets.QGroupBox()
        self.top_cuarto_semestres2_groupBox.setTitle(self.dicc.top_5_10) 
        self.top_cuarto_semestres2_groupBox.setLayout(self.top_cuarto_semestre2_vert)
        
        self.top_cuarto_graficas_groupBox = QtWidgets.QGroupBox()
        self.top_cuarto_graficas_groupBox.setTitle(self.dicc.graficas) 
        self.top_cuarto_graficas_groupBox.setLayout(self.graph_layout)

        self.top_cuarto_group_layout = QtWidgets.QHBoxLayout()
        self.top_cuarto_group_layout.addStretch(1)
        self.top_cuarto_group_layout.addWidget(self.top_cuarto_semestres1_groupBox)
        self.top_cuarto_group_layout.addStretch(1)
        self.top_cuarto_group_layout.addWidget(self.top_cuarto_semestres2_groupBox)     
        self.top_cuarto_group_layout.addStretch(3)
        self.top_cuarto_group_layout.addWidget(self.top_cuarto_graficas_groupBox)
        self.top_cuarto_group_layout.addStretch(1.5)

        
        self.pestana2_groupBox = QtWidgets.QGroupBox()
        self.pestana2_groupBox.setTitle(self.dicc.predicciones) 
        self.pestana2_groupBox.setLayout(self.top_cuarto_group_layout) 

        self.top_cuarto_semestres_layout = QtWidgets.QHBoxLayout()
        self.top_cuarto_semestres_layout.addWidget(self.pestana2_groupBox)     


        self.top_cuarto_semestres_frame.setLayout(self.top_cuarto_semestres_layout)
        
    def pinta_primera_grafica(self,names,values):
        """
        Método que pinta la gráfica de barras del top 10
        """
        self._static_ax.bar([i+1 for i in range(len(values))], values)
        
    def pinta_segunda_grafica(self,names,values):
        """
        Método que pinta la gráfica de las caracterizaciones de las asignaturas del top 10
        """
        explode = (0.1, 0.1, 0.1, 0.1) 
        self._static_ax2.set_aspect('1')
        self._static_ax2.pie(values, labels=names,explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)