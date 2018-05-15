
from PyQt5 import QtWidgets
from proyecto.ejecucion.RW_Datos_Drive import RW_Datos_Drive
from proyecto.ejecucion.RW_Datos_Fichero import RW_Datos_Fichero
from proyecto.ejecucion.Rec_Bas_Prod import Rec_Bas_Prod
from proyecto.gui.VentanaInicio import VentanaInicio

import sys
import os
import pandas as pd
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    print(os.getcwd())
    main = VentanaInicio(os.getcwd())
    main.show()
    sys.exit(app.exec_())

    
#     a = RW_Datos_Drive();
#     tabla1= a.transformarDatos();
#     f= Rec_Bas_Prod(tabla1);
#     matrizSim= pd.DataFrame(f.matriz_sim(tabla1))
#     g = RW_Datos_Fichero(tabla1)
#     g.guardarDatos()
#     print('esta')