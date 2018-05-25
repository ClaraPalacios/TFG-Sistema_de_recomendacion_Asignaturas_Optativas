
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class SegundoCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(SegundoCurso, self).__init__(parent)
        self.semestres_segundo()
        
    def semestres_segundo(self):
        self.segundo_semestres_frame = QtWidgets.QFrame()

        #         Button : Entrar y salir
        self.segundo_semestre1_vert = QtWidgets.QVBoxLayout()
        self.segundo_semestre1 = QtWidgets.QLabel("segundo_sem1", self)
        self.segundo_semestre1.setToolTip('Pulsa para entrar')
        self.segundo_semestre1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.segundo_semestre1.setFont(fontTex)
        
        self.label_s_p_asig1 = QtWidgets.QLabel("s_p_asig1", self)
        self.label_s_p_asig1.setToolTip('Pulsa para entrar')
        self.label_s_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig1.setFont(fontTex)  
         
        self.slider_s_p_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_p_asig1.setMinimum(1)
        self.slider_s_p_asig1.setMaximum(5)
        self.slider_s_p_asig1.setValue(3)
        self.slider_s_p_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_p_asig1.setTickInterval(1)        
        self.slider_s_p_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_p_asig1 = QtWidgets.QLabel(str(self.slider_s_p_asig1.value()), self)
        self.label_value_s_p_asig1.setToolTip('Pulsa para entrar')
        self.label_value_s_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_p_asig1.setFont(fontTex)  
        
        self.segundo_semestre1p_p_asig1 = QtWidgets.QHBoxLayout()
        self.segundo_semestre1p_p_asig1.addWidget(self.label_s_p_asig1)
        self.segundo_semestre1p_p_asig1.addWidget(self.slider_s_p_asig1)
        self.segundo_semestre1p_p_asig1.addWidget(self.label_value_s_p_asig1)

        self.label_s_p_asig2 = QtWidgets.QLabel("s_p_asig2", self)
        self.label_s_p_asig2.setToolTip('Pulsa para entrar')
        self.label_s_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig2.setFont(fontTex)  
         
        self.slider_s_p_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_p_asig2.setMinimum(1)
        self.slider_s_p_asig2.setMaximum(5)
        self.slider_s_p_asig2.setValue(3)
        self.slider_s_p_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_p_asig2.setTickInterval(1)
        self.slider_s_p_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_p_asig2 = QtWidgets.QLabel(str(self.slider_s_p_asig2.value()), self)
        self.label_value_s_p_asig2.setToolTip('Pulsa para entrar')
        self.label_value_s_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_p_asig2.setFont(fontTex) 
        
        self.segundo_semestre1p_p_asig2 = QtWidgets.QHBoxLayout()
        self.segundo_semestre1p_p_asig2.addWidget(self.label_s_p_asig2)
        self.segundo_semestre1p_p_asig2.addWidget(self.slider_s_p_asig2)
        self.segundo_semestre1p_p_asig2.addWidget(self.label_value_s_p_asig2)
        
        self.label_s_p_asig3 = QtWidgets.QLabel("s_p_asig3", self)
        self.label_s_p_asig3.setToolTip('Pulsa para entrar')
        self.label_s_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig3.setFont(fontTex)  
         
        self.slider_s_p_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_p_asig3.setMinimum(1)
        self.slider_s_p_asig3.setMaximum(5)
        self.slider_s_p_asig3.setValue(3)
        self.slider_s_p_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_p_asig3.setTickInterval(1)
        self.slider_s_p_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_p_asig3 = QtWidgets.QLabel(str(self.slider_s_p_asig3.value()), self)
        self.label_value_s_p_asig3.setToolTip('Pulsa para entrar')
        self.label_value_s_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_p_asig3.setFont(fontTex)   
                           
        self.segundo_semestre1p_p_asig3 = QtWidgets.QHBoxLayout()
        self.segundo_semestre1p_p_asig3.addWidget(self.label_s_p_asig3)
        self.segundo_semestre1p_p_asig3.addWidget(self.slider_s_p_asig3)
        self.segundo_semestre1p_p_asig3.addWidget(self.label_value_s_p_asig3)

        self.label_s_p_asig4 = QtWidgets.QLabel("s_p_asig4", self)
        self.label_s_p_asig4.setToolTip('Pulsa para entrar')
        self.label_s_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig4.setFont(fontTex)  
         
        self.slider_s_p_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_p_asig4.setMinimum(1)
        self.slider_s_p_asig4.setMaximum(5)
        self.slider_s_p_asig4.setValue(3)
        self.slider_s_p_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_p_asig4.setTickInterval(1)
        self.slider_s_p_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_p_asig4 = QtWidgets.QLabel(str(self.slider_s_p_asig4.value()), self)
        self.label_value_s_p_asig4.setToolTip('Pulsa para entrar')
        self.label_value_s_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_p_asig4.setFont(fontTex)   
                            
        self.segundo_semestre1p_p_asig4 = QtWidgets.QHBoxLayout()
        self.segundo_semestre1p_p_asig4.addWidget(self.label_s_p_asig4)
        self.segundo_semestre1p_p_asig4.addWidget(self.slider_s_p_asig4)
        self.segundo_semestre1p_p_asig4.addWidget(self.label_value_s_p_asig4)
        
        self.label_s_p_asig5 = QtWidgets.QLabel("s_p_asig5", self)
        self.label_s_p_asig5.setToolTip('Pulsa para entrar')
        self.label_s_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_p_asig5.setFont(fontTex)  
         
        self.slider_s_p_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_p_asig5.setMinimum(1)
        self.slider_s_p_asig5.setMaximum(5)
        self.slider_s_p_asig5.setValue(3)
        self.slider_s_p_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_p_asig5.setTickInterval(1)
        self.slider_s_p_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_p_asig5 = QtWidgets.QLabel(str(self.slider_s_p_asig5.value()), self)
        self.label_value_s_p_asig5.setToolTip('Pulsa para entrar')
        self.label_value_s_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_p_asig5.setFont(fontTex)  
                            
        self.segundo_semestre1p_p_asig5 = QtWidgets.QHBoxLayout()
        self.segundo_semestre1p_p_asig5.addWidget(self.label_s_p_asig5)
        self.segundo_semestre1p_p_asig5.addWidget(self.slider_s_p_asig5)
        self.segundo_semestre1p_p_asig5.addWidget(self.label_value_s_p_asig5)
        
        self.segundo_semestre1_vert.addWidget(self.segundo_semestre1)
        self.segundo_semestre1_vert.addStretch(1.3)  
        self.segundo_semestre1_vert.addLayout(self.segundo_semestre1p_p_asig1)
        self.segundo_semestre1_vert.addStretch(1)        
        self.segundo_semestre1_vert.addLayout(self.segundo_semestre1p_p_asig2)
        self.segundo_semestre1_vert.addStretch(1)        
        self.segundo_semestre1_vert.addLayout(self.segundo_semestre1p_p_asig3)
        self.segundo_semestre1_vert.addStretch(1)        
        self.segundo_semestre1_vert.addLayout(self.segundo_semestre1p_p_asig4)
        self.segundo_semestre1_vert.addStretch(1)        
        self.segundo_semestre1_vert.addLayout(self.segundo_semestre1p_p_asig5)
        self.segundo_semestre1_vert.addStretch(2)        


        #         Button : Entrar y salir
        self.segundo_semestre2_vert = QtWidgets.QVBoxLayout()
        self.segundo_semestre2 = QtWidgets.QLabel("segundo_sem2", self)
        self.segundo_semestre2.setToolTip('Pulsa para entrar')
        self.segundo_semestre2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.segundo_semestre2.setFont(fontTex)
        
        self.label_s_asig1 = QtWidgets.QLabel("s_s_asig1", self)
        self.label_s_asig1.setToolTip('Pulsa para entrar')
        self.label_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig1.setFont(fontTex)  
         
        self.slider_s_s_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_s_asig1.setMinimum(1)
        self.slider_s_s_asig1.setMaximum(5)
        self.slider_s_s_asig1.setValue(3)
        self.slider_s_s_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_s_asig1.setTickInterval(1)
        self.slider_s_s_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_s_asig1 = QtWidgets.QLabel(str(self.slider_s_s_asig1.value()), self)
        self.label_value_s_s_asig1.setToolTip('Pulsa para entrar')
        self.label_value_s_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_s_asig1.setFont(fontTex)                    
                    
        self.segundo_semestre2_s_asig1 = QtWidgets.QHBoxLayout()
        self.segundo_semestre2_s_asig1.addWidget(self.label_s_asig1)
        self.segundo_semestre2_s_asig1.addWidget(self.slider_s_s_asig1)
        self.segundo_semestre2_s_asig1.addWidget(self.label_value_s_s_asig1)

        self.label_s_asig2 = QtWidgets.QLabel("s_s_asig2", self)
        self.label_s_asig2.setToolTip('Pulsa para entrar')
        self.label_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig2.setFont(fontTex)  
         
        self.slider_s_s_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_s_asig2.setMinimum(1)
        self.slider_s_s_asig2.setMaximum(5)
        self.slider_s_s_asig2.setValue(3)
        self.slider_s_s_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_s_asig2.setTickInterval(1)
        self.slider_s_s_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_s_asig2 = QtWidgets.QLabel(str(self.slider_s_s_asig2.value()), self)
        self.label_value_s_s_asig2.setToolTip('Pulsa para entrar')
        self.label_value_s_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_s_asig2.setFont(fontTex) 
                            
        self.segundo_semestre2_s_asig2 = QtWidgets.QHBoxLayout()
        self.segundo_semestre2_s_asig2.addWidget(self.label_s_asig2)
        self.segundo_semestre2_s_asig2.addWidget(self.slider_s_s_asig2)
        self.segundo_semestre2_s_asig2.addWidget(self.label_value_s_s_asig2)
        
        self.label_s_asig3 = QtWidgets.QLabel("s_s_asig3", self)
        self.label_s_asig3.setToolTip('Pulsa para entrar')
        self.label_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig3.setFont(fontTex)  
         
        self.slider_s_s_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_s_asig3.setMinimum(1)
        self.slider_s_s_asig3.setMaximum(5)
        self.slider_s_s_asig3.setValue(3)
        self.slider_s_s_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_s_asig3.setTickInterval(1)
        self.slider_s_s_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_s_asig3 = QtWidgets.QLabel(str(self.slider_s_s_asig3.value()), self)
        self.label_value_s_s_asig3.setToolTip('Pulsa para entrar')
        self.label_value_s_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_s_asig3.setFont(fontTex) 
                            
        self.segundo_semestre2_s_asig3 = QtWidgets.QHBoxLayout()
        self.segundo_semestre2_s_asig3.addWidget(self.label_s_asig3)
        self.segundo_semestre2_s_asig3.addWidget(self.slider_s_s_asig3)
        self.segundo_semestre2_s_asig3.addWidget(self.label_value_s_s_asig3)
        
        self.label_s_asig4 = QtWidgets.QLabel("s_s_asig4", self)
        self.label_s_asig4.setToolTip('Pulsa para entrar')
        self.label_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig4.setFont(fontTex)  
         
        self.slider_s_s_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_s_asig4.setMinimum(1)
        self.slider_s_s_asig4.setMaximum(5)
        self.slider_s_s_asig4.setValue(3)
        self.slider_s_s_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_s_asig4.setTickInterval(1)
        self.slider_s_s_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_s_asig4 = QtWidgets.QLabel(str(self.slider_s_s_asig4.value()), self)
        self.label_value_s_s_asig4.setToolTip('Pulsa para entrar')
        self.label_value_s_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_s_asig4.setFont(fontTex)  
                           
        self.segundo_semestre2_s_asig4 = QtWidgets.QHBoxLayout()
        self.segundo_semestre2_s_asig4.addWidget(self.label_s_asig4)
        self.segundo_semestre2_s_asig4.addWidget(self.slider_s_s_asig4)
        self.segundo_semestre2_s_asig4.addWidget(self.label_value_s_s_asig4)
        
        self.label_s_asig5 = QtWidgets.QLabel("s_s_asig5", self)
        self.label_s_asig5.setToolTip('Pulsa para entrar')
        self.label_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_s_asig5.setFont(fontTex)  
         
        self.slider_s_s_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_s_s_asig5.setMinimum(1)
        self.slider_s_s_asig5.setMaximum(5)
        self.slider_s_s_asig5.setValue(3)
        self.slider_s_s_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_s_s_asig5.setTickInterval(1) 
        self.slider_s_s_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_s_s_asig5 = QtWidgets.QLabel(str(self.slider_s_s_asig5.value()), self)
        self.label_value_s_s_asig5.setToolTip('Pulsa para entrar')
        self.label_value_s_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_s_s_asig5.setFont(fontTex)  
                            
        self.segundo_semestre2_s_asig5 = QtWidgets.QHBoxLayout()
        self.segundo_semestre2_s_asig5.addWidget(self.label_s_asig5)
        self.segundo_semestre2_s_asig5.addWidget(self.slider_s_s_asig5)
        self.segundo_semestre2_s_asig5.addWidget(self.label_value_s_s_asig5)
        
        
        self.segundo_semestre2_vert.addWidget(self.segundo_semestre2)
        self.segundo_semestre2_vert.addStretch(1.3)        
        self.segundo_semestre2_vert.addLayout(self.segundo_semestre2_s_asig1)
        self.segundo_semestre2_vert.addStretch(1)        
        self.segundo_semestre2_vert.addLayout(self.segundo_semestre2_s_asig2)
        self.segundo_semestre2_vert.addStretch(1)        
        self.segundo_semestre2_vert.addLayout(self.segundo_semestre2_s_asig3)
        self.segundo_semestre2_vert.addStretch(1)        
        self.segundo_semestre2_vert.addLayout(self.segundo_semestre2_s_asig4)
        self.segundo_semestre2_vert.addStretch(1)        
        self.segundo_semestre2_vert.addLayout(self.segundo_semestre2_s_asig5)
        self.segundo_semestre2_vert.addStretch(2)        

        self.segundo_semestres1_groupBox = QtWidgets.QGroupBox()
        self.segundo_semestres1_groupBox.setTitle("Semestre1") 
        self.segundo_semestres1_groupBox.setLayout(self.segundo_semestre1_vert)
        
                
        self.segundo_semestres2_groupBox = QtWidgets.QGroupBox()
        self.segundo_semestres2_groupBox.setTitle("Semestre2") 
        self.segundo_semestres2_groupBox.setLayout(self.segundo_semestre2_vert)


        self.segundo_semestres_layoutBox = QtWidgets.QHBoxLayout()
        self.segundo_semestres_layoutBox.addStretch(1)
        self.segundo_semestres_layoutBox.addWidget(self.segundo_semestres1_groupBox)
#         self.segundo_semestres_layout.addSpacing(50)
        self.segundo_semestres_layoutBox.addStretch(2)
        self.segundo_semestres_layoutBox.addWidget(self.segundo_semestres2_groupBox)     
        self.segundo_semestres_layoutBox.addStretch(1)

        self.segundo_semestres_groupBox = QtWidgets.QGroupBox()
        self.segundo_semestres_groupBox.setTitle("Valoraciones") 
        self.segundo_semestres_groupBox.setLayout(self.segundo_semestres_layoutBox)
        
        self.segundo_semestres_layout = QtWidgets.QHBoxLayout()
        self.segundo_semestres_layout.addWidget(self.segundo_semestres_groupBox)  


        self.segundo_semestres_frame.setLayout(self.segundo_semestres_layout)
        
    def values_primer_sem(self):
        valoraciones={
            self.label_s_p_asig1.text():self.slider_s_p_asig1.value(),
            self.label_s_p_asig2.text():self.slider_s_p_asig2.value(),
            self.label_s_p_asig3.text():self.slider_s_p_asig3.value(),
            self.label_s_p_asig4.text():self.slider_s_p_asig4.value(),
            self.label_s_p_asig5.text():self.slider_s_p_asig5.value()            
            }
        return valoraciones

    def set_values_primer_sem(self,diccionario):
        self.slider_s_p_asig1.setValue(diccionario[self.label_s_p_asig1.text()])
        self.slider_s_p_asig2.setValue(diccionario[self.label_s_p_asig2.text()])
        self.slider_s_p_asig3.setValue(diccionario[self.label_s_p_asig3.text()])
        self.slider_s_p_asig4.setValue(diccionario[self.label_s_p_asig4.text()])
        self.slider_s_p_asig5.setValue(diccionario[self.label_s_p_asig5.text()])
            
    def values_segundo_sem(self):
        valoraciones={
            self.label_s_asig1.text():self.slider_s_s_asig1.value(),
            self.label_s_asig2.text():self.slider_s_s_asig2.value(),
            self.label_s_asig3.text():self.slider_s_s_asig3.value(),
            self.label_s_asig4.text():self.slider_s_s_asig4.value(),
            self.label_s_asig5.text():self.slider_s_s_asig5.value()          
        }
        return valoraciones 
    
    def set_values_segundo_sem(self,diccionario):
        self.slider_s_s_asig1.setValue(diccionario[self.label_s_asig1.text()])
        self.slider_s_s_asig2.setValue(diccionario[self.label_s_asig2.text()])
        self.slider_s_s_asig3.setValue(diccionario[self.label_s_asig3.text()])
        self.slider_s_s_asig4.setValue(diccionario[self.label_s_asig4.text()])
        self.slider_s_s_asig5.setValue(diccionario[self.label_s_asig5.text()])    
             
    def valuechange_slider(self):

        self.label_value_s_p_asig1.setText(str(self.slider_s_p_asig1.value()))
        self.label_value_s_p_asig2.setText(str(self.slider_s_p_asig2.value()))
        self.label_value_s_p_asig3.setText(str(self.slider_s_p_asig3.value()))
        self.label_value_s_p_asig4.setText(str(self.slider_s_p_asig4.value()))
        self.label_value_s_p_asig5.setText(str(self.slider_s_p_asig5.value()))
        
        self.label_value_s_s_asig1.setText(str(self.slider_s_s_asig1.value()))
        self.label_value_s_s_asig2.setText(str(self.slider_s_s_asig2.value()))
        self.label_value_s_s_asig3.setText(str(self.slider_s_s_asig3.value()))
        self.label_value_s_s_asig4.setText(str(self.slider_s_s_asig4.value()))
        self.label_value_s_s_asig5.setText(str(self.slider_s_s_asig5.value()))