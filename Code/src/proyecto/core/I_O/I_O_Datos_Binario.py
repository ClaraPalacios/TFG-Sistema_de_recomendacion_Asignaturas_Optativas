#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import pickle
import pandas as pd
import numpy as np
from proyecto.core.I_O.I_I_O_Datos import I_I_O_Datos

class I_O_Datos_Binario(I_I_O_Datos):
    def __init__(self,nombreArchivo):
        super().__init__(nombreArchivo)
    #formato binario
    def obtener_datos(self):
        archivo = open(self._nombreArchivo, "rb")
        tablaDatos = pickle.load(archivo)
        archivo.close()
        return tablaDatos
    
    def guardarDatos(self, tabla1):
        archivo = open(self._nombreArchivo, "wb")
        pickle.dump(tabla1, archivo)
        archivo.close()
        
    def transfor_datos(self,tabla):
        #almacenar en un diccionario de diccionarios cuya clave sea el usuario, y como valor un conjunto de  diccionarios
        #(clave=nombre asignatura, valor=ponderacion). No introducimos el Token ni la fecha en la que se realizó el cuestionario. 
        asignaturas= list(tabla.columns)
        diccAsi={}
        diccAsi.setdefault(1,{})
        for k in asignaturas:
            if k != 'Token'and k!='Submitted At':
                for i, j in zip(tabla[k], range(len(tabla)) ):
                    diccAsi.setdefault(j,{})
                    diccAsi[j][k]=i
        tabla1 = pd.DataFrame.from_dict(diccAsi)
        tabla1= tabla1.T
        #transformamos los vacíos en NaN para evitar el error de calcular el coeficiente de correlación de pearson entre un int y un string ('' equivale a un str)
        tabla1= tabla1.replace('', np.nan, regex=True)
        return tabla1