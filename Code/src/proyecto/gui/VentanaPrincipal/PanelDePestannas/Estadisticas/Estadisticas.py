#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from proyecto.dicc.Dicc import Dicc
from proyecto.dicc.Nombres_Asignaturas import Nombres_Asignaturas
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Estadisticas.PrimeroCurso import PrimeroCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Estadisticas.SegundoCurso import SegundoCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Estadisticas.TerceroCurso import TerceroCurso
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Estadisticas.CuartoCurso import CuartoCurso
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure
from proyecto.core.I_O.I_O_Datos_API_Rest import I_O_Datos_API_Rest

class Estadisticas(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Estadisticas, self).__init__(parent)
        IO_DATOS=I_O_Datos_API_Rest('http://claratfg2.pythonanywhere.com/Valoraciones_Get_All')
        self.tabla=IO_DATOS.obtener_datos()
        self.tabla=IO_DATOS.transfor_datos(self.tabla)
        self.media_or_mediana=0
        
        self.dictMedias={}
        self.dictMedian={}
        self.dictMax={}
        self.dictMin={}
        for i in self.tabla.columns:
            self.dictMedias[i]=self.tabla[i].mean()
            self.dictMedian[i]=self.tabla[i].median()
            self.dictMax[i]=self.tabla[i].max()
            self.dictMin[i]=self.tabla[i].min()
            
        self.dicc = Dicc()
        
        self.nombresAsigs=Nombres_Asignaturas()
        
        self.tab3UI()
        
    def tab3UI(self):

        
        
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
        
        self.media = QtWidgets.QPushButton("Media", self)
        self.media.setToolTip('Pulsa para entrar')
        self.media.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.media.setFont(fontTex)
        self.media.clicked.connect(lambda: self.media_or_mediana_frame(0))

        #         Button : Entrar y salir
        self.median = QtWidgets.QPushButton("Mediana", self)
        self.median.setToolTip('Pulsa para entrar')
        self.median.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.median.setFont(fontTex)
        self.median.clicked.connect(lambda: self.media_or_mediana_frame(1))  
        
        self.maximos = QtWidgets.QPushButton("Maximos", self)
        self.maximos.setToolTip('Pulsa para entrar')
        self.maximos.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.maximos.setFont(fontTex)
        self.maximos.clicked.connect(lambda: self.media_or_mediana_frame(2))

        #         Button : Entrar y salir
        self.minimos = QtWidgets.QPushButton("Minimos", self)
        self.minimos.setToolTip('Pulsa para entrar')
        self.minimos.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.minimos.setFont(fontTex)
        self.minimos.clicked.connect(lambda: self.media_or_mediana_frame(3))  
        
        self.pestanna3 = QtWidgets.QVBoxLayout() 
        self.pestanna3.addWidget(self.primero)
        self.pestanna3.addWidget(self.segundo)
        self.pestanna3.addWidget(self.tercero)
        self.pestanna3.addWidget(self.cuarto)
        
        self.pestanna3_types = QtWidgets.QVBoxLayout() 
        self.pestanna3_types.addWidget(self.media)
        self.pestanna3_types.addWidget(self.median)
        self.pestanna3_types.addWidget(self.maximos)
        self.pestanna3_types.addWidget(self.minimos)

        
        self.controles_groupBox = QtWidgets.QGroupBox()
        self.controles_groupBox.setTitle("Cursos") 
        self.controles_groupBox.setLayout(self.pestanna3)
        
        self.medidas_groupBox = QtWidgets.QGroupBox()
        self.medidas_groupBox.setTitle("Medida") 
        self.medidas_groupBox.setLayout(self.pestanna3_types)
        
        self.controles_types = QtWidgets.QVBoxLayout() 
        self.controles_types.addWidget(self.controles_groupBox)
        self.controles_types.addWidget(self.medidas_groupBox)

        
        self.primero_frame=PrimeroCurso();
        self.segundo_frame=SegundoCurso();
        self.tercero_frame=TerceroCurso();
        self.cuarto_frame=CuartoCurso();
        
        
        self.static_canvas = FigureCanvas(Figure(figsize=(10, 5),dpi=100))
        self._static_ax = self.static_canvas.figure.subplots(  sharey=True)
        
        self.segundo_frame.segundo_frame.hide()
        self.tercero_frame.tercero_frame.hide()
        self.cuarto_frame.cuarto_frame.hide()
        self.pinta_medias_primero(self.dictMedias)       


        self.graph_layout = QtWidgets.QVBoxLayout() 
        self.graph_layout.addStretch(1)      
        self.graph_layout.addWidget(self.static_canvas)
        self.graph_layout.addStretch(1)      


        self.graph_groupBox = QtWidgets.QGroupBox()
        self.graph_groupBox.setTitle("Gráfica de Medias") 
        self.graph_groupBox.setLayout(self.graph_layout)
        

        
        self.leyenda_layout = QtWidgets.QHBoxLayout()    
        self.leyenda_layout.addWidget(self.primero_frame.primero_frame)   
        self.leyenda_layout.addWidget(self.segundo_frame.segundo_frame)   
        self.leyenda_layout.addWidget(self.tercero_frame.tercero_frame)   
        self.leyenda_layout.addWidget(self.cuarto_frame.cuarto_frame) 
        
        self.leyenda_groupBox = QtWidgets.QGroupBox()
        self.leyenda_groupBox.setTitle("Leyenda") 
        self.leyenda_groupBox.setLayout(self.leyenda_layout)
        
        self.estadisticas_layout = QtWidgets.QHBoxLayout()    
        self.estadisticas_layout.addWidget(self.leyenda_groupBox)   
        self.estadisticas_layout.addWidget(self.graph_groupBox)

        self.estadisticas_groupBox = QtWidgets.QGroupBox()
        self.estadisticas_groupBox.setTitle("Estadisticas") 
        self.estadisticas_groupBox.setLayout(self.estadisticas_layout)
                        
        self.pestanna3_layout = QtWidgets.QHBoxLayout()    
        self.pestanna3_layout.addLayout(self.controles_types)   
        self.pestanna3_layout.addStretch(1) 
        self.pestanna3_layout.addWidget(self.estadisticas_groupBox) 
        self.pestanna3_layout.addStretch(1)

        
    def hideShow_frame(self,i):
        """
        
        """   
        value=self.dictMedias if self.media_or_mediana==0 else self.dictMedian if self.media_or_mediana==1 else self.dictMax if self.media_or_mediana==2 else self.dictMin
        if i==1: 
            self.pinta_medias_primero(value )
            self.primero_frame.primero_frame.show()            
            self.segundo_frame.segundo_frame.hide()
            self.tercero_frame.tercero_frame.hide()
            self.cuarto_frame.cuarto_frame.hide()
        if i==2:
            self.pinta_medias_segundo(value)
            self.primero_frame.primero_frame.hide()
            self.segundo_frame.segundo_frame.show()
            self.tercero_frame.tercero_frame.hide()
            self.cuarto_frame.cuarto_frame.hide()

        if i==3:
            self.pinta_medias_tercero(value)
            self.primero_frame.primero_frame.hide()
            self.segundo_frame.segundo_frame.hide()
            self.tercero_frame.tercero_frame.show()
            self.cuarto_frame.cuarto_frame.hide() 
           
        if i==4:
            self.pinta_medias_cuarto(value)
            self.primero_frame.primero_frame.hide()
            self.segundo_frame.segundo_frame.hide()
            self.tercero_frame.tercero_frame.hide()
            self.cuarto_frame.cuarto_frame.show()

    def pinta_medias_primero(self,dictMedias):        
        self.get_values_curso(dictMedias,self.nombresAsigs.get_asignaturas_primero())

                                   
    def pinta_medias_segundo(self,dictMedias):        
        self.get_values_curso(dictMedias,self.nombresAsigs.get_asignaturas_segundo())
            
    def pinta_medias_tercero(self,dictMedias):        
        self.get_values_curso(dictMedias,self.nombresAsigs.get_asignaturas_tercero())

    def pinta_medias_cuarto(self,dictMedias):        
        self.get_values_curso(dictMedias,self.nombresAsigs.get_asignaturas_cuarto())

    
    def pinta_asig_valor(self,asig,valor):
        for i,j in zip(asig,valor):
            self._static_ax.bar(i,j)
            
    def get_values_curso(self,dictMedias,curso):
        vals=[]
        labels=[]            
        ii=1
        for i in curso:
            if i=='Álgebra Lineal':
                i='álgebra Lineal'
            vals.append(dictMedias[i])
            labels.append('A'+str(ii))
            ii+=1              
        self._static_ax.cla()
        self.pinta_asig_valor(labels, vals)
        
        
    def media_or_mediana_frame(self,i):
        self.media_or_mediana=i
        value="Gráfica de Medias" if self.media_or_mediana==0 else "Gráfica de Medianas" if self.media_or_mediana==1 else "Gráfica de Maximos" if self.media_or_mediana==2 else "Gráfica de Minimos"
        self.graph_groupBox.setTitle(value) 
