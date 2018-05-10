class asignatura():
#     def __init__(self):
#         self.nombre =""
#         self.isNullable = False
#         self.curso= 0
#         self.caracteristica= "";
#         
#         
    @property
    def getId(self):
        return self.id

    @id.setter()
    def setId(self, id):
        self.id = id    
        
    @property
    def getNombre(self):
        return self.nombre

    @nombre.setter()
    def setNombre(self, nombre):
        self.nombre = nombre

    @property
    def getIsNullable(self):
        return self.isNullable

    @isNullable.setter()
    def setIsNullable(self, isNullable):
        self.isNullable = isNullable
        
    @property
    def getCurso(self):
        return self.curso

    @curso.setter
    def setCurso(self, curso):
        self.curso = curso
        
    @property
    def getCaracteristica(self):
        return self.caracteristica

    @caracteristica.setter
    def setCaracteristica(self, caracteristica):
        self.caracteristica = caracteristica
        

    