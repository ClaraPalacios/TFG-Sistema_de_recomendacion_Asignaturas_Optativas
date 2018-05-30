from proyecto.dicc.Dicc import Dicc
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class TerceroCurso(QtWidgets.QFrame):
    
    def __init__(self, parent = None):
        super(TerceroCurso, self).__init__(parent)
        self.dicc = Dicc()
        self.semestres_tercero()
        
    def semestres_tercero(self):
        self.tercero_semestres_frame = QtWidgets.QFrame()

        #         Button : Entrar y salir
        self.tercero_semestre1_vert = QtWidgets.QVBoxLayout()
        self.tercero_semestre1 = QtWidgets.QLabel(self.dicc.tercero_sem1, self)
        self.tercero_semestre1.setToolTip('Pulsa para entrar')
        self.tercero_semestre1.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.tercero_semestre1.setFont(fontTex)
        self.tercero_semestre1.setAlignment( QtCore.Qt.AlignHCenter)

        
        self.label_t_p_asig1 = QtWidgets.QLabel(self.dicc.tercero_semestre1p_p_asig1, self)
        self.label_t_p_asig1.setToolTip('Pulsa para entrar')
        self.label_t_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig1.setFont(fontTex)  
        self.label_t_p_asig1.setWordWrap(True)
         
        self.slider_t_p_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_p_asig1.setMinimum(1)
        self.slider_t_p_asig1.setMaximum(5)
        self.slider_t_p_asig1.setValue(3)
        self.slider_t_p_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_p_asig1.setTickInterval(1)        
        self.slider_t_p_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_p_asig1 = QtWidgets.QLabel(str(self.slider_t_p_asig1.value()), self)
        self.label_value_t_p_asig1.setToolTip('Pulsa para entrar')
        self.label_value_t_p_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_p_asig1.setFont(fontTex)  
        
        self.check_box_t_p_asig1 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_p_asig1.stateChanged.connect(self.valuechange_checkBox1)
                
        self.tercero_semestre1p_p_asig1 = QtWidgets.QHBoxLayout()
        self.tercero_semestre1p_p_asig1.addWidget(self.label_t_p_asig1)
        self.tercero_semestre1p_p_asig1.addWidget(self.slider_t_p_asig1)
        self.tercero_semestre1p_p_asig1.addWidget(self.label_value_t_p_asig1)
        self.tercero_semestre1p_p_asig1.addWidget(self.check_box_t_p_asig1)

        self.label_t_p_asig2 = QtWidgets.QLabel(self.dicc.tercero_semestre1p_p_asig2, self)
        self.label_t_p_asig2.setToolTip('Pulsa para entrar')
        self.label_t_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig2.setFont(fontTex)  
        self.label_t_p_asig2.setWordWrap(True)
         
        self.slider_t_p_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_p_asig2.setMinimum(1)
        self.slider_t_p_asig2.setMaximum(5)
        self.slider_t_p_asig2.setValue(3)
        self.slider_t_p_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_p_asig2.setTickInterval(1)
        self.slider_t_p_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_p_asig2 = QtWidgets.QLabel(str(self.slider_t_p_asig2.value()), self)
        self.label_value_t_p_asig2.setToolTip('Pulsa para entrar')
        self.label_value_t_p_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_p_asig2.setFont(fontTex) 
        
        self.check_box_t_p_asig2 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_p_asig2.stateChanged.connect(self.valuechange_checkBox2)
                
        self.tercero_semestre1p_p_asig2 = QtWidgets.QHBoxLayout()
        self.tercero_semestre1p_p_asig2.addWidget(self.label_t_p_asig2)
        self.tercero_semestre1p_p_asig2.addWidget(self.slider_t_p_asig2)
        self.tercero_semestre1p_p_asig2.addWidget(self.label_value_t_p_asig2)
        self.tercero_semestre1p_p_asig2.addWidget(self.check_box_t_p_asig2)
        
        self.label_t_p_asig3 = QtWidgets.QLabel(self.dicc.tercero_semestre1p_p_asig3, self)
        self.label_t_p_asig3.setToolTip('Pulsa para entrar')
        self.label_t_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig3.setFont(fontTex)  
        self.label_t_p_asig3.setWordWrap(True)
         
        self.slider_t_p_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_p_asig3.setMinimum(1)
        self.slider_t_p_asig3.setMaximum(5)
        self.slider_t_p_asig3.setValue(3)
        self.slider_t_p_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_p_asig3.setTickInterval(1)
        self.slider_t_p_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_p_asig3 = QtWidgets.QLabel(str(self.slider_t_p_asig3.value()), self)
        self.label_value_t_p_asig3.setToolTip('Pulsa para entrar')
        self.label_value_t_p_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_p_asig3.setFont(fontTex)   

        self.check_box_t_p_asig3 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_p_asig3.stateChanged.connect(self.valuechange_checkBox3)
                
        self.tercero_semestre1p_p_asig3 = QtWidgets.QHBoxLayout()
        self.tercero_semestre1p_p_asig3.addWidget(self.label_t_p_asig3)
        self.tercero_semestre1p_p_asig3.addWidget(self.slider_t_p_asig3)
        self.tercero_semestre1p_p_asig3.addWidget(self.label_value_t_p_asig3)
        self.tercero_semestre1p_p_asig3.addWidget(self.check_box_t_p_asig3)

        self.label_t_p_asig4 = QtWidgets.QLabel(self.dicc.tercero_semestre1p_p_asig4, self)
        self.label_t_p_asig4.setToolTip('Pulsa para entrar')
        self.label_t_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig4.setFont(fontTex)  
        self.label_t_p_asig4.setWordWrap(True)
         
        self.slider_t_p_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_p_asig4.setMinimum(1)
        self.slider_t_p_asig4.setMaximum(5)
        self.slider_t_p_asig4.setValue(3)
        self.slider_t_p_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_p_asig4.setTickInterval(1)
        self.slider_t_p_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_p_asig4 = QtWidgets.QLabel(str(self.slider_t_p_asig4.value()), self)
        self.label_value_t_p_asig4.setToolTip('Pulsa para entrar')
        self.label_value_t_p_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_p_asig4.setFont(fontTex)   
                       
        self.check_box_t_p_asig4 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_p_asig4.stateChanged.connect(self.valuechange_checkBox4)
                                    
        self.tercero_semestre1p_p_asig4 = QtWidgets.QHBoxLayout()
        self.tercero_semestre1p_p_asig4.addWidget(self.label_t_p_asig4)
        self.tercero_semestre1p_p_asig4.addWidget(self.slider_t_p_asig4)
        self.tercero_semestre1p_p_asig4.addWidget(self.label_value_t_p_asig4)
        self.tercero_semestre1p_p_asig4.addWidget(self.check_box_t_p_asig4)
        
        self.label_t_p_asig5 = QtWidgets.QLabel(self.dicc.tercero_semestre1p_p_asig5, self)
        self.label_t_p_asig5.setToolTip('Pulsa para entrar')
        self.label_t_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_p_asig5.setFont(fontTex)  
        self.label_t_p_asig5.setWordWrap(True)
         
        self.slider_t_p_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_p_asig5.setMinimum(1)
        self.slider_t_p_asig5.setMaximum(5)
        self.slider_t_p_asig5.setValue(3)
        self.slider_t_p_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_p_asig5.setTickInterval(1)
        self.slider_t_p_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_p_asig5 = QtWidgets.QLabel(str(self.slider_t_p_asig5.value()), self)
        self.label_value_t_p_asig5.setToolTip('Pulsa para entrar')
        self.label_value_t_p_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_p_asig5.setFont(fontTex)  
                     
        self.check_box_t_p_asig5 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_p_asig5.stateChanged.connect(self.valuechange_checkBox5)                     
                            
        self.tercero_semestre1p_p_asig5 = QtWidgets.QHBoxLayout()
        self.tercero_semestre1p_p_asig5.addWidget(self.label_t_p_asig5)
        self.tercero_semestre1p_p_asig5.addWidget(self.slider_t_p_asig5)
        self.tercero_semestre1p_p_asig5.addWidget(self.label_value_t_p_asig5)
        self.tercero_semestre1p_p_asig5.addWidget(self.check_box_t_p_asig5)
        
        self.tercero_semestre1_vert.addWidget(self.tercero_semestre1)
        self.tercero_semestre1_vert.addStretch(1.3)  
        self.tercero_semestre1_vert.addLayout(self.tercero_semestre1p_p_asig1)
        self.tercero_semestre1_vert.addStretch(1)        
        self.tercero_semestre1_vert.addLayout(self.tercero_semestre1p_p_asig2)
        self.tercero_semestre1_vert.addStretch(1)        
        self.tercero_semestre1_vert.addLayout(self.tercero_semestre1p_p_asig3)
        self.tercero_semestre1_vert.addStretch(1)        
        self.tercero_semestre1_vert.addLayout(self.tercero_semestre1p_p_asig4)
        self.tercero_semestre1_vert.addStretch(1)        
        self.tercero_semestre1_vert.addLayout(self.tercero_semestre1p_p_asig5)
        self.tercero_semestre1_vert.addStretch(2)        


        #         Button : Entrar y salir
        self.tercero_semestre2_vert = QtWidgets.QVBoxLayout()
        self.tercero_semestre2 = QtWidgets.QLabel(self.dicc.tercero_sem2, self)
        self.tercero_semestre2.setToolTip('Pulsa para entrar')
        self.tercero_semestre2.setStyleSheet('color: blue; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.tercero_semestre2.setFont(fontTex)
        self.tercero_semestre2.setAlignment( QtCore.Qt.AlignHCenter)

        
        self.label_t_asig1 = QtWidgets.QLabel(self.dicc.tercero_semestre2_s_asig1, self)
        self.label_t_asig1.setToolTip('Pulsa para entrar')
        self.label_t_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig1.setFont(fontTex)
        self.label_t_asig1.setWordWrap(True)
  
         
        self.slider_t_s_asig1 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_s_asig1.setMinimum(1)
        self.slider_t_s_asig1.setMaximum(5)
        self.slider_t_s_asig1.setValue(3)
        self.slider_t_s_asig1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_s_asig1.setTickInterval(1)
        self.slider_t_s_asig1.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_s_asig1 = QtWidgets.QLabel(str(self.slider_t_s_asig1.value()), self)
        self.label_value_t_s_asig1.setToolTip('Pulsa para entrar')
        self.label_value_t_s_asig1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_s_asig1.setFont(fontTex)                    
                    
        self.check_box_t_s_asig1 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_s_asig1.stateChanged.connect(self.valuechange_checkBox2_1)                    
                    
        self.tercero_semestre2_s_asig1 = QtWidgets.QHBoxLayout()
        self.tercero_semestre2_s_asig1.addWidget(self.label_t_asig1)
        self.tercero_semestre2_s_asig1.addWidget(self.slider_t_s_asig1)
        self.tercero_semestre2_s_asig1.addWidget(self.label_value_t_s_asig1)
        self.tercero_semestre2_s_asig1.addWidget(self.check_box_t_s_asig1)

        self.label_t_asig2 = QtWidgets.QLabel(self.dicc.tercero_semestre2_s_asig2, self)
        self.label_t_asig2.setToolTip('Pulsa para entrar')
        self.label_t_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig2.setFont(fontTex)  
        self.label_t_asig2.setWordWrap(True)
         
        self.slider_t_s_asig2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_s_asig2.setMinimum(1)
        self.slider_t_s_asig2.setMaximum(5)
        self.slider_t_s_asig2.setValue(3)
        self.slider_t_s_asig2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_s_asig2.setTickInterval(1)
        self.slider_t_s_asig2.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_s_asig2 = QtWidgets.QLabel(str(self.slider_t_s_asig2.value()), self)
        self.label_value_t_s_asig2.setToolTip('Pulsa para entrar')
        self.label_value_t_s_asig2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_s_asig2.setFont(fontTex) 
                           
        self.check_box_t_s_asig2 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_s_asig2.stateChanged.connect(self.valuechange_checkBox2_2)                            
                            
        self.tercero_semestre2_s_asig2 = QtWidgets.QHBoxLayout()
        self.tercero_semestre2_s_asig2.addWidget(self.label_t_asig2)
        self.tercero_semestre2_s_asig2.addWidget(self.slider_t_s_asig2)
        self.tercero_semestre2_s_asig2.addWidget(self.label_value_t_s_asig2)
        self.tercero_semestre2_s_asig2.addWidget(self.check_box_t_s_asig2)
        
        self.label_t_asig3 = QtWidgets.QLabel(self.dicc.tercero_semestre2_s_asig3, self)
        self.label_t_asig3.setToolTip('Pulsa para entrar')
        self.label_t_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig3.setFont(fontTex)
        self.label_t_asig3.setWordWrap(True)  
         
        self.slider_t_s_asig3 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_s_asig3.setMinimum(1)
        self.slider_t_s_asig3.setMaximum(5)
        self.slider_t_s_asig3.setValue(3)
        self.slider_t_s_asig3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_s_asig3.setTickInterval(1)
        self.slider_t_s_asig3.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_s_asig3 = QtWidgets.QLabel(str(self.slider_t_s_asig3.value()), self)
        self.label_value_t_s_asig3.setToolTip('Pulsa para entrar')
        self.label_value_t_s_asig3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_s_asig3.setFont(fontTex) 
                            
        self.check_box_t_s_asig3 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_s_asig3.stateChanged.connect(self.valuechange_checkBox2_3)                             
                            
        self.tercero_semestre2_s_asig3 = QtWidgets.QHBoxLayout()
        self.tercero_semestre2_s_asig3.addWidget(self.label_t_asig3)
        self.tercero_semestre2_s_asig3.addWidget(self.slider_t_s_asig3)
        self.tercero_semestre2_s_asig3.addWidget(self.label_value_t_s_asig3)
        self.tercero_semestre2_s_asig3.addWidget(self.check_box_t_s_asig3)

        
        self.label_t_asig4 = QtWidgets.QLabel(self.dicc.tercero_semestre2_s_asig4, self)
        self.label_t_asig4.setToolTip('Pulsa para entrar')
        self.label_t_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig4.setFont(fontTex)  
        self.label_t_asig4.setWordWrap(True)
         
        self.slider_t_s_asig4 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_s_asig4.setMinimum(1)
        self.slider_t_s_asig4.setMaximum(5)
        self.slider_t_s_asig4.setValue(3)
        self.slider_t_s_asig4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_s_asig4.setTickInterval(1)
        self.slider_t_s_asig4.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_s_asig4 = QtWidgets.QLabel(str(self.slider_t_s_asig4.value()), self)
        self.label_value_t_s_asig4.setToolTip('Pulsa para entrar')
        self.label_value_t_s_asig4.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_s_asig4.setFont(fontTex)  
                           
        self.check_box_t_s_asig4 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_s_asig4.stateChanged.connect(self.valuechange_checkBox2_4)                            
                           
        self.tercero_semestre2_s_asig4 = QtWidgets.QHBoxLayout()
        self.tercero_semestre2_s_asig4.addWidget(self.label_t_asig4)
        self.tercero_semestre2_s_asig4.addWidget(self.slider_t_s_asig4)
        self.tercero_semestre2_s_asig4.addWidget(self.label_value_t_s_asig4)
        self.tercero_semestre2_s_asig4.addWidget(self.check_box_t_s_asig4)
        
        self.label_t_asig5 = QtWidgets.QLabel(self.dicc.tercero_semestre2_s_asig5, self)
        self.label_t_asig5.setToolTip('Pulsa para entrar')
        self.label_t_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_t_asig5.setFont(fontTex)  
        self.label_t_asig5.setWordWrap(True)
         
        self.slider_t_s_asig5 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_t_s_asig5.setMinimum(1)
        self.slider_t_s_asig5.setMaximum(5)
        self.slider_t_s_asig5.setValue(3)
        self.slider_t_s_asig5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_t_s_asig5.setTickInterval(1) 
        self.slider_t_s_asig5.valueChanged.connect(self.valuechange_slider)


        self.label_value_t_s_asig5 = QtWidgets.QLabel(str(self.slider_t_s_asig5.value()), self)
        self.label_value_t_s_asig5.setToolTip('Pulsa para entrar')
        self.label_value_t_s_asig5.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.label_value_t_s_asig5.setFont(fontTex)  
                            
        self.check_box_t_s_asig5 = QtWidgets.QCheckBox('Omitir', self)
        self.check_box_t_s_asig5.stateChanged.connect(self.valuechange_checkBox2_5)                             
                            
        self.tercero_semestre2_s_asig5 = QtWidgets.QHBoxLayout()
        self.tercero_semestre2_s_asig5.addWidget(self.label_t_asig5)
        self.tercero_semestre2_s_asig5.addWidget(self.slider_t_s_asig5)
        self.tercero_semestre2_s_asig5.addWidget(self.label_value_t_s_asig5)
        self.tercero_semestre2_s_asig5.addWidget(self.check_box_t_s_asig5)

        
        self.tercero_semestre2_vert.addWidget(self.tercero_semestre2)
        self.tercero_semestre2_vert.addStretch(1.3)        
        self.tercero_semestre2_vert.addLayout(self.tercero_semestre2_s_asig1)
        self.tercero_semestre2_vert.addStretch(1)        
        self.tercero_semestre2_vert.addLayout(self.tercero_semestre2_s_asig2)
        self.tercero_semestre2_vert.addStretch(1)        
        self.tercero_semestre2_vert.addLayout(self.tercero_semestre2_s_asig3)
        self.tercero_semestre2_vert.addStretch(1)        
        self.tercero_semestre2_vert.addLayout(self.tercero_semestre2_s_asig4)
        self.tercero_semestre2_vert.addStretch(1)        
        self.tercero_semestre2_vert.addLayout(self.tercero_semestre2_s_asig5)
        self.tercero_semestre2_vert.addStretch(2)        


        self.tercero_semestres1_groupBox = QtWidgets.QGroupBox()
        self.tercero_semestres1_groupBox.setTitle(self.dicc.semestre1) 
        self.tercero_semestres1_groupBox.setLayout(self.tercero_semestre1_vert)
        
                
        self.tercero_semestres2_groupBox = QtWidgets.QGroupBox()
        self.tercero_semestres2_groupBox.setTitle(self.dicc.semestre2) 
        self.tercero_semestres2_groupBox.setLayout(self.tercero_semestre2_vert)

        self.tercero_semestres_layoutBox = QtWidgets.QHBoxLayout()
        self.tercero_semestres_layoutBox.addStretch(1)
        self.tercero_semestres_layoutBox.addWidget(self.tercero_semestres1_groupBox)
#         self.tercero_semestres_layout.addSpacing(50)
        self.tercero_semestres_layoutBox.addStretch(2)
        self.tercero_semestres_layoutBox.addWidget(self.tercero_semestres2_groupBox)     
        self.tercero_semestres_layoutBox.addStretch(1)
        
        self.tercero_semestres_groupBox = QtWidgets.QGroupBox()
        self.tercero_semestres_groupBox.setTitle("Valoraciones") 
        self.tercero_semestres_groupBox.setLayout(self.tercero_semestres_layoutBox)
        
        self.tercero_semestres_layout = QtWidgets.QHBoxLayout()
        self.tercero_semestres_layout.addWidget(self.tercero_semestres_groupBox)  


        self.tercero_semestres_frame.setLayout(self.tercero_semestres_layout)

    def values_primer_sem(self):
        valasig1= self.slider_t_p_asig1.value() if self.label_value_t_p_asig1.text() != 'NO'  else 0
        valasig2= self.slider_t_p_asig2.value() if self.label_value_t_p_asig2.text() != 'NO'  else 0
        valasig3= self.slider_t_p_asig3.value() if self.label_value_t_p_asig3.text() != 'NO'  else 0
        valasig4= self.slider_t_p_asig4.value() if self.label_value_t_p_asig4.text() != 'NO'  else 0
        valasig5= self.slider_t_p_asig5.value() if self.label_value_t_p_asig5.text() != 'NO'  else 0
        valoraciones={
            self.label_t_p_asig1.text(): valasig1,
            self.label_t_p_asig2.text(): valasig2,
            self.label_t_p_asig3.text(): valasig3,
            self.label_t_p_asig4.text(): valasig4,
            self.label_t_p_asig5.text(): valasig5            
            }
        return valoraciones
       
    def set_values_primer_sem(self,diccionario):
            if diccionario[self.label_t_p_asig1.text()]==0:
                self.slider_t_p_asig1.setValue(1)
                self.slider_t_p_asig1.setEnabled(False)
                self.label_value_t_p_asig1.setText('NO')
                self.check_box_t_p_asig1.setChecked(True)
            else:
                self.slider_t_p_asig1.setEnabled(True)
                self.slider_t_p_asig1.setValue(diccionario[self.label_t_p_asig1.text()])

            if diccionario[self.label_t_p_asig2.text()]==0:
                self.slider_t_p_asig2.setValue(1)
                self.slider_t_p_asig2.setEnabled(False)
                self.label_value_t_p_asig2.setText('NO')
                self.check_box_t_p_asig2.setChecked(True)
            else:
                self.slider_t_p_asig2.setEnabled(True)
                self.slider_t_p_asig2.setValue(diccionario[self.label_t_p_asig2.text()])
 
            if diccionario[self.label_t_p_asig3.text()]==0:
                self.slider_t_p_asig3.setValue(1)
                self.slider_t_p_asig3.setEnabled(False)
                self.label_value_t_p_asig3.setText('NO')
                self.check_box_t_p_asig3.setChecked(True)
            else:
                self.slider_t_p_asig3.setEnabled(True)
                self.slider_t_p_asig3.setValue(diccionario[self.label_t_p_asig3.text()])   
            
            if diccionario[self.label_t_p_asig4.text()]==0:
                self.slider_t_p_asig4.setValue(1)
                self.slider_t_p_asig4.setEnabled(False)
                self.label_value_t_p_asig4.setText('NO')
                self.check_box_t_p_asig4.setChecked(True)
            else:
                self.slider_t_p_asig4.setEnabled(True)
                self.slider_t_p_asig4.setValue(diccionario[self.label_t_p_asig4.text()])
            
            if diccionario[self.label_t_p_asig5.text()]==0:
                self.slider_t_p_asig5.setValue(1)
                self.slider_t_p_asig5.setEnabled(False)
                self.label_value_t_p_asig5.setText('NO')
                self.check_box_t_p_asig5.setChecked(True)
            else:
                self.slider_t_p_asig5.setEnabled(True)
                self.slider_t_p_asig5.setValue(diccionario[self.label_t_p_asig5.text()]) 
       
    def values_segundo_sem(self):
        valasig1= self.slider_t_s_asig1.value() if self.label_value_t_s_asig1.text() != 'NO'  else 0
        valasig2= self.slider_t_s_asig2.value() if self.label_value_t_s_asig2.text() != 'NO'  else 0
        valasig3= self.slider_t_s_asig3.value() if self.label_value_t_s_asig3.text() != 'NO'  else 0
        valasig4= self.slider_t_s_asig4.value() if self.label_value_t_s_asig4.text() != 'NO'  else 0
        valasig5= self.slider_t_s_asig5.value() if self.label_value_t_s_asig5.text() != 'NO'  else 0
        
        valoraciones={
            self.label_t_asig1.text():valasig1,
            self.label_t_asig2.text():valasig2,
            self.label_t_asig3.text():valasig3,
            self.label_t_asig4.text():valasig4,
            self.label_t_asig5.text():valasig5           
        }
        return valoraciones 
    def set_values_segundo_sem(self,diccionario):
            if diccionario[self.label_t_asig1.text()]==0:
                self.slider_t_s_asig1.setValue(1)
                self.slider_t_s_asig1.setEnabled(False)
                self.label_value_t_s_asig1.setText('NO')
                self.check_box_t_s_asig1.setChecked(True)
            else:
                self.slider_t_s_asig1.setEnabled(True)
                self.slider_t_s_asig1.setValue(diccionario[self.label_t_asig1.text()])

            if diccionario[self.label_t_asig2.text()]==0:
                self.slider_t_s_asig2.setValue(1)
                self.slider_t_s_asig2.setEnabled(False)
                self.label_value_t_s_asig2.setText('NO')
                self.check_box_t_s_asig2.setChecked(True)
            else:
                self.slider_t_s_asig2.setEnabled(True)
                self.slider_t_s_asig2.setValue(diccionario[self.label_t_asig2.text()])
 
            if diccionario[self.label_t_asig3.text()]==0:
                self.slider_t_s_asig3.setValue(1)
                self.slider_t_s_asig3.setEnabled(False)
                self.label_value_t_s_asig3.setText('NO')
                self.check_box_t_s_asig3.setChecked(True)
            else:
                self.slider_t_s_asig3.setEnabled(True)
                self.slider_t_s_asig3.setValue(diccionario[self.label_t_asig3.text()])   
            
            if diccionario[self.label_t_asig4.text()]==0:
                self.slider_t_s_asig4.setValue(1)
                self.slider_t_s_asig4.setEnabled(False)
                self.label_value_t_s_asig4.setText('NO')
                self.check_box_t_s_asig4.setChecked(True)
            else:
                self.slider_t_s_asig4.setEnabled(True)
                self.slider_t_s_asig4.setValue(diccionario[self.label_t_asig4.text()])
            
            if diccionario[self.label_t_asig5.text()]==0:
                self.slider_t_s_asig5.setValue(1)
                self.slider_t_s_asig5.setEnabled(False)
                self.label_value_t_s_asig5.setText('NO')
                self.check_box_t_s_asig5.setChecked(True)
            else:
                self.slider_t_s_asig5.setEnabled(True)
                self.slider_t_s_asig5.setValue(diccionario[self.label_t_asig5.text()])    
    def valuechange_slider(self):
        if self.check_box_t_p_asig1.isChecked()!=True:
            self.label_value_t_p_asig1.setText(str(self.slider_t_p_asig1.value()))            
        if self.check_box_t_p_asig2.isChecked()!=True:
            self.label_value_t_p_asig2.setText(str(self.slider_t_p_asig2.value()))
        if self.check_box_t_p_asig3.isChecked()!=True:
            self.label_value_t_p_asig3.setText(str(self.slider_t_p_asig3.value()))
        if self.check_box_t_p_asig4.isChecked()!=True:
            self.label_value_t_p_asig4.setText(str(self.slider_t_p_asig4.value()))
        if self.check_box_t_p_asig5.isChecked()!=True:
            self.label_value_t_p_asig5.setText(str(self.slider_t_p_asig5.value()))
        
        if self.check_box_t_s_asig1.isChecked()!=True:
            self.label_value_t_s_asig1.setText(str(self.slider_t_s_asig1.value()))
        if self.check_box_t_s_asig2.isChecked()!=True:
            self.label_value_t_s_asig2.setText(str(self.slider_t_s_asig2.value()))
        if self.check_box_t_s_asig3.isChecked()!=True:
            self.label_value_t_s_asig3.setText(str(self.slider_t_s_asig3.value()))
        if self.check_box_t_s_asig4.isChecked()!=True:
            self.label_value_t_s_asig4.setText(str(self.slider_t_s_asig4.value()))
        if self.check_box_t_s_asig5.isChecked()!=True:
            self.label_value_t_s_asig5.setText(str(self.slider_t_s_asig5.value()))
        
    def valuechange_checkBox1(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_p_asig1.setEnabled(False)
            self.label_t_p_asig1.setStyleSheet('color: grey; ')
            self.label_value_t_p_asig1.setText('NO')
        else:
            self.slider_t_p_asig1.setEnabled(True)
            self.label_t_p_asig1.setStyleSheet('color: black; ')
            self.label_value_t_p_asig1.setText(str(self.slider_t_p_asig1.value()))
            
    def valuechange_checkBox2(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_p_asig2.setEnabled(False)
            self.label_t_p_asig2.setStyleSheet('color: grey; ')
            self.label_value_t_p_asig2.setText('NO')
        else:
            self.slider_t_p_asig2.setEnabled(True)
            self.label_t_p_asig2.setStyleSheet('color: black; ')
            self.label_value_t_p_asig2.setText(str(self.slider_t_p_asig2.value()))
             
    def valuechange_checkBox3(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_p_asig3.setEnabled(False)
            self.label_t_p_asig3.setStyleSheet('color: grey; ')
            self.label_value_t_p_asig3.setText('NO')
        else:
            self.slider_t_p_asig3.setEnabled(True)
            self.label_t_p_asig3.setStyleSheet('color: black; ')
            self.label_value_t_p_asig3.setText(str(self.slider_t_p_asig3.value()))
    
    def valuechange_checkBox4(self,state):    
        if state == QtCore.Qt.Checked:
            self.slider_t_p_asig4.setEnabled(False)
            self.label_t_p_asig4.setStyleSheet('color: grey; ')
            self.label_value_t_p_asig4.setText('NO')
        else:
            self.slider_t_p_asig4.setEnabled(True)
            self.label_t_p_asig4.setStyleSheet('color: black; ')
            self.label_value_t_p_asig4.setText(str(self.slider_t_p_asig4.value()))
    
    def valuechange_checkBox5(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_p_asig5.setEnabled(False)
            self.label_t_p_asig5.setStyleSheet('color: grey; ')
            self.label_value_t_p_asig5.setText('NO')
        else:
            self.slider_t_p_asig5.setEnabled(True)
            self.label_t_p_asig5.setStyleSheet('color: black; ')
            self.label_value_t_p_asig5.setText(str(self.slider_t_p_asig5.value()))
    
    def valuechange_checkBox2_5(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_s_asig5.setEnabled(False)
            self.label_t_asig5.setStyleSheet('color: grey; ')
            self.label_value_t_s_asig5.setText('NO')
        else:
            self.slider_t_s_asig5.setEnabled(True)
            self.label_t_asig5.setStyleSheet('color: black; ')
            self.label_value_t_s_asig5.setText(str(self.slider_t_s_asig5.value()))    
    
    def valuechange_checkBox2_4(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_s_asig4.setEnabled(False)
            self.label_t_asig4.setStyleSheet('color: grey; ')
            self.label_value_t_s_asig4.setText('NO')
        else:
            self.slider_t_s_asig4.setEnabled(True)
            self.label_t_asig4.setStyleSheet('color: black; ')
            self.label_value_t_s_asig4.setText(str(self.slider_t_s_asig4.value()))
     
               
    def valuechange_checkBox2_3(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_s_asig3.setEnabled(False)
            self.label_t_asig3.setStyleSheet('color: grey; ')
            self.label_value_t_s_asig3.setText('NO')
        else:
            self.slider_t_s_asig3.setEnabled(True)
            self.label_t_asig3.setStyleSheet('color: black; ')
            self.label_value_t_s_asig3.setText(str(self.slider_t_s_asig3.value()))
         
    def valuechange_checkBox2_2(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_s_asig2.setEnabled(False)
            self.label_t_asig2.setStyleSheet('color: grey; ')
            self.label_value_t_s_asig2.setText('NO')
        else:
            self.slider_t_s_asig2.setEnabled(True)
            self.label_t_asig2.setStyleSheet('color: black; ')
            self.label_value_t_s_asig2.setText(str(self.slider_t_s_asig2.value()))
              
    def valuechange_checkBox2_1(self,state):
        if state == QtCore.Qt.Checked:
            self.slider_t_s_asig1.setEnabled(False)
            self.label_t_asig1.setStyleSheet('color: grey; ')
            self.label_value_t_s_asig1.setText('NO')
        else:
            self.slider_t_s_asig1.setEnabled(True)
            self.label_t_asig1.setStyleSheet('color: black; ')
            self.label_value_t_s_asig1.setText(str(self.slider_t_s_asig1.value())) 