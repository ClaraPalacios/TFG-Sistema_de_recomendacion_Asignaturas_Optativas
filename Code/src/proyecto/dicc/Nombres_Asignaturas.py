#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys 


class Nombres_Asignaturas:

    def __init__(self):
        # primer semestre
        self._asignaturas_cuarto_sem1 = [
            'Diseño e Implementación de Sistemas Digitales',
            'Gestión de la Información',
            'Diseño y Mantenimiento del Software',
            'Organización y Gestión de Empresas',
            'Mantenimiento de Equipos Informáticos',
            'Control por Computador',
            'Hardware de Aplicación Específica',
            'Validación y Pruebas',
            'Computación Neuronal y Evolutiva',
            'Programación de Sistemas Operativos',
        ] 
        
        # segundo semestre
        self._asignaturas_cuarto_sem2 = [
            'Sistemas Distribuidos',
            'Sistemas Empotrados y de Tiempo Real',
            'Métodos Formales',
            'Nuevas Tecnologías y Empresa',
            'Minería de Datos',
            'Desarrollo Avanzado de Sistemas Software'
        ]
        
        # primer semestre
        self._asignaturas_tercero_sem1 = [
            'Arquitecturas Paralelas',
            'Sistemas Inteligentes',
            'Gestión de Proyectos',
            'Diseño y Administración de Sistemas y Redes ',
            'Procesadores del Lenguaje'
        ]
        
        # segundo semestre
        self._asignaturas_tercero_sem2 = [ 
            'Programación Concurrente y de Tiempo Real',
            'Seguridad Informática',
            'Aplicaciones de Bases de Datos',
            'Algoritmia',
            'Métodos Numéricos y Optimización'            
        ]
        
        # primer semestre
        self._asignaturas_segundo_sem1 = [
            'Metodología de la Programación',
            'Estadística',
            'Ingeniería del Software',
            'Bases de Datos',
            'Arquitectura de Computadores'
        ]
        
        # segundo semestre
        self._asignaturas_segundo_sem2 = [
            'Estructuras de Datos',
            'Redes',
            'Interacción Hombre-Máquina',
            'Fundamentos de Organización y Gestión de Empresas',
            'Análisis y Diseño de Sistemas',
        ]   
        
        # primer semestre
        self._asignaturas_primero_sem1 = [
            'Fundamentos Deontológicos y Jurídicos de las TIC',
            'Álgebra Lineal',
            'Informática Básica',
            'Fundamentos Físicos de la Informática',
            'Matemática Discreta'
        ]       
        
        # segundo semestre
        self._asignaturas_primero_sem2 = [
            'Inglés Aplicado a la Informática',
            'Cálculo',
            'Programación',
            'Fundamentos de Computadores',
            'Sistemas Operativos'
        ]
        
        self.caracterizacion = {
            'Diseño e Implementación de Sistemas Digitales'     :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (1,"Equipos")],
            'Gestión de la Información'                         :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (1,"Economia"), (0,"Diseño"), (0,"Equipos")],
            'Diseño y Mantenimiento del Software'               :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (0,"Equipos")],
            'Organización y Gestión de Empresas'                :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (1,"Economia"), (0,"Diseño"), (0,"Equipos")],
            'Mantenimiento de Equipos Informáticos'             :[(1,"Matematicas"), (0,"Derecho"), (0,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (1,"Equipos")],
            'Control por Computador'                            :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (1,"Equipos")],
            'Hardware de Aplicación Específica'                 :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (1,"Equipos")],
            'Validación y Pruebas'                              :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (0,"Equipos")],
            'Computación Neuronal y Evolutiva'                  :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (0,"Equipos")],
            'Programación de Sistemas Operativos'               :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (1,"Equipos")],
            'Sistemas Distribuidos'                             :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (0,"Equipos")],
            'Sistemas Empotrados y de Tiempo Real'              :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (1,"Equipos")],
            'Métodos Formales'                                  :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (0,"Equipos")],
            'Nuevas Tecnologías y Empresa'                      :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (0,"Equipos")],
            'Minería de Datos'                                  :[(1,"Matematicas"), (0,"Derecho"), (1,"Programar"), (1,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (0,"Diseño"), (0,"Equipos")],
            'Desarrollo Avanzado de Sistemas Software'          :[(0,"Matematicas"), (0,"Derecho"), (1,"Programar"), (0,"Algoritmos"), (0,"Idiomas"), (0,"Economia"), (1,"Diseño"), (0,"Equipos")]
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
