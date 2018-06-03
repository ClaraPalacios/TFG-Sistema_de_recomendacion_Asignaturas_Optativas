# -*- coding: latin1 -*-
from PyQt5 import QtWidgets
from proyecto.gui.Autenticacion.VentanaAutenticacion import VentanaAutenticacion
import sys
import os

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = VentanaAutenticacion(os.getcwd())
    main.show()
    sys.exit(app.exec_())

