#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from proyecto.gui.VentanaPrincipal.PanelDePestannas.Modelos.TopCuartoFrame import TopCuartoFrame
# from proyecto.core.I_O.I_O_Datos_Binario import I_O_Datos_Binario
from proyecto.core.I_O.I_O_Datos_API_Rest import I_O_Datos_API_Rest
from proyecto.core.Filtros.F_B_Memoria.util.Distancias import Distancias
from proyecto.core.Filtros.F_B_Memoria.Usuarios.Filtro_Basado_Usuarios import Filtro_Basado_Usuarios
from proyecto.core.Filtros.F_B_Memoria.Productos.Filtro_Basado_Productos import Filtro_Basado_Productos
from proyecto.dicc.Nombres_Asignaturas import Nombres_Asignaturas
from proyecto.dicc.Dicc import Dicc
import operator
import itertools
import pickle
import pandas as pd
class Modelos(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Modelos, self).__init__(parent)
        self.dicc = Dicc()  

#         IO_DATOS = I_O_Datos_Binario('archivoDatos.bin')   
#         self.tabla = IO_DATOS.obtener_datos()
#         self.tabla = IO_DATOS.transfor_datos(self.tabla)
#         
        IO_DATOS=I_O_Datos_API_Rest('http://claratfg2.pythonanywhere.com/Valoraciones_Get_All')
        self.tabla=IO_DATOS.obtener_datos()
        self.tabla=IO_DATOS.transfor_datos(self.tabla)
        
        self.nombres_Asignaturas=Nombres_Asignaturas()
        self.tab2UI()
        
    def tab2UI(self):
        
        #         Button : Entrar y salir
        self.filtro1 = QtWidgets.QPushButton(self.dicc.filtro_usuarios, self)
        self.filtro1.setToolTip('Pulsa para entrar')
        self.filtro1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.filtro1.setFont(fontTex)
        self.filtro1.clicked.connect(self.actualiza_datos_Modelo_1)  

        
        #         Button : Entrar y salir
        self.filtro2 = QtWidgets.QPushButton(self.dicc.filtro_productos, self)
        self.filtro2.setToolTip('Pulsa para entrar')
        self.filtro2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.filtro2.setFont(fontTex)
        self.filtro2.clicked.connect(self.actualiza_datos_Modelo_2)  
        self.filtro2.setEnabled(False)
        
        #         Button : Entrar y salir
        self.filtro3 = QtWidgets.QPushButton(self.dicc.filtro_modelos, self)
        self.filtro3.setToolTip('Pulsa para entrar')
        self.filtro3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.filtro3.setFont(fontTex)
        self.filtro3.clicked.connect(self.actualiza_datos_Modelo_3)  
        self.filtro3.setEnabled(False)

        self.modelos_layout = QtWidgets.QVBoxLayout()
        self.modelos_layout.addWidget(self.filtro1)
        self.modelos_layout.addWidget(self.filtro2)
        self.modelos_layout.addWidget(self.filtro3)
        
        self.pestana2_botones_groupBox = QtWidgets.QGroupBox()
        self.pestana2_botones_groupBox.setTitle(self.dicc.op_modelos) 
        self.pestana2_botones_groupBox.setLayout(self.modelos_layout) 
        
        #         Button : Entrar y salir
        self.calcular_filtro1 = QtWidgets.QPushButton(self.dicc.f_u_calcular, self)
        self.calcular_filtro1.setToolTip('Pulsa para entrar')
        self.calcular_filtro1.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.calcular_filtro1.setFont(fontTex)
        self.calcular_filtro1.clicked.connect(self.ejecutar_modelo1)  
        
        #         Button : Entrar y salir
        self.calcular_filtro2 = QtWidgets.QPushButton(self.dicc.f_p_calcular, self)
        self.calcular_filtro2.setToolTip('Pulsa para entrar')
        self.calcular_filtro2.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.calcular_filtro2.setFont(fontTex)
        self.calcular_filtro2.clicked.connect(self.ejecutar_modelo2)  

        #         Button : Entrar y salir
        self.calcular_filtro3 = QtWidgets.QPushButton(self.dicc.f_m_calcular, self)
        self.calcular_filtro3.setToolTip('Pulsa para entrar')
        self.calcular_filtro3.setStyleSheet('color: black; ')
        fontTex = QtGui.QFont("ini_time", 15, QtGui.QFont.Bold, True)
        self.calcular_filtro3.setFont(fontTex)
#         ·self.calcular_filtro3.clicked.connect(self.ejecutar_modelo3)  
        
        self.ejecucion_modelos_layout = QtWidgets.QVBoxLayout()
        self.ejecucion_modelos_layout.addWidget(self.calcular_filtro1)
        self.ejecucion_modelos_layout.addWidget(self.calcular_filtro2)
        self.ejecucion_modelos_layout.addWidget(self.calcular_filtro3)
        
        self.pestana2_botones_ejecucion_groupBox = QtWidgets.QGroupBox()
        self.pestana2_botones_ejecucion_groupBox.setTitle(self.dicc.ejecucion) 
        self.pestana2_botones_ejecucion_groupBox.setLayout(self.ejecucion_modelos_layout) 
        
        self.top_cuarto_semestres_frame = TopCuartoFrame();       

        self.opciones_pestana2 = QtWidgets.QVBoxLayout()
        self.opciones_pestana2.addWidget(self.pestana2_botones_groupBox)
        self.opciones_pestana2.addWidget(self.pestana2_botones_ejecucion_groupBox)
        
        self.pestanna2 = QtWidgets.QHBoxLayout()
        self.pestanna2.addLayout(self.opciones_pestana2)
        self.pestanna2.addWidget(self.top_cuarto_semestres_frame.top_cuarto_semestres_frame)
        self.ejecutar_modelo1()
         
    def ejecutar_modelo1(self):
        try:
            print("Filtro_Basado_Usuarios")
            self.tabla=self.tabla.append(pd.DataFrame([self.load_valoraciones()]),ignore_index=True)
    
            distancias = Distancias()
            filtro_Basado_Usuarios = Filtro_Basado_Usuarios(self.tabla, distancias.coef_corr_pearson)
            
            usuario = self.tabla.shape[0]-1
            predic = dict(filtro_Basado_Usuarios.calcula_Prediccion_Cuarto(usuario))
            predic = sorted(predic.items(), key=operator.itemgetter(1), reverse=True)
            self.predict_model1 = predic
            self.actualiza_datos_Modelo_1()
            
            self.filtro1.setEnabled(True)
            
            predic= list(itertools.islice(predic, 10))
            
            self.top_cuarto_semestres_frame._static_ax.cla()
            self.top_cuarto_semestres_frame.pinta_primera_grafica([ seq[0] for seq in predic ], [ seq[1] for seq in predic ])
            
            porcentajes=self.carazterizacion_calculo(predic)
            self.top_cuarto_semestres_frame._static_ax2.cla()
            self.top_cuarto_semestres_frame.pinta_segunda_grafica(porcentajes.keys(),porcentajes.values()) 
            
            self.tabla=self.tabla.drop(self.tabla.index[[self.tabla.shape[0]-1]])
    
            print("------------------------------------------------------------------------------------")
        except:
            pass
    def ejecutar_modelo2(self):
        try:
            print("Filtro_Basado_Productos")
            self.tabla=self.tabla.append(pd.DataFrame([self.load_valoraciones()]),ignore_index=True)
            distancias = Distancias()
            filtro_Basado_Productos = Filtro_Basado_Productos(self.tabla, distancias.coef_corr_pearson)
            
            usuario = self.tabla.shape[0]-1
            predic = dict(filtro_Basado_Productos.calcula_Prediccion_Cuarto(usuario))
            predic = sorted(predic.items(), key=operator.itemgetter(1), reverse=True)
            print("------------------------------------------------------------------------------------")
            self.predict_model2 = predic
            self.actualiza_datos_Modelo_2()
            self.filtro2.setEnabled(True)
            
            predic= list(itertools.islice(predic, 10))
            
            self.top_cuarto_semestres_frame._static_ax.cla()
            self.top_cuarto_semestres_frame.pinta_primera_grafica([ seq[0] for seq in predic ], [ seq[1] for seq in predic ])
            
            porcentajes=self.carazterizacion_calculo(predic)
            self.top_cuarto_semestres_frame._static_ax2.cla()
            self.top_cuarto_semestres_frame.pinta_segunda_grafica(porcentajes.keys(),porcentajes.values()) 
            
            self.tabla=self.tabla.drop(self.tabla.index[[self.tabla.shape[0]-1]])
        except:
            pass
    def ejecutar_modelo3(self):
        
        
        self.filtro3.setEnabled(True)

        pass
    def load_valoraciones(self):
        try:
            with open('valoraciones.pickle', 'rb') as handle:
                return pickle.load(handle)
        except:
            pass            
    def actualiza_datos_Modelo_1(self):
        n = 0
        for k in self.predict_model1:
            i, j = k
            if n > 9:
                break
            self.actualiza_labels(n, i, j)
            n += 1
         
        predic= list(itertools.islice(self.predict_model1, 10))
        
        self.top_cuarto_semestres_frame._static_ax.cla()
        self.top_cuarto_semestres_frame.pinta_primera_grafica([ seq[0] for seq in predic ], [ seq[1] for seq in predic ])   
        
        porcentajes=self.carazterizacion_calculo(predic)
        self.top_cuarto_semestres_frame._static_ax2.cla()
        self.top_cuarto_semestres_frame.pinta_segunda_grafica(porcentajes.keys(),porcentajes.values()) 

        
    def actualiza_datos_Modelo_2(self):
        n = 0
        for k in self.predict_model2:
            i, j = k
            if n > 9:
                break
            self.actualiza_labels(n, i, j)
            n += 1
        predic= list(itertools.islice(self.predict_model2, 10))
        
        self.top_cuarto_semestres_frame._static_ax.cla()
        self.top_cuarto_semestres_frame.pinta_primera_grafica([ seq[0] for seq in predic ], [ seq[1] for seq in predic ]) 
        
        porcentajes=self.carazterizacion_calculo(predic)
        self.top_cuarto_semestres_frame._static_ax2.cla()
        self.top_cuarto_semestres_frame.pinta_segunda_grafica(porcentajes.keys(),porcentajes.values()) 


        
        
    def carazterizacion_calculo(self,predic): 
        
        dic={"Matematicas":0,
             "Derecho":0,
             "Programar":0,
             "Algoritmos":0,
             "Idiomas":0,
             "Economia":0,
             "Diseño":0,
             "Equipos":0,
            }
        for i in list(itertools.islice(predic, 10)):
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][0][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][0][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][1][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][1][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][2][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][2][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][3][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][3][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][4][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][4][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][5][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][5][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][6][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][6][0]
            dic[self.nombres_Asignaturas.caracterizacion[i[0]][7][1]]+=self.nombres_Asignaturas.caracterizacion[i[0]][7][0]
        sorted_x = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        sorted_x=dict(itertools.islice(sorted_x, 4))
        total=sum(sorted_x.values())
        for i,j in sorted_x.items():
            sorted_x[i]=round((j*100)/total,0)
        return sorted_x
    def actualiza_datos_Modelo_3(self):
        pass
#         n = 0
#         if self.predict_model3 != None:
#             for k in self.predict_model3:
#                 i, j = k
#                 if n > 9:
#                     break
#                 self.actualiza_labels(n, i, j)
#                 n += 1

    def actualiza_labels(self, n, i, j):

        if n == 0:
            self.top_cuarto_semestres_frame.label_top_c_p_asig1.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_p_asig1.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_p_asig1.setText(str(round(j, 0)) + " ")
        if n == 1:
            self.top_cuarto_semestres_frame.label_top_c_p_asig2.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_p_asig2.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_p_asig2.setText(str(round(j, 0)) + " ")
              
        if n == 2:
            self.top_cuarto_semestres_frame.label_top_c_p_asig3.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_p_asig3.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_p_asig3.setText(str(round(j, 0)) + " ")
              
        if n == 3:
            self.top_cuarto_semestres_frame.label_top_c_p_asig4.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_p_asig4.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_p_asig4.setText(str(round(j, 0)) + " ")
              
        if n == 4:
            self.top_cuarto_semestres_frame.label_top_c_p_asig5.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_p_asig5.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_p_asig5.setText(str(round(j, 0)) + " ")    
#                     
        if n == 5:
            self.top_cuarto_semestres_frame.label_top_c_asig1.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_asig1.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_s_asig1.setText(str(round(j, 0)) + " ")                   
        
        if n == 6:
            self.top_cuarto_semestres_frame.label_top_c_asig2.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_asig2.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_s_asig2.setText(str(round(j, 0)) + " ")                
               
        if n == 7:
            self.top_cuarto_semestres_frame.label_top_c_asig3.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_asig3.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_s_asig3.setText(str(round(j, 0)) + " ")                 
               
        if n == 8:
            self.top_cuarto_semestres_frame.label_top_c_asig4.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_asig4.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_s_asig4.setText(str(round(j, 0)) + " ")                 
               
        if n == 9:
            self.top_cuarto_semestres_frame.label_top_c_asig5.setText(i)
            self.top_cuarto_semestres_frame.label_top_c_asig5.setToolTip("Asignatura número: "+str(n+1) )
            self.top_cuarto_semestres_frame.label_value_top_c_s_asig5.setText(str(round(j, 0)) + "  ")
