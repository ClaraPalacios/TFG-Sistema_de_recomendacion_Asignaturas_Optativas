import pickle

class RW_Datos_Fichero:
    
    def __init__(self, tabla1):
        self.tabla1 = tabla1

    def guardarDatos(self):
        archivo = open("datos.bin", "wb")
        pickle.dump(self.tabla1, archivo)
        archivo.close()
        return archivo
    
    def recuperarDatos(self):
        archivo = open(self.nombreArchivo, "rb")
        tablaDatos = pickle.load(archivo)
        archivo.close()
        return tablaDatos