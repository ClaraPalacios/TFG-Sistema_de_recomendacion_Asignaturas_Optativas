import numpy as np
import pandas as pd
class Rec_Bas_Prod:
    
    def __init__(self, tabla):
        self.tabla = tabla
        

#     
    def med_pond(self, tabla, list1):
        return tabla[list1].mean()
#     
#     
    def med_pond_ix(self, tabla, list1):
        return tabla.ix[list1].mean()
     
#     
    def coef_corr_pearson(self, tabla1, usu1, usu2, rows=True):
        if rows: 
            #almacenamiento en un array de arrays las listas con las respuestas no vacías de ambos usuarios
            listUsu= tabla1.loc[[usu1,usu2]].dropna(axis=1).as_matrix()
        else:
            listUsu= tabla1[[usu1,usu2]].dropna(axis=0).as_matrix().T
        if listUsu.any():
            # Medias sobre la lista de asignaturas valoradas por ambos usuarios
            usu1_med=listUsu[0,:].mean()  
            usu2_med=listUsu[1,:].mean()
            
            correl_pearson= np.dot(listUsu[0,:] - usu1_med, listUsu[1,:]-usu2_med)/(np.sqrt(np.dot(listUsu[0,:]-usu1_med, listUsu[0, :]-usu1_med))*
            np.sqrt(np.dot(listUsu[1,:]-usu2_med, listUsu[1, :]-usu2_med)))
            if np.isnan(correl_pearson):
                return 0
            else:
                return correl_pearson
        else:
            return 0
        
    def matriz_sim(self, tabla, rows=False, correl_pearson=coef_corr_pearson ):
    # Nacho: utilizo nombres de lista generales para que pueda servir para calcular
    # las matriz de similitudes de usuarios o de asignaturas
    
        matrizSim={}
    
        if rows==True:
            lista=tabla.index.tolist()
        else:
            lista=tabla.columns.tolist()
    
        for x in lista:
            otras= lista[lista.index(x): len(lista)]
            matrizSim[x]= dict([(x2, correl_pearson(tabla, x, x2, rows)) for x2 in otras])
        for x in lista:
            otras= lista[lista.index(x): len(lista)]
            for x2 in otras:
                matrizSim[x2][x]= matrizSim[x][x2]
        return matrizSim
        
    
        
    