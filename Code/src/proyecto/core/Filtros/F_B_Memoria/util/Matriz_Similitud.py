# -*- coding: latin1 -*-
class Matriz_Similitud:
    def __init__(self,similarity):
        self._similarity=similarity
    def similarity_matrix_for_items(self,tabla, rows= False):
        """
        Método que calcula la matriz de similitud tanto para el filtro colaborativo basado en usuarios como del filtro colaborativo basado en productos. 
        """
        matrizSim={}

        if rows==True:
            lista=tabla.index.tolist()
        else:
            lista=tabla.columns.tolist()

        for x in lista:
            otras= lista[lista.index(x): len(lista)]
            matrizSim[x]= dict([(x2, self._similarity(tabla, x, x2, rows)) for x2 in otras])
        for x in lista:
            otras= lista[lista.index(x): len(lista)]
            for x2 in otras:
                matrizSim[x2][x]= matrizSim[x][x2]
        return matrizSim
