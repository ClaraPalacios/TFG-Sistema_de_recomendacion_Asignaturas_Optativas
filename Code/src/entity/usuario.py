class usuario():
#     def __init__(self):
#         self.id= 0
#         self.nombre =""
#         self.email = ""
#         self.password = ""
#         self.rol = ""
# 
#         

       
    @property
    def getId(self):
        return self.id

    @id.setter()
    def setId(self, id):
        self.id = id

    @property
    def getIsNullable(self):
        return self.nombre

    @nombre.setter()
    def setNombre(self, nombre):
        self.nombre = nombre
        
    @property
    def getEmail(self):
        return self.email

    @email.setter
    def setEmail(self, email):
        self.email = email
        
    @property
    def getPassword(self):
        return self.password

    @password.setter
    def setPassword(self, password):
        self.password = password
    