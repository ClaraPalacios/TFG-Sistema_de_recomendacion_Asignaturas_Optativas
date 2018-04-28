import pandas as pd
import numpy as np
from ejecucion import Rec_Bas_Prod
class recomend_bas_usu:
    def __init__(self, dataframe, matrizSim, usu,  asignatura):
        self.dataframe= dataframe
        self.matrizSim= matrizSim
        self.usu= usu
        self.asignatura = asignatura
    
    def calculaPrediccion(self, dataframe,matrizSim,asign,usuario):
        # Encontrar los k usuarios que evaluaron 'asign'
        #Nacho guardamos las keys de los usuarios
        kUsuarios=dataframe[dataframe[asign]>0].index #np.where(dataframe[asign] > 0)[0]
        
        # Calcular la similitud de esos k usuarios a 'usuario'
        k_Similitu=matrizSim[usuario][kUsuarios]
    
        # Unir índices de usuarios y similitudes
        k_zip=list(zip(k_Similitu,kUsuarios))
    
        # Media valoraciones de usuario (sobre asignaturas cursadas)
        #Nacho: la función mean() no tiene en cuenta los valores NaN, no es necesario filtrar por valores >0
        user_u_average=dataframe.T[usuario].mean() #[list(np.where(dataframe.T[usuario]>0)[0])].mean()
    
        # Media de los valores absolutos de similitud de vecions próximos a usuario
        k_sim=[k_zip[i][0] for i in range(len(k_zip))]
        k_sim_average=np.abs(np.array(k_sim)).sum()
        
        # Estimación del rating a la asignatura asign
        rating_user_u_item_i=0
        for user_v in [k_zip[i][1] for i in range(len(k_zip))]:
            rating_user_u_item_i+= (dataframe.T[user_v][asign] - dataframe.T[user_v].mean())*matrizSim[usuario][user_v]
        rating_user_u_item_i=user_u_average + rating_user_u_item_i/k_sim_average
        #Devolvemos el rating estimado
        return rating_user_u_item_i
    
    
    #preguntar
    def coef_corr_pearson(self, dataframe,a,b,rows=True):
        dataframe
        if rows:
            common_ratings= dataframe.ix[[a,b]].dropna(axis=1).as_matrix()
            a_average = dataframe.ix[a].mean()
            b_average = dataframe.ix[b].mean()       
        else:
            common_ratings= dataframe[[a,b]].dropna(axis=0).as_matrix().T
            a_average=dataframe[a].mean()
            b_average=dataframe[b].mean()              
        if common_ratings.any(): 
            a_common_ratings=common_ratings[0,:]
            b_common_ratings=common_ratings[1,:]
            pcorr = np.dot(a_common_ratings-a_average,b_common_ratings-b_average) / ( 
                     np.sqrt(np.dot(a_common_ratings-a_average,a_common_ratings-a_average))*
                     np.sqrt(np.dot(b_common_ratings-b_average,b_common_ratings-b_average)))
            if np.isnan(pcorr):
                return 0
            else:
                return pcorr
        else:
            return 0
    
    #me he quedado aqui
    def dev_recom_productos(self, dataframe,  asignatura, usu):
        f= Rec_Bas_Prod(self.dataframe);
        matrizSim= pd.DataFrame(f.matriz_sim(self.dataframe))
        #matrizSim1=pd.DataFrame(f.matriz_sim(self.dataframe))
                                
        prediccion= self.calculaPrediccion(dataframe,matrizSim,"Computación Neuronal y Evolutiva",2)
        