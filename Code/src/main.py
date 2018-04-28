from ejecucion import Rec_Bas_Prod
from ejecucion import obtencionDatos
from ejecucion import RW_Datos_Drive
from ejecucion import RW_Datos_Fichero

from ejecucion import recomend_bas_prod
import pandas as pd

if __name__ == '__main__':
    d= obtencionDatos()

    tabla1= d.transformarDatos();
    #f = Rec_Bas_Prod(tabla1)
    # matrizSim= pd.DataFrame(f.matriz_sim(tabla1))
   # nombreArchivo= "archivosGuardados.bin"
  #  print(matrizSim)
    g = RW_Datos_Fichero(tabla1)
    g.guardarDatos()

    
    
    