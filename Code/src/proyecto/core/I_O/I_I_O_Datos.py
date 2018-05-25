class I_I_O_Datos(object):
    def __init__(self,nombreArchivo):
        self._nombreArchivo=nombreArchivo
    def obtener_datos( self ):
        raise NotImplementedError( "Should have implemented this" )
    def transfor_datos( self,tabla ):
        raise NotImplementedError( "Should have implemented this" )