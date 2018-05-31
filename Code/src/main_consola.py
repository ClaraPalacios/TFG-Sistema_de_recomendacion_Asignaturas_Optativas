#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from proyecto.core.I_O.I_O_Datos_Binario import I_O_Datos_Binario
from proyecto.core.Filtros.F_B_Memoria.util.Distancias import Distancias
from proyecto.core.Filtros.F_B_Memoria.Usuarios.Filtro_Basado_Usuarios import Filtro_Basado_Usuarios
from proyecto.core.Filtros.F_B_Memoria.Productos.Filtro_Basado_Productos import Filtro_Basado_Productos
import operator
import pprint
if __name__ == '__main__':
    IO_DATOS=I_O_Datos_Binario('archivoDatos.bin')     
    tabla=IO_DATOS.obtener_datos()
    tabla=IO_DATOS.transfor_datos(tabla)
    #pprint.pprint(tabla)
    #IO_DATOS.guardarDatos(DATOS)
    
#     distancias=Distancias()
#     filtro_Basado_Usuarios=Filtro_Basado_Usuarios(tabla,distancias.coef_corr_pearson)
#     usuario=2
#     predic=dict(filtro_Basado_Usuarios.calcula_Prediccion_Cuarto(usuario))
#     predic = sorted(predic.items(), key=operator.itemgetter(1),reverse=True)
#     pprint.pprint(predic)
#     print("------------------------------------------------------------------------------------")
#     
    print("Filtro_Basado_Productos")
    distancias=Distancias()
    Filtro_Basado_Productos=Filtro_Basado_Productos(tabla,distancias.coef_corr_pearson)
    usuario=20
    predic=dict(Filtro_Basado_Productos.calcula_Prediccion_Cuarto(usuario))
    predic = sorted(predic.items(), key=operator.itemgetter(1),reverse=True)
    pprint.pprint(predic)


