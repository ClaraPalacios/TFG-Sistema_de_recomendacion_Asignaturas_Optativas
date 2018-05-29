#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

class Dicc():
    """ 
    Clase que contiene los string necesarios para inicializar los datos..
  
    """
    def __init__(self):
        #Ventana incio sesion
        self.vn_proyecto= 'Proyecto Sistema de Recomendacion de Asignaturas Optativas'
        self.vn_archivo = 'Archivo'
        self.vn_salir = 'Salir'
        self.vn_inicia= 'Inicia Sesion'
        self.semestre1 = "Primer semestre"
        self.semestre2 = "Segundo semestre"
        self.graficas = "Gr�ficas"
        self.vn_opciones = "Opciones"
        
        self.op_estadisticas = "Estad�sticas"
        self.op_modelos = "Modelos"
        self.op_valoraciones = "Valoraciones"
        
        self.curso_primero = "Primero"
        self.curso_segundo = "Segundo"
        self.curso_tercero = "Tercero"
        self.curso_cuarto = "Cuarto"

        self.cargar = "Cargar"
        self.guardar = "Guardar"
        self.controles = "Controles"
        self.cursos = "Cursos"
        
        self.filtro_usuarios = "F.C Usuarios "
        self.filtro_productos = "F.C Productos "
        self.filtro_modelos ="F.C Modelos"
        self.f_u_calcular = "Calcular F.C. Usuarios "
        self.f_p_calcular = "Calcular F.C. Productos "
        self.f_m_calcular = "Calcular F.C. Modelos "
        self.ejecucion = "Ejecuci�n"
        self.predicciones = "Predicciones"

        
                #primer semestre
        self.primero_sem1 = "Primer curso, Semestre 1"
        self.primero_semestre1p_p_asig1 = 'Fundamentos Deontol�gicos y Jur�dicos de las TIC'
        self.primero_semestre1p_p_asig2 = '�lgebra Lineal'
        self.primero_semestre1p_p_asig3 = 'Inform�tica B�sica'
        self.primero_semestre1p_p_asig4 = 'Fundamentos F�sicos de la Inform�tica'
        self.primero_semestre1p_p_asig5 = 'Matem�tica Discreta'
        #segundo semestre
        self.primero_sem2 = "Primer curso, Semestre 2"        
        self.primero_semestre2_s_asig1 = 'Ingl�s Aplicado a la Inform�tica'
        self.primero_semestre2_s_asig2 = 'C�lculo'
        self.primero_semestre2_s_asig3 = 'Programaci�n'
        self.primero_semestre2_s_asig4 = 'Fundamentos de Computadores'
        self.primero_semestre2_s_asig5 = 'Sistemas Operativos'
        
        #tercer semestre
        self.segundo_sem1 = "Segundo curso, Semestre 1"
        self.segundo_semestre1p_p_asig1 = 'Metodolog�a de la Programaci�n'
        self.segundo_semestre1p_p_asig2 = 'Estad�stica'
        self.segundo_semestre1p_p_asig3 = 'Ingenier�a del Software'
        self.segundo_semestre1p_p_asig4 = 'Bases de Datos'
        self.segundo_semestre1p_p_asig5 = 'Arquitectura de Computadores'
        
        #cuarto semestre
        self.segundo_sem2 = "Segundo curso, Semestre 2"
        self.segundo_semestre2_s_asig1 = 'Estructuras de Datos'
        self.segundo_semestre2_s_asig2 = 'Redes'
        self.segundo_semestre2_s_asig3 = 'Interacci�n Hombre-M�quina'
        self.segundo_semestre2_s_asig4 = 'Fundamentos de Organizaci�n y Gesti�n de Empresas'
        self.segundo_semestre2_s_asig5 = 'An�lisis y Dise�o de Sistemas'
        
        #quinto semestre
        self.tercero_sem1 = "Tercer curso, Semestre 1"
        self.tercero_semestre1p_p_asig1 = 'Arquitecturas Paralelas'
        self.tercero_semestre1p_p_asig2 = 'Sistemas Inteligentes'
        self.tercero_semestre1p_p_asig3 = 'Gesti�n de Proyectos'
        self.tercero_semestre1p_p_asig4 = 'Dise�o y Administraci�n de Sistemas y Redes '
        self.tercero_semestre1p_p_asig5 =  'Procesadores del Lenguaje'
        
        #sexto semestre
        self.tercero_sem2 = "Tercer curso, Semestre 2"
        self.tercero_semestre2_s_asig1 = 'Programaci�n Concurrente y de Tiempo Real'
        self.tercero_semestre2_s_asig2 = 'Seguridad Inform�tica'
        self.tercero_semestre2_s_asig3 = 'Aplicaciones de Bases de Datos'
        self.tercero_semestre2_s_asig4 = 'Algoritmia'
        self.tercero_semestre2_s_asig5 = 'M�todos Num�ricos y Optimizaci�n'
        
        
        #septimo semestre
        self.cuarto_sem1_1 = "Cuarto curso, Semestre 1: 1-5"
        self.cuarto_sem1_2 = "Cuarto curso, Semestre 1: 5-10"
        self.cuarto_semestre1p_p_asig1 = 'Dise�o e Implementaci�n de Sistemas Digitales'
        self.cuarto_semestre1p_p_asig2 ='Gesti�n de la Informaci�n'
        self.cuarto_semestre1p_p_asig3 ='Dise�o y Mantenimiento del Software'
        self.cuarto_semestre1p_p_asig4 = 'Organizaci�n y Gesti�n de Empresas'
        self.cuarto_semestre1p_p_asig5 = 'Mantenimiento de Equipos Inform�ticos'
        self.cuarto_semestre1p_p_asig6 = 'Control por Computador'
        self.cuarto_semestre1p_p_asig7 = 'Hardware de Aplicaci�n Espec�fica'
        self.cuarto_semestre1p_p_asig8 = 'Validaci�n y Pruebas'
        self.cuarto_semestre1p_p_asig9 = 'Computaci�n Neuronal y Evolutiva'
        self.cuarto_semestre1p_p_asig10 = 'Programaci�n de Sistemas Operativos'
    
        #octavo semestre
        self.cuarto_sem2 = "Cuarto curso, Semestre 2"
        self.cuarto_semestre2_s_asig1 = 'Sistemas Distribuidos'
        self.cuarto_semestre2_s_asig2 = 'Sistemas Empotrados y de Tiempo Real'
        self.cuarto_semestre2_s_asig3 = 'M�todos Formales'
        self.cuarto_semestre2_s_asig4 = 'Nuevas Tecnolog�as y Empresa'
        self.cuarto_semestre2_s_asig5 = 'Miner�a de Datos'
        self.cuarto_semestre2_s_asig5 = 'Miner�a de Datos'
        self.cuarto_semestre2_s_asig6 = 'Desarrollo Avanzado de Sistemas Software'        
        
        #top Asignaturas
        self.top_1_5 = "Top 1-5"
        self.top_5_10 = "Top 5-10"
        self.top_asignaturas1 = "Top asignaturas 1-5"
        self.top_asignaturas2 = "Top asignaturas 5-10"
        
        