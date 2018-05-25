import pandas as pd
import numpy as np
from proyecto.core.Filtros.F_B_Memoria.IFiltro_Memoria import IFiltro_Memoria
from proyecto.core.Filtros.F_B_Memoria.util.Matriz_Similitud import Matriz_Similitud
from proyecto.dicc.Nombres_Asignaturas import Nombres_Asignaturas
class Filtro_Basado_Usuarios(IFiltro_Memoria):
    def __init__(self,tabla,similitud):
        self._tabla=tabla
        self.similitud=similitud
        self.matriz_similitud=Matriz_Similitud(self.similitud)
        self.matrizSim=pd.DataFrame(self.matriz_similitud.similarity_matrix_for_items(self._tabla.T))
        self.asinaturas_cuarto=Nombres_Asignaturas().get_asignaturas_cuarto()
        
    def calculaPrediccion(self,asign,usuario):
        # Encontrar los k usuarios que evaluaron 'asign'
        #Nacho guardamos las keys de los usuarios
        kUsuarios=self._tabla[self._tabla[asign]>0].index #np.where(dataframe[asign] > 0)[0]

        # Calcular la similitud de esos k usuarios a 'usuario'
        k_Similitu=self.matrizSim[usuario][kUsuarios]

        # Unir índices de usuarios y similitudes
        k_zip=list(zip(k_Similitu,kUsuarios))

        # Media valoraciones de usuario (sobre asignaturas cursadas)
        #Nacho: la función mean() no tiene en cuenta los valores NaN, no es necesario filtrar por valores >0
        user_u_average=self._tabla.T[usuario].mean() #[list(np.where(dataframe.T[usuario]>0)[0])].mean()

        # Media de los valores absolutos de similitud de vecions próximos a usuario
        k_sim=[k_zip[i][0] for i in range(len(k_zip))]
        k_sim_average=np.abs(np.array(k_sim)).sum()

        # Estimación del rating a la asignatura asign
        rating_user_u_item_i=0
        for user_v in [k_zip[i][1] for i in range(len(k_zip))]:
            rating_user_u_item_i+= (self._tabla.T[user_v][asign] - self._tabla.T[user_v].mean())*self.matrizSim[usuario][user_v]
        rating_user_u_item_i=user_u_average + rating_user_u_item_i/k_sim_average
        #Devolvemos el rating estimado
        return rating_user_u_item_i
    def calcula_Prediccion_Cuarto(self,usuario):
        for i in self.asinaturas_cuarto:
            yield (i,self.calculaPrediccion(i,usuario))
            