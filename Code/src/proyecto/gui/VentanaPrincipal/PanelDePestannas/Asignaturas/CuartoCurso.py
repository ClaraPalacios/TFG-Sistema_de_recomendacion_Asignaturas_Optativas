from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class CuartoCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(CuartoCurso, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_cuarto()
        
    def semestres_cuarto(self):
        self.cuarto_semestres_frame = QtWidgets.QFrame()

        #         Button : Entrar y salir
        self.cuarto_semestre1_vert = QtWidgets.QVBoxLayout()
        self.cuarto_semestre1_1_5_descri = QtWidgets.QLabel(self.dicc.cuarto_sem1_1, self)
        self.cuarto_semestre1_1_5_descri.setToolTip('Pulsa para entrar')
        self.cuarto_semestre1_1_5_descri.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.cuarto_semestre1_1_5_descri.setFont(fontTex)
        self.cuarto_semestre1_1_5_descri.setAlignment( QtCore.Qt.AlignHCenter)

        
        self.cuarto_semestre1_5_10_descri = QtWidgets.QLabel(self.dicc.cuarto_sem1_2, self)
        self.cuarto_semestre1_5_10_descri.setToolTip('Pulsa para entrar')
        self.cuarto_semestre1_5_10_descri.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.cuarto_semestre1_5_10_descri.setFont(fontTex)
        self.cuarto_semestre1_5_10_descri.setAlignment( QtCore.Qt.AlignHCenter)

        
        self.label_c_p_asig1 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig1, self)
        self.label_c_p_asig1.setToolTip('Pulsa para entrar')
        self.label_c_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig1.setFont(fontTex)
        self.label_c_p_asig1.setWordWrap(True)  
         
        self.slider_c_p_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig1.setMinimum(1)
        self.slider_c_p_asig1.setMaximum(5)
        self.slider_c_p_asig1.setValue(3)
        self.slider_c_p_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig1.setTickInterval(1)        
        self.slider_c_p_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig1 = QtWidgets.QLabel(str(self.slider_c_p_asig1.value()), self)
        self.label_value_c_p_asig1.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig1.setFont(fontTex)  
        
        self.cuarto_semestre1p_p_asig1 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig1.addWidget(self.label_c_p_asig1)
        self.cuarto_semestre1p_p_asig1.addWidget(self.slider_c_p_asig1)
        self.cuarto_semestre1p_p_asig1.addWidget(self.label_value_c_p_asig1)

        self.label_c_p_asig2 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig2, self)
        self.label_c_p_asig2.setToolTip('Pulsa para entrar')
        self.label_c_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig2.setFont(fontTex)  
        self.label_c_p_asig2.setWordWrap(True)
         
        self.slider_c_p_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig2.setMinimum(1)
        self.slider_c_p_asig2.setMaximum(5)
        self.slider_c_p_asig2.setValue(3)
        self.slider_c_p_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig2.setTickInterval(1)
        self.slider_c_p_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig2 = QtWidgets.QLabel(str(self.slider_c_p_asig2.value()), self)
        self.label_value_c_p_asig2.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig2.setFont(fontTex) 
        
        self.cuarto_semestre1p_p_asig2 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig2.addWidget(self.label_c_p_asig2)
        self.cuarto_semestre1p_p_asig2.addWidget(self.slider_c_p_asig2)
        self.cuarto_semestre1p_p_asig2.addWidget(self.label_value_c_p_asig2)
        
        self.label_c_p_asig3 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig3, self)
        self.label_c_p_asig3.setToolTip('Pulsa para entrar')
        self.label_c_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig3.setFont(fontTex)  
        self.label_c_p_asig3.setWordWrap(True)
         
        self.slider_c_p_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig3.setMinimum(1)
        self.slider_c_p_asig3.setMaximum(5)
        self.slider_c_p_asig3.setValue(3)
        self.slider_c_p_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig3.setTickInterval(1)
        self.slider_c_p_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig3 = QtWidgets.QLabel(str(self.slider_c_p_asig3.value()), self)
        self.label_value_c_p_asig3.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig3.setFont(fontTex)   
                           
        self.cuarto_semestre1p_p_asig3 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig3.addWidget(self.label_c_p_asig3)
        self.cuarto_semestre1p_p_asig3.addWidget(self.slider_c_p_asig3)
        self.cuarto_semestre1p_p_asig3.addWidget(self.label_value_c_p_asig3)

        self.label_c_p_asig4 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig4, self)
        self.label_c_p_asig4.setToolTip('Pulsa para entrar')
        self.label_c_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig4.setFont(fontTex) 
        self.label_c_p_asig4.setWordWrap(True) 
         
        self.slider_c_p_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig4.setMinimum(1)
        self.slider_c_p_asig4.setMaximum(5)
        self.slider_c_p_asig4.setValue(3)
        self.slider_c_p_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig4.setTickInterval(1)
        self.slider_c_p_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig4 = QtWidgets.QLabel(str(self.slider_c_p_asig4.value()), self)
        self.label_value_c_p_asig4.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig4.setFont(fontTex)   
                            
        self.cuarto_semestre1p_p_asig4 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig4.addWidget(self.label_c_p_asig4)
        self.cuarto_semestre1p_p_asig4.addWidget(self.slider_c_p_asig4)
        self.cuarto_semestre1p_p_asig4.addWidget(self.label_value_c_p_asig4)
        
        self.label_c_p_asig5 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig5, self)
        self.label_c_p_asig5.setToolTip('Pulsa para entrar')
        self.label_c_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig5.setFont(fontTex) 
        self.label_c_p_asig5.setWordWrap(True) 
         
        self.slider_c_p_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig5.setMinimum(1)
        self.slider_c_p_asig5.setMaximum(5)
        self.slider_c_p_asig5.setValue(3)
        self.slider_c_p_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig5.setTickInterval(1)
        self.slider_c_p_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig5 = QtWidgets.QLabel(str(self.slider_c_p_asig5.value()), self)
        self.label_value_c_p_asig5.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig5.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig5 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig5.addWidget(self.label_c_p_asig5)
        self.cuarto_semestre1p_p_asig5.addWidget(self.slider_c_p_asig5)
        self.cuarto_semestre1p_p_asig5.addWidget(self.label_value_c_p_asig5)
        
        ###############################################################
        self.label_c_p_asig6 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig6, self)
        self.label_c_p_asig6.setToolTip('Pulsa para entrar')
        self.label_c_p_asig6.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig6.setFont(fontTex) 
        self.label_c_p_asig6.setWordWrap(True) 
         
        self.slider_c_p_asig6 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig6.setMinimum(1)
        self.slider_c_p_asig6.setMaximum(5)
        self.slider_c_p_asig6.setValue(3)
        self.slider_c_p_asig6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig6.setTickInterval(1)
        self.slider_c_p_asig6.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig6 = QtWidgets.QLabel(str(self.slider_c_p_asig6.value()), self)
        self.label_value_c_p_asig6.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig6.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig6.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig6 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig6.addWidget(self.label_c_p_asig6)
        self.cuarto_semestre1p_p_asig6.addWidget(self.slider_c_p_asig6)
        self.cuarto_semestre1p_p_asig6.addWidget(self.label_value_c_p_asig6)
        
        
        self.label_c_p_asig7 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig7, self)
        self.label_c_p_asig7.setToolTip('Pulsa para entrar')
        self.label_c_p_asig7.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig7.setFont(fontTex) 
        self.label_c_p_asig7.setWordWrap(True) 
         
        self.slider_c_p_asig7 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig7.setMinimum(1)
        self.slider_c_p_asig7.setMaximum(5)
        self.slider_c_p_asig7.setValue(3)
        self.slider_c_p_asig7.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig7.setTickInterval(1)
        self.slider_c_p_asig7.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig7 = QtWidgets.QLabel(str(self.slider_c_p_asig7.value()), self)
        self.label_value_c_p_asig7.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig7.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig7.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig7 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig7.addWidget(self.label_c_p_asig7)
        self.cuarto_semestre1p_p_asig7.addWidget(self.slider_c_p_asig7)
        self.cuarto_semestre1p_p_asig7.addWidget(self.label_value_c_p_asig7)
        
        self.label_c_p_asig8 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig8, self)
        self.label_c_p_asig8.setToolTip('Pulsa para entrar')
        self.label_c_p_asig8.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig8.setFont(fontTex) 
        self.label_c_p_asig8.setWordWrap(True) 
         
        self.slider_c_p_asig8 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig8.setMinimum(1)
        self.slider_c_p_asig8.setMaximum(5)
        self.slider_c_p_asig8.setValue(3)
        self.slider_c_p_asig8.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig8.setTickInterval(1)
        self.slider_c_p_asig8.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig8 = QtWidgets.QLabel(str(self.slider_c_p_asig8.value()), self)
        self.label_value_c_p_asig8.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig8.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig8.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig8 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig8.addWidget(self.label_c_p_asig8)
        self.cuarto_semestre1p_p_asig8.addWidget(self.slider_c_p_asig8)
        self.cuarto_semestre1p_p_asig8.addWidget(self.label_value_c_p_asig8)
        
        self.label_c_p_asig9 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig9, self)
        self.label_c_p_asig9.setToolTip('Pulsa para entrar')
        self.label_c_p_asig9.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig9.setFont(fontTex) 
        self.label_c_p_asig9.setWordWrap(True) 
         
        self.slider_c_p_asig9 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig9.setMinimum(1)
        self.slider_c_p_asig9.setMaximum(5)
        self.slider_c_p_asig9.setValue(3)
        self.slider_c_p_asig9.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig9.setTickInterval(1)
        self.slider_c_p_asig9.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig9 = QtWidgets.QLabel(str(self.slider_c_p_asig9.value()), self)
        self.label_value_c_p_asig9.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig9.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig9.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig9 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig9.addWidget(self.label_c_p_asig9)
        self.cuarto_semestre1p_p_asig9.addWidget(self.slider_c_p_asig9)
        self.cuarto_semestre1p_p_asig9.addWidget(self.label_value_c_p_asig9)
        
        self.label_c_p_asig10 = QtWidgets.QLabel(self.dicc.cuarto_semestre1p_p_asig10, self)
        self.label_c_p_asig10.setToolTip('Pulsa para entrar')
        self.label_c_p_asig10.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_c_p_asig10.setFont(fontTex) 
        self.label_c_p_asig10.setWordWrap(True) 
         
        self.slider_c_p_asig10 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_p_asig10.setMinimum(1)
        self.slider_c_p_asig10.setMaximum(5)
        self.slider_c_p_asig10.setValue(3)
        self.slider_c_p_asig10.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_p_asig10.setTickInterval(1)
        self.slider_c_p_asig10.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_p_asig10 = QtWidgets.QLabel(str(self.slider_c_p_asig10.value()), self)
        self.label_value_c_p_asig10.setToolTip('Pulsa para entrar')
        self.label_value_c_p_asig10.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 12, QtGui.QFont.Bold, True)
        self.label_value_c_p_asig10.setFont(fontTex)  
                            
        self.cuarto_semestre1p_p_asig10 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre1p_p_asig10.addWidget(self.label_c_p_asig10)
        self.cuarto_semestre1p_p_asig10.addWidget(self.slider_c_p_asig10)
        self.cuarto_semestre1p_p_asig10.addWidget(self.label_value_c_p_asig10)
        
        self.cuarto_semestre1_1_5Horizontal = QtWidgets.QHBoxLayout()
        
        self.cuarto_semestre1_1_5 = QtWidgets.QVBoxLayout()
        
        self.cuarto_semestre1_1_5.addWidget(self.cuarto_semestre1_1_5_descri)
        self.cuarto_semestre1_1_5.addStretch(1.3)  
        self.cuarto_semestre1_1_5.addLayout(self.cuarto_semestre1p_p_asig1)
        self.cuarto_semestre1_1_5.addStretch(1)        
        self.cuarto_semestre1_1_5.addLayout(self.cuarto_semestre1p_p_asig2)
        self.cuarto_semestre1_1_5.addStretch(1)        
        self.cuarto_semestre1_1_5.addLayout(self.cuarto_semestre1p_p_asig3)
        self.cuarto_semestre1_1_5.addStretch(1)        
        self.cuarto_semestre1_1_5.addLayout(self.cuarto_semestre1p_p_asig4)
        self.cuarto_semestre1_1_5.addStretch(1)        
        self.cuarto_semestre1_1_5.addLayout(self.cuarto_semestre1p_p_asig5)
        
        self.cuarto_semestre1__5_10 = QtWidgets.QVBoxLayout()

        self.cuarto_semestre1__5_10.addWidget(self.cuarto_semestre1_5_10_descri)
        self.cuarto_semestre1__5_10.addStretch(1.3)  
        self.cuarto_semestre1__5_10.addLayout(self.cuarto_semestre1p_p_asig6)
        self.cuarto_semestre1__5_10.addStretch(1)        
        self.cuarto_semestre1__5_10.addLayout(self.cuarto_semestre1p_p_asig7)
        self.cuarto_semestre1__5_10.addStretch(1) 
        self.cuarto_semestre1__5_10.addLayout(self.cuarto_semestre1p_p_asig8)
        self.cuarto_semestre1__5_10.addStretch(1)  
        self.cuarto_semestre1__5_10.addLayout(self.cuarto_semestre1p_p_asig9)
        self.cuarto_semestre1__5_10.addStretch(1)  
        self.cuarto_semestre1__5_10.addLayout(self.cuarto_semestre1p_p_asig10)
#          
        self.cuarto_semestre1_1_5Horizontal.addLayout(self.cuarto_semestre1_1_5)
        self.cuarto_semestre1_1_5Horizontal.addLayout(self.cuarto_semestre1__5_10)
        #         Button : Entrar y salir
        self.cuarto_semestre2_vert = QtWidgets.QVBoxLayout()
        self.cuarto_semestre2 = QtWidgets.QLabel(self.dicc.cuarto_sem2, self)
        self.cuarto_semestre2.setToolTip('Pulsa para entrar')
        self.cuarto_semestre2.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.cuarto_semestre2.setFont(fontTex)
        self.cuarto_semestre2.setAlignment( QtCore.Qt.AlignHCenter)

        
        self.label_c_asig1 = QtWidgets.QLabel(self.dicc.cuarto_semestre2_s_asig1, self)
        self.label_c_asig1.setToolTip('Pulsa para entrar')
        self.label_c_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_c_asig1.setFont(fontTex)  
        self.label_c_asig1.setWordWrap(True)
         
        self.slider_c_s_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_s_asig1.setMinimum(1)
        self.slider_c_s_asig1.setMaximum(5)
        self.slider_c_s_asig1.setValue(3)
        self.slider_c_s_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_s_asig1.setTickInterval(1)
        self.slider_c_s_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_s_asig1 = QtWidgets.QLabel(str(self.slider_c_s_asig1.value()), self)
        self.label_value_c_s_asig1.setToolTip('Pulsa para entrar')
        self.label_value_c_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_c_s_asig1.setFont(fontTex)                    
                    
        self.cuarto_semestre2_s_asig1 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre2_s_asig1.addWidget(self.label_c_asig1)
        self.cuarto_semestre2_s_asig1.addWidget(self.slider_c_s_asig1)
        self.cuarto_semestre2_s_asig1.addWidget(self.label_value_c_s_asig1)

        self.label_c_asig2 = QtWidgets.QLabel(self.dicc.cuarto_semestre2_s_asig2, self)
        self.label_c_asig2.setToolTip('Pulsa para entrar')
        self.label_c_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_c_asig2.setFont(fontTex)
        self.label_c_asig2.setWordWrap(True)  
         
        self.slider_c_s_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_s_asig2.setMinimum(1)
        self.slider_c_s_asig2.setMaximum(5)
        self.slider_c_s_asig2.setValue(3)
        self.slider_c_s_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_s_asig2.setTickInterval(1)
        self.slider_c_s_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_s_asig2 = QtWidgets.QLabel(str(self.slider_c_s_asig2.value()), self)
        self.label_value_c_s_asig2.setToolTip('Pulsa para entrar')
        self.label_value_c_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_c_s_asig2.setFont(fontTex) 
                            
        self.cuarto_semestre2_s_asig2 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre2_s_asig2.addWidget(self.label_c_asig2)
        self.cuarto_semestre2_s_asig2.addWidget(self.slider_c_s_asig2)
        self.cuarto_semestre2_s_asig2.addWidget(self.label_value_c_s_asig2)
        
        self.label_c_asig3 = QtWidgets.QLabel(self.dicc.cuarto_semestre2_s_asig3, self)
        self.label_c_asig3.setToolTip('Pulsa para entrar')
        self.label_c_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_c_asig3.setFont(fontTex)  
        self.label_c_asig3.setWordWrap(True)
         
        self.slider_c_s_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_s_asig3.setMinimum(1)
        self.slider_c_s_asig3.setMaximum(5)
        self.slider_c_s_asig3.setValue(3)
        self.slider_c_s_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_s_asig3.setTickInterval(1)
        self.slider_c_s_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_s_asig3 = QtWidgets.QLabel(str(self.slider_c_s_asig3.value()), self)
        self.label_value_c_s_asig3.setToolTip('Pulsa para entrar')
        self.label_value_c_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_c_s_asig3.setFont(fontTex) 
                            
        self.cuarto_semestre2_s_asig3 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre2_s_asig3.addWidget(self.label_c_asig3)
        self.cuarto_semestre2_s_asig3.addWidget(self.slider_c_s_asig3)
        self.cuarto_semestre2_s_asig3.addWidget(self.label_value_c_s_asig3)
        
        self.label_c_asig4 = QtWidgets.QLabel(self.dicc.cuarto_semestre2_s_asig4, self)
        self.label_c_asig4.setToolTip('Pulsa para entrar')
        self.label_c_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_c_asig4.setFont(fontTex)  
        self.label_c_asig4.setWordWrap(True)
         
        self.slider_c_s_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_s_asig4.setMinimum(1)
        self.slider_c_s_asig4.setMaximum(5)
        self.slider_c_s_asig4.setValue(3)
        self.slider_c_s_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_s_asig4.setTickInterval(1)
        self.slider_c_s_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_s_asig4 = QtWidgets.QLabel(str(self.slider_c_s_asig4.value()), self)
        self.label_value_c_s_asig4.setToolTip('Pulsa para entrar')
        self.label_value_c_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_c_s_asig4.setFont(fontTex)  
                           
        self.cuarto_semestre2_s_asig4 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre2_s_asig4.addWidget(self.label_c_asig4)
        self.cuarto_semestre2_s_asig4.addWidget(self.slider_c_s_asig4)
        self.cuarto_semestre2_s_asig4.addWidget(self.label_value_c_s_asig4)
        
        self.label_c_asig5 = QtWidgets.QLabel(self.dicc.cuarto_semestre2_s_asig5, self)
        self.label_c_asig5.setToolTip('Pulsa para entrar')
        self.label_c_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_c_asig5.setFont(fontTex)  
        self.label_c_asig5.setWordWrap(True)
         
        self.slider_c_s_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_c_s_asig5.setMinimum(1)
        self.slider_c_s_asig5.setMaximum(5)
        self.slider_c_s_asig5.setValue(3)
        self.slider_c_s_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_c_s_asig5.setTickInterval(1) 
        self.slider_c_s_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_c_s_asig5 = QtWidgets.QLabel(str(self.slider_c_s_asig5.value()), self)
        self.label_value_c_s_asig5.setToolTip('Pulsa para entrar')
        self.label_value_c_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_c_s_asig5.setFont(fontTex)  
                            
        self.cuarto_semestre2_s_asig5 = QtWidgets.QHBoxLayout()
        self.cuarto_semestre2_s_asig5.addWidget(self.label_c_asig5)
        self.cuarto_semestre2_s_asig5.addWidget(self.slider_c_s_asig5)
        self.cuarto_semestre2_s_asig5.addWidget(self.label_value_c_s_asig5)
        
        
        self.cuarto_semestre2_vert.addWidget(self.cuarto_semestre2)
        self.cuarto_semestre2_vert.addStretch(1.3)        
        self.cuarto_semestre2_vert.addLayout(self.cuarto_semestre2_s_asig1)
        self.cuarto_semestre2_vert.addStretch(1)        
        self.cuarto_semestre2_vert.addLayout(self.cuarto_semestre2_s_asig2)
        self.cuarto_semestre2_vert.addStretch(1)        
        self.cuarto_semestre2_vert.addLayout(self.cuarto_semestre2_s_asig3)
        self.cuarto_semestre2_vert.addStretch(1)        
        self.cuarto_semestre2_vert.addLayout(self.cuarto_semestre2_s_asig4)
        self.cuarto_semestre2_vert.addStretch(1)        
        self.cuarto_semestre2_vert.addLayout(self.cuarto_semestre2_s_asig5)
        self.cuarto_semestre2_vert.addStretch(2)        


        self.cuarto_semestres1_groupBox = QtWidgets.QGroupBox()
        self.cuarto_semestres1_groupBox.setTitle(self.dicc.semestre1) 
        self.cuarto_semestres1_groupBox.setLayout(self.cuarto_semestre1_1_5Horizontal)
        
                
        self.cuarto_semestres2_groupBox = QtWidgets.QGroupBox()
        self.cuarto_semestres2_groupBox.setTitle(self.dicc.semestre2) 
        self.cuarto_semestres2_groupBox.setLayout(self.cuarto_semestre2_vert)
        
        self.cuarto_semestres_layoutBox = QtWidgets.QHBoxLayout()
        self.cuarto_semestres_layoutBox.addStretch(1)
        self.cuarto_semestres_layoutBox.addWidget(self.cuarto_semestres1_groupBox)
#         self.cuarto_semestres_layout.addSpacing(50)
        self.cuarto_semestres_layoutBox.addStretch(2)
        self.cuarto_semestres_layoutBox.addWidget(self.cuarto_semestres2_groupBox)     
        self.cuarto_semestres_layoutBox.addStretch(1)
        self.cuarto_semestres_groupBox = QtWidgets.QGroupBox()
        self.cuarto_semestres_groupBox.setTitle("Valoraciones") 
        self.cuarto_semestres_groupBox.setLayout(self.cuarto_semestres_layoutBox)
        
        self.cuarto_semestres_layout = QtWidgets.QHBoxLayout()
        self.cuarto_semestres_layout.addWidget(self.cuarto_semestres_groupBox)  


        self.cuarto_semestres_frame.setLayout(self.cuarto_semestres_layout)
      
    def values_primer_sem(self):
        valoraciones={
            self.label_c_p_asig1.text():self.slider_c_p_asig1.value(),
            self.label_c_p_asig2.text():self.slider_c_p_asig2.value(),
            self.label_c_p_asig3.text():self.slider_c_p_asig3.value(),
            self.label_c_p_asig4.text():self.slider_c_p_asig4.value(),
            self.label_c_p_asig5.text():self.slider_c_p_asig5.value(), 
            self.label_c_p_asig6.text():self.slider_c_p_asig6.value(),  
            self.label_c_p_asig7.text():self.slider_c_p_asig7.value(), 
            self.label_c_p_asig8.text():self.slider_c_p_asig8.value(),  
            self.label_c_p_asig9.text():self.slider_c_p_asig9.value(), 
            self.label_c_p_asig10.text():self.slider_c_p_asig10.value()              
            }
        return valoraciones

    def set_values_primer_sem(self,diccionario):
        self.slider_c_p_asig1.setValue(diccionario[self.label_c_p_asig1.text()])
        self.slider_c_p_asig2.setValue(diccionario[self.label_c_p_asig2.text()])
        self.slider_c_p_asig3.setValue(diccionario[self.label_c_p_asig3.text()])
        self.slider_c_p_asig4.setValue(diccionario[self.label_c_p_asig4.text()])
        self.slider_c_p_asig5.setValue(diccionario[self.label_c_p_asig5.text()])
        self.slider_c_p_asig6.setValue(diccionario[self.label_c_p_asig6.text()])    
        self.slider_c_p_asig7.setValue(diccionario[self.label_c_p_asig7.text()])
        self.slider_c_p_asig8.setValue(diccionario[self.label_c_p_asig8.text()])
        self.slider_c_p_asig9.setValue(diccionario[self.label_c_p_asig9.text()])
        self.slider_c_p_asig10.setValue(diccionario[self.label_c_p_asig10.text()])    
    def values_segundo_sem(self):
        valoraciones={
            self.label_c_asig1.text():self.slider_c_s_asig1.value(),
            self.label_c_asig2.text():self.slider_c_s_asig2.value(),
            self.label_c_asig3.text():self.slider_c_s_asig3.value(),
            self.label_c_asig4.text():self.slider_c_s_asig4.value(),
            self.label_c_asig5.text():self.slider_c_s_asig5.value()       
        }
        return valoraciones    
    
    def set_values_segundo_sem(self,diccionario):
        self.slider_c_s_asig1.setValue(diccionario[self.label_c_asig1.text()])
        self.slider_c_s_asig2.setValue(diccionario[self.label_c_asig2.text()])
        self.slider_c_s_asig3.setValue(diccionario[self.label_c_asig3.text()])
        self.slider_c_s_asig4.setValue(diccionario[self.label_c_asig4.text()])
        self.slider_c_s_asig5.setValue(diccionario[self.label_c_asig5.text()])
             
    def valuechange_slider(self):

        self.label_value_c_p_asig1.setText(str(self.slider_c_p_asig1.value()))
        self.label_value_c_p_asig2.setText(str(self.slider_c_p_asig2.value()))
        self.label_value_c_p_asig3.setText(str(self.slider_c_p_asig3.value()))
        self.label_value_c_p_asig4.setText(str(self.slider_c_p_asig4.value()))
        self.label_value_c_p_asig5.setText(str(self.slider_c_p_asig5.value()))
        self.label_value_c_p_asig6.setText(str(self.slider_c_p_asig6.value()))
        self.label_value_c_p_asig7.setText(str(self.slider_c_p_asig7.value()))
        self.label_value_c_p_asig8.setText(str(self.slider_c_p_asig8.value()))
        self.label_value_c_p_asig9.setText(str(self.slider_c_p_asig9.value()))
        self.label_value_c_p_asig10.setText(str(self.slider_c_p_asig10.value()))
                                        
        
        self.label_value_c_s_asig1.setText(str(self.slider_c_s_asig1.value()))
        self.label_value_c_s_asig2.setText(str(self.slider_c_s_asig2.value()))
        self.label_value_c_s_asig3.setText(str(self.slider_c_s_asig3.value()))
        self.label_value_c_s_asig4.setText(str(self.slider_c_s_asig4.value()))
        self.label_value_c_s_asig5.setText(str(self.slider_c_s_asig5.value()))