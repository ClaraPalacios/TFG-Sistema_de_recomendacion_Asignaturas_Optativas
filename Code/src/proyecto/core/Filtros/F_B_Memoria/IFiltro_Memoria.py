from proyecto.core.Filtros.IFiltro import IFiltro
class IFiltro_Memoria(IFiltro):
    def __init__( self ):
        raise NotImplementedError( "Should have implemented this" )
    def calculaPrediccion( self ):
        raise NotImplementedError( "Should have implemented this" )
    def calcula_Prediccion_Cuarto( self ):
        raise NotImplementedError( "Should have implemented this" )