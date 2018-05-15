class asignatura():
#     def __init__(self):
#         self.nombre =""
#         self.isNullable = False
#         self.curso= 0
#         self.caracteristica= "";
#         
#         

    @property
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    @property
    def getIsNullable(self):
        return self.isNullable

    def setIsNullable(self, isNullable):
        self.isNullable = isNullable
        
    @property
    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso
        
    @property
    def getCaracteristica(self):
        return self.caracteristica

    def setCaracteristica(self, caracteristica):
        self.caracteristica = caracteristica
        
    @property
    def getPonderacion(self):
        return self.ponderacion
    
    
    def setPonderacion(self, ponderacion):
        self.ponderacion = ponderacion