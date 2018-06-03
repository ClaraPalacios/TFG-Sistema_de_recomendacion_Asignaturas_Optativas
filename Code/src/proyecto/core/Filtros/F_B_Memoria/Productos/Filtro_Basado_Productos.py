# -*- coding: latin1 -*-
import pandas as pd
from proyecto.core.Filtros.F_B_Memoria.IFiltro_Memoria import IFiltro_Memoria
from proyecto.core.Filtros.F_B_Memoria.util.Matriz_Similitud import Matriz_Similitud
from proyecto.dicc.Nombres_Asignaturas import Nombres_Asignaturas

class Filtro_Basado_Productos(IFiltro_Memoria):
    def __init__(self,tabla,similitud):
        self._tabla=tabla
        self.similitud=similitud
        self.matriz_similitud=Matriz_Similitud(self.similitud)
        self.matrizSim=pd.DataFrame(self.matriz_similitud.similarity_matrix_for_items(self._tabla))
        self.asinaturas_cuarto=Nombres_Asignaturas().get_asignaturas_cuarto()

 
   
    def predicc_usu_asign(self,listDatos, n):
        """
        Método que devuelve la predicción de un usuario a una asignatura.
        """  
        divis=0.0
        div=0.0
        for i in listDatos[0: n]:
            if i[1]>0:
                div+=abs(i[1])
                divis+=(i[1]*i[0])
        return divis/div if div!=0 else 0
    
    def mezl_dat(self, usu, asignatura):
        """
        Método que obtiene las votaciones no nulas de los usuarios y devuelve el nombre de la asignatura y la predicción. 
        """
        vot_usu= pd.isnull(self._tabla.ix[usu])
        vot_usu[asignatura]=True
        for i,k,j in zip(self.matrizSim[asignatura],self._tabla.ix[usu],vot_usu):
            if j== False:
                yield (k, i)
                
    def calculaPrediccion(self,asign,usuario,num):
        """
        Método que calcula la predicción para un usuario y los ordena. 
        """
        listDatos=list(self.mezl_dat(usuario, asign))
        listDatos.sort(key=lambda x:x[1],reverse=True)
        #return round(predicc_usu_asign(listDatos,n),0)
        return self.predicc_usu_asign(listDatos,num)
    
    def calcula_Prediccion_Cuarto(self,usuario,num=100):
        """
        Método que calcula la predicción de las asignaturas de cuarto. 
        """
        for i in self.asinaturas_cuarto:
            yield (i,self.calculaPrediccion(i,usuario,num))
            
