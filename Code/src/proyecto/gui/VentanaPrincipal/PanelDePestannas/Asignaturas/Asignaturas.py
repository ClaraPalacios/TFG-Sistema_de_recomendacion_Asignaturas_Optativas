
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import pickle
from proyecto.dicc.Dicc import Dicc;
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Asignaturas.PrimeroCurso import PrimeroCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Asignaturas.SegundoCurso import SegundoCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Asignaturas.TerceroCurso import TerceroCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Asignaturas.CuartoCurso import CuartoCurso
from proyecto.dicc.Dicc import Dicc
class Asignaturas(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Asignaturas, self).__init__(parent)
        self.dicc = Dicc()
        self.tab1UI()
        
    def tab1UI(self):
        
        #         Button : Entrar y salir
        self.primero = QtWidgets.QPushButton(self.dicc.curso_primero, self)
        self.primero.setToolTip('Pulsa para entrar')
        self.primero.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.primero.setFont(fontTex)
        self.primero.clicked.connect(lambda: self.hideShow_frame(1))

        #         Button : Entrar y salir
        self.segundo = QtWidgets.QPushButton(self.dicc.curso_segundo, self)
        self.segundo.setToolTip('Pulsa para entrar')
        self.segundo.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.segundo.setFont(fontTex)
        self.segundo.clicked.connect(lambda: self.hideShow_frame(2))

        
        #         Button : Entrar y salir
        self.tercero = QtWidgets.QPushButton(self.dicc.curso_tercero, self)
        self.tercero.setToolTip('Pulsa para entrar')
        self.tercero.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.tercero.setFont(fontTex)
        self.tercero.clicked.connect(lambda: self.hideShow_frame(3))

        #         Button : Entrar y salir
        self.cuarto = QtWidgets.QPushButton(self.dicc.curso_cuarto, self)
        self.cuarto.setToolTip('Pulsa para entrar')
        self.cuarto.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.cuarto.setFont(fontTex)
        self.cuarto.clicked.connect(lambda: self.hideShow_frame(4))  
        
        self.save = QtWidgets.QPushButton(self.dicc.guardar, self)
        self.save.setToolTip('Pulsa para entrar')
        self.save.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.save.setFont(fontTex)
        self.save.clicked.connect(self.save_valoraciones)  

        self.load = QtWidgets.QPushButton(self.dicc.cargar, self)
        self.load.setToolTip('Pulsa para entrar')
        self.load.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.load.setFont(fontTex)
        self.load.clicked.connect(self.load_valoraciones) 
         
        self.asignaturas_layout = QtWidgets.QVBoxLayout()

        self.asignaturas_layout.addWidget(self.primero)     
        self.asignaturas_layout.addWidget(self.segundo)     
        self.asignaturas_layout.addWidget(self.tercero)     
        self.asignaturas_layout.addWidget(self.cuarto)
        
        self.save_asignaturas = QtWidgets.QVBoxLayout()
        self.save_asignaturas.addWidget(self.save)
        self.save_asignaturas.addWidget(self.load)
        
        self.save_asignaturas_groupBox = QtWidgets.QGroupBox()
        self.save_asignaturas_groupBox.setTitle(self.dicc.controles) 
        self.save_asignaturas_groupBox.setLayout(self.save_asignaturas)
        
        self.pestana1_botones_groupBox = QtWidgets.QGroupBox()
        self.pestana1_botones_groupBox.setTitle(self.dicc.cursos) 
        self.pestana1_botones_groupBox.setLayout(self.asignaturas_layout) 
        
        self.primero_semestres_frame=PrimeroCurso();
        self.segundo_semestres_frame=SegundoCurso();
        self.tercero_semestres_frame=TerceroCurso();
        self.cuarto_semestres_frame=CuartoCurso();
        
        self.segundo_semestres_frame.segundo_semestres_frame.hide()
        self.tercero_semestres_frame.tercero_semestres_frame.hide()
        self.cuarto_semestres_frame.cuarto_semestres_frame.hide()

        self.controles = QtWidgets.QVBoxLayout()

        self.controles.addWidget(self.pestana1_botones_groupBox) 
        self.controles.addWidget(self.save_asignaturas_groupBox)
        
        self.pestanna1_layout = QtWidgets.QHBoxLayout()
 
        
        self.pestanna1_layout.addLayout(self.controles)   
        self.pestanna1_layout.addWidget(self.primero_semestres_frame.primero_semestres_frame)   
        self.pestanna1_layout.addWidget(self.segundo_semestres_frame.segundo_semestres_frame)   
        self.pestanna1_layout.addWidget(self.tercero_semestres_frame.tercero_semestres_frame)   
        self.pestanna1_layout.addWidget(self.cuarto_semestres_frame.cuarto_semestres_frame) 
        self.load_valoraciones()
        
        
    def save_valoraciones(self):
        

        d= self.primero_semestres_frame.values_segundo_sem()
        d.update(self.primero_semestres_frame.values_primer_sem())
        
        d.update(self.segundo_semestres_frame.values_primer_sem())
        d.update(self.segundo_semestres_frame.values_segundo_sem())
        
        d.update(self.tercero_semestres_frame.values_primer_sem())
        d.update(self.tercero_semestres_frame.values_segundo_sem())
        
        d.update(self.cuarto_semestres_frame.values_primer_sem())
        d.update(self.cuarto_semestres_frame.values_segundo_sem())
        with open('valoraciones.pickle', 'wb') as handle:
            pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_valoraciones(self):
        try:
            with open('valoraciones.pickle', 'rb') as handle:
                b = pickle.load(handle)
                self.primero_semestres_frame.set_values_primer_sem(b)
                self.primero_semestres_frame.set_values_segundo_sem(b)
                
                self.segundo_semestres_frame.set_values_primer_sem(b)
                self.segundo_semestres_frame.set_values_segundo_sem(b)
                
                self.tercero_semestres_frame.set_values_primer_sem(b)
                self.tercero_semestres_frame.set_values_segundo_sem(b)
                
                self.cuarto_semestres_frame.set_values_primer_sem(b)
                self.cuarto_semestres_frame.set_values_segundo_sem(b)
                print(b)
        except:
            pass

    def hideShow_frame(self,i):
        """
        
        """   
        if i==1:            
            self.primero_semestres_frame.primero_semestres_frame.show()
            self.segundo_semestres_frame.segundo_semestres_frame.hide()
            self.tercero_semestres_frame.tercero_semestres_frame.hide()
            self.cuarto_semestres_frame.cuarto_semestres_frame.hide()
        if i==2:
            self.primero_semestres_frame.primero_semestres_frame.hide()
            self.segundo_semestres_frame.segundo_semestres_frame.show()
            self.tercero_semestres_frame.tercero_semestres_frame.hide()
            self.cuarto_semestres_frame.cuarto_semestres_frame.hide()
        if i==3:
            self.primero_semestres_frame.primero_semestres_frame.hide()
            self.segundo_semestres_frame.segundo_semestres_frame.hide()
            self.tercero_semestres_frame.tercero_semestres_frame.show()
            self.cuarto_semestres_frame.cuarto_semestres_frame.hide()            
        if i==4:
            self.primero_semestres_frame.primero_semestres_frame.hide()
            self.segundo_semestres_frame.segundo_semestres_frame.hide()
            self.tercero_semestres_frame.tercero_semestres_frame.hide()
            self.cuarto_semestres_frame.cuarto_semestres_frame.show()

#         self.tab1.setLayout(self.pestanna1_layout)