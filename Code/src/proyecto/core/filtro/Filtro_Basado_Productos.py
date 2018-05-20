import pandas as pd
from proyecto.filtro.Matriz_Similitud import Matriz_Similitud

class Filtro_Basado_Productos:
    def __init__(self,tabla,similitud):
        self._tabla=tabla
        self.similitud=similitud
        self.matriz_similitud=Matriz_Similitud(self.similitud)
        self.matrizSim=pd.DataFrame(self.matriz_similitud.similarity_matrix_for_items(self._tabla))
        self.asinaturas_cuarto=[
            #primer semestre
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
            #segundo semestre
            'Sistemas Distribuidos',
            'Sistemas Empotrados y de Tiempo Real',
            'M�todos Formales',
            'Nuevas Tecnolog�as y Empresa',
            'Miner�a de Datos',
            'Desarrollo Avanzado de Sistemas Software'
        ]
        
   
    def predicc_usu_asign(self,listDatos, n):
        divis=0.0
        div=0.0
        for i in listDatos[0: n]:
            if i[1]>0:
                div+=abs(i[1])
                divis+=(i[1]*i[0])
        return divis/div if div!=0 else 0
    
    def mezl_dat(self, usu, asignatura):
        vot_usu= pd.isnull(self._tabla.ix[usu])
        vot_usu[asignatura]=True
        for i,k,j in zip(self.matrizSim[asignatura],self._tabla.ix[usu],vot_usu):
            if j== False:
                yield (k, i)
    def calculaPrediccion(self,asign,usuario,num):
        listDatos=list(self.mezl_dat(usuario, asign))
        listDatos.sort(key=lambda x:x[1],reverse=True)
        #return round(predicc_usu_asign(listDatos,n),0)
        return self.predicc_usu_asign(listDatos,num)
    
    def calcula_Prediccion_Cuarto(self,usuario,num=100):
        for i in self.asinaturas_cuarto:
            yield (i,self.calculaPrediccion(i,usuario,num))
            
