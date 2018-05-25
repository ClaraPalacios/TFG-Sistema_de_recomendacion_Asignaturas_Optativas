#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys 


class Nombres_Asignaturas:

    def __init__(self):
        # primer semestre
        self._asignaturas_cuarto_sem1 = [
            'Dise�o e Implementaci�n de Sistemas Digitales',
            'Gesti�n de la Informaci�n',
            'Dise�o y Mantenimiento del Software',
            'Organizaci�n y Gesti�n de Empresas',
            'Mantenimiento de Equipos Inform�ticos',
            'Control por Computador',
            'Hardware de Aplicaci�n Espec�fica',
            'Validaci�n y Pruebas',
            'Computaci�n Neuronal y Evolutiva',
            'Programaci�n de Sistemas Operativos',
        ] 
        
        # segundo semestre
        self._asignaturas_cuarto_sem2 = [
            'Sistemas Distribuidos',
            'Sistemas Empotrados y de Tiempo Real',
            'M�todos Formales',
            'Nuevas Tecnolog�as y Empresa',
            'Miner�a de Datos',
            'Desarrollo Avanzado de Sistemas Software'
        ]
        
        # primer semestre
        self._asignaturas_tercero_sem1 = [
            'Arquitecturas Paralelas',
            'Sistemas Inteligentes',
            'Gesti�n de Proyectos',
            'Dise�o y Administraci�n de Sistemas y Redes ',
            'Procesadores del Lenguaje'
        ]
        
        # segundo semestre
        self._asignaturas_tercero_sem2 = [ 
            'Programaci�n Concurrente y de Tiempo Real',
            'Seguridad Inform�tica',
            'Aplicaciones de Bases de Datos',
            'Algoritmia',
            'M�todos Num�ricos y Optimizaci�n'            
        ]
        
        # primer semestre
        self._asignaturas_segundo_sem1 = [
            'Metodolog�a de la Programaci�n',
            'Estad�stica',
            'Ingenier�a del Software',
            'Bases de Datos',
            'Arquitectura de Computadores'
        ]
        
        # segundo semestre
        self._asignaturas_segundo_sem2 = [
            'Estructuras de Datos',
            'Redes',
            'Interacci�n Hombre-M�quina',
            'Fundamentos de Organizaci�n y Gesti�n de Empresas',
            'An�lisis y Dise�o de Sistemas',
        ]   
        
        # primer semestre
        self._asignaturas_primero_sem1 = [
            'Fundamentos Deontol�gicos y Jur�dicos de las TIC',
            '�lgebra Lineal',
            'Inform�tica B�sica',
            'Fundamentos F�sicos de la Inform�tica',
            'Matem�tica Discreta'
        ]       
        
        # segundo semestre
        self._asignaturas_primero_sem2 = [
            'Ingl�s Aplicado a la Inform�tica',
            'C�lculo',
            'Programaci�n',
            'Fundamentos de Computadores',
            'Sistemas Operativos'
        ]
        
        self.caracterizacion = {
            'Dise�o e Implementaci�n de Sistemas Digitales'     :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (1,"Equipos")],
            'Gesti�n de la Informaci�n'                         :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (1,"Economia"), (0,"Dise�o"), (0,"Equipos")],
            'Dise�o y Mantenimiento del Software'               :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (0,"Equipos")],
            'Organizaci�n y Gesti�n de Empresas'                :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (1,"Economia"), (0,"Dise�o"), (0,"Equipos")],
            'Mantenimiento de Equipos Inform�ticos'             :[(1,"Matematicas"), (0,"Derecho"), (0,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (1,"Equipos")],
            'Control por Computador'                            :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (1,"Equipos")],
            'Hardware de Aplicaci�n Espec�fica'                 :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (1,"Equipos")],
            'Validaci�n y Pruebas'                              :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (0,"Equipos")],
            'Computaci�n Neuronal y Evolutiva'                  :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (0,"Equipos")],
            'Programaci�n de Sistemas Operativos'               :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (1,"Equipos")],
            'Sistemas Distribuidos'                             :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (0,"Equipos")],
            'Sistemas Empotrados y de Tiempo Real'              :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (1,"Equipos")],
            'M�todos Formales'                                  :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (0,"Equipos")],
            'Nuevas Tecnolog�as y Empresa'                      :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (0,"Equipos")],
            'Miner�a de Datos'                                  :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Dise�o"), (0,"Equipos")],
            'Desarrollo Avanzado de Sistemas Software'          :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Dise�o"), (0,"Equipos")]
            }
        
    def get_caracterizacion(self):
        return self.caracterizacion
    
    def get_asignaturas_cuarto(self):
        return self._asignaturas_cuarto_sem1 + self._asignaturas_cuarto_sem2

    def get_asignaturas_cuarto_sem1(self):
        return self._asignaturas_cuarto_sem1

    def get_asignaturas_cuarto_sem2(self):
        return self._asignaturas_cuarto_sem2
    
    def get_asignaturas_tercero(self):
        return self._asignaturas_tercero_sem1 + self._asignaturas_tercero_sem2

    def get_asignaturas_tercero__sem1(self):
        return self._asignaturas_tercero_sem1

    def get_asignaturas_tercero__sem2(self):
        return self._asignaturas_tercero_sem2
    
    def get_asignaturas_segundo(self):
        return self._asignaturas_segundo_sem1 + self._asignaturas_segundo_sem2

    def get_asignaturas_segundo_sem1(self):
        return self._asignaturas_segundo_sem1

    def get_asignaturas_segundo_sem2(self):
        return self._asignaturas_segundo_sem2
    
    def get_asignaturas_primero(self):  
        return self._asignaturas_primero_sem1 + self._asignaturas_primero_sem2

    def get_asignaturas_primero_sem1(self):
        return self._asignaturas_primero_sem1

    def get_asignaturas_primero_sem2(self):
        return self._asignaturas_primero_sem2
