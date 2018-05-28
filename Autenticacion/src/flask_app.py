
#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Crypto.Cipher import AES
import base64 
from flasgger import Swagger
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy import and_
import traceback

secret_key = "supersegurisimo"
secret_key = secret_key.rjust(32)
cipher = AES.new(secret_key, AES.MODE_ECB) 
 
# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="claraTFG2",
#     password="123456clara",
#     hostname="claraTFG2.mysql.pythonanywhere-services.com",
#     databasename="claraTFG2$prueba",
# )
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config['SWAGGER'] = {
    # set to True so instead of
    # $ref: '#/definitions/alert'
    # we get
    # $ref: '#/definitions/index_post_alert'
    'prefix_ids': True
}
swag = Swagger(app)

class Valoraciones(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    Algoritmia=db.Column(db.String(120), unique=False)
    AnaTZYlisis_y_DisenTZYo_de_Sistemas=db.Column(db.String(120), unique=False)
    Aplicaciones_de_Bases_de_Datos=db.Column(db.String(120), unique=False)
    Arquitecturas_Paralelas=db.Column(db.String(120), unique=False)
    Bases_de_Datos=db.Column(db.String(120), unique=False)
    ComputacioTZYn_Neuronal_y_Evolutiva=db.Column(db.String(120), unique=False)
    Control_por_Computador=db.Column(db.String(120), unique=False)
    Desarrollo_Avanzado_de_Sistemas_Software=db.Column(db.String(120), unique=False)
    DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales=db.Column(db.String(120), unique=False)
    DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_=db.Column(db.String(120), unique=False)
    DisenTZYo_y_Mantenimiento_del_Software=db.Column(db.String(120), unique=False)
    EstadiTZYstica=db.Column(db.String(120), unique=False)
    Estructuras_de_Datos=db.Column(db.String(120), unique=False)
    CaTZYlculo=db.Column(db.String(120), unique=False)    
    Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC=db.Column(db.String(120), unique=False)
    Fundamentos_FiTZYsicos_de_la_InformaTZYtica=db.Column(db.String(120), unique=False)
    Fundamentos_de_Computadores=db.Column(db.String(120), unique=False)
    Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas=db.Column(db.String(120), unique=False)
    GestioTZYn_de_Proyectos=db.Column(db.String(120), unique=False)
    GestioTZYn_de_la_InformacioTZYn=db.Column(db.String(120), unique=False)
    Hardware_de_AplicacioTZYn_EspeciTZYfica=db.Column(db.String(120), unique=False)
    InformaTZYtica_BaTZYsica=db.Column(db.String(120), unique=False)
    IngenieriTZYa_del_Software=db.Column(db.String(120), unique=False)
    IngleTZYs_Aplicado_a_la_InformaTZYtica=db.Column(db.String(120), unique=False)
    InteraccioTZYn_HombreXxMaTZYquina=db.Column(db.String(120), unique=False)
    Mantenimiento_de_Equipos_InformaTZYticos=db.Column(db.String(120), unique=False)
    MatemaTZYtica_Discreta=db.Column(db.String(120), unique=False)
    MetodologiTZYa_de_la_ProgramacioTZYn=db.Column(db.String(120), unique=False)
    MineriTZYa_de_Datos=db.Column(db.String(120), unique=False)
    MeTZYtodos_Formales=db.Column(db.String(120), unique=False)
    MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn=db.Column(db.String(120), unique=False)
    Nuevas_TecnologiTZYas_y_Empresa=db.Column(db.String(120), unique=False)
    OrganizacioTZYn_y_GestioTZYn_de_Empresas=db.Column(db.String(120), unique=False)
    Procesadores_del_Lenguaje=db.Column(db.String(120), unique=False)
    ProgramacioTZYn=db.Column(db.String(120), unique=False)
    ProgramacioTZYn_Concurrente_y_de_Tiempo_Real=db.Column(db.String(120), unique=False)
    ProgramacioTZYn_de_Sistemas_Operativos=db.Column(db.String(120), unique=False)
    Redes=db.Column(db.String(120), unique=False)
    Seguridad_InformaTZYtica=db.Column(db.String(120), unique=False)
    Sistemas_Distribuidos=db.Column(db.String(120), unique=False)
    Sistemas_Empotrados_y_de_Tiempo_Real=db.Column(db.String(120), unique=False)
    Sistemas_Inteligentes=db.Column(db.String(120), unique=False)
    Sistemas_Operativos=db.Column(db.String(120), unique=False)
    ValidacioTZYn_y_Pruebas=db.Column(db.String(120), unique=False)
    aTZYlgebra_Lineal=db.Column(db.String(120), unique=False)
    Arquitectura_de_Computadores=db.Column(db.String(120), unique=False)

 
    def __init__(self,aTZYlgebra_Lineal , Arquitectura_de_Computadores="",Algoritmia="",AnaTZYlisis_y_DisenTZYo_de_Sistemas="",Aplicaciones_de_Bases_de_Datos="",Arquitecturas_Paralelas="",
                Bases_de_Datos="",ComputacioTZYn_Neuronal_y_Evolutiva="",Control_por_Computador="",Desarrollo_Avanzado_de_Sistemas_Software=""  ,
                DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales="" ,DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_="" ,
                DisenTZYo_y_Mantenimiento_del_Software="" ,EstadiTZYstica="",Estructuras_de_Datos="",CaTZYlculo="" ,
                Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC="",Fundamentos_FiTZYsicos_de_la_InformaTZYtica="",
                Fundamentos_de_Computadores="",Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas="",GestioTZYn_de_Proyectos="",
                GestioTZYn_de_la_InformacioTZYn="",Hardware_de_AplicacioTZYn_EspeciTZYfica="",InformaTZYtica_BaTZYsica="",IngenieriTZYa_del_Software="",
                IngleTZYs_Aplicado_a_la_InformaTZYtica="",InteraccioTZYn_HombreXxMaTZYquina="",Mantenimiento_de_Equipos_InformaTZYticos="",
                MatemaTZYtica_Discreta="",MetodologiTZYa_de_la_ProgramacioTZYn="",MineriTZYa_de_Datos="" ,MeTZYtodos_Formales="", 
                MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn="",Nuevas_TecnologiTZYas_y_Empresa="",OrganizacioTZYn_y_GestioTZYn_de_Empresas="",
                Procesadores_del_Lenguaje="",ProgramacioTZYn="",ProgramacioTZYn_Concurrente_y_de_Tiempo_Real="",
                ProgramacioTZYn_de_Sistemas_Operativos="" ,Redes ="",Seguridad_InformaTZYtica="",Sistemas_Distribuidos="",
                Sistemas_Empotrados_y_de_Tiempo_Real="",Sistemas_Inteligentes="",Sistemas_Operativos="" ,ValidacioTZYn_y_Pruebas="",ids=None):
        
        self.aTZYlgebra_Lineal=aTZYlgebra_Lineal
        self.Arquitectura_de_Computadores=Arquitectura_de_Computadores
        self.Algoritmia=Algoritmia
        self.AnaTZYlisis_y_DisenTZYo_de_Sistemas=AnaTZYlisis_y_DisenTZYo_de_Sistemas
        self.Aplicaciones_de_Bases_de_Datos=Aplicaciones_de_Bases_de_Datos
        self.Arquitecturas_Paralelas=Arquitecturas_Paralelas
        self.Bases_de_Datos=Bases_de_Datos
        self.ComputacioTZYn_Neuronal_y_Evolutiva=ComputacioTZYn_Neuronal_y_Evolutiva
        self.Control_por_Computador=Control_por_Computador
        self.Desarrollo_Avanzado_de_Sistemas_Software=Desarrollo_Avanzado_de_Sistemas_Software
        self.DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales=DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales
        self.DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_=DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_
        self.DisenTZYo_y_Mantenimiento_del_Software=DisenTZYo_y_Mantenimiento_del_Software
        self.EstadiTZYstica=EstadiTZYstica
        self.Estructuras_de_Datos=Estructuras_de_Datos
        self.CaTZYlculo=CaTZYlculo
        self.Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC=Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC
        self.Fundamentos_FiTZYsicos_de_la_InformaTZYtica=Fundamentos_FiTZYsicos_de_la_InformaTZYtica
        self.Fundamentos_de_Computadores=Fundamentos_de_Computadores
        self.Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas=Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas
        self.GestioTZYn_de_Proyectos=GestioTZYn_de_Proyectos
        self.GestioTZYn_de_la_InformacioTZYn=GestioTZYn_de_la_InformacioTZYn
        self.Hardware_de_AplicacioTZYn_EspeciTZYfica=Hardware_de_AplicacioTZYn_EspeciTZYfica
        self.InformaTZYtica_BaTZYsica=InformaTZYtica_BaTZYsica
        self.IngenieriTZYa_del_Software=IngenieriTZYa_del_Software
        self.IngleTZYs_Aplicado_a_la_InformaTZYtica=IngleTZYs_Aplicado_a_la_InformaTZYtica
        self.InteraccioTZYn_HombreXxMaTZYquina=InteraccioTZYn_HombreXxMaTZYquina
        self.Mantenimiento_de_Equipos_InformaTZYticos=Mantenimiento_de_Equipos_InformaTZYticos
        self.MatemaTZYtica_Discreta=MatemaTZYtica_Discreta
        self.MetodologiTZYa_de_la_ProgramacioTZYn=MetodologiTZYa_de_la_ProgramacioTZYn
        self.MineriTZYa_de_Datos=MineriTZYa_de_Datos
        self.MeTZYtodos_Formales=MeTZYtodos_Formales
        self.MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn=MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn
        self.Nuevas_TecnologiTZYas_y_Empresa=Nuevas_TecnologiTZYas_y_Empresa
        self.OrganizacioTZYn_y_GestioTZYn_de_Empresas=OrganizacioTZYn_y_GestioTZYn_de_Empresas
        self.Procesadores_del_Lenguaje=Procesadores_del_Lenguaje
        self.ProgramacioTZYn=ProgramacioTZYn
        self.ProgramacioTZYn_Concurrente_y_de_Tiempo_Real=ProgramacioTZYn_Concurrente_y_de_Tiempo_Real
        self.ProgramacioTZYn_de_Sistemas_Operativos=ProgramacioTZYn_de_Sistemas_Operativos
        self.Redes=Redes
        self.Seguridad_InformaTZYtica=Seguridad_InformaTZYtica
        self.Sistemas_Distribuidos=Sistemas_Distribuidos
        self.Sistemas_Empotrados_y_de_Tiempo_Real=Sistemas_Empotrados_y_de_Tiempo_Real
        self.Sistemas_Inteligentes=Sistemas_Inteligentes
        self.Sistemas_Operativos=Sistemas_Operativos
        self.ValidacioTZYn_y_Pruebas=ValidacioTZYn_y_Pruebas

class User(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=False)
    rol = db.Column(db.String(120), unique=False)
 
    def __init__(self, username, email, password, rol, ids=None):
        self.username = username
        self.email = email
        self.password = password
        self.rol = rol
        self.ids = ids
 
    def jsonUser(self):
        return self.username + self.email + self.password + self.rol
 
 
class UserSchema(ma.Schema):

    class Meta:
        # Fields to expose
        fields = ('ids', 'username', 'email', 'password', 'rol')
 
class ValoracionesSchema(ma.Schema):

    class Meta:
        # Fields to expose
        fields = ('ids','aTZYlgebra_Lineal','Arquitectura_de_Computadores','Algoritmia' ,'AnaTZYlisis_y_DisenTZYo_de_Sistemas','Aplicaciones_de_Bases_de_Datos' ,'Arquitecturas_Paralelas','Bases_de_Datos',                                                
    'ComputacioTZYn_Neuronal_y_Evolutiva','Control_por_Computador','Desarrollo_Avanzado_de_Sistemas_Software','DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales',
    'DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_','DisenTZYo_y_Mantenimiento_del_Software' ,'EstadiTZYstica','Estructuras_de_Datos','CaTZYlculo',                                                        
    'Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC'            
    ,'Fundamentos_FiTZYsicos_de_la_InformaTZYtica'                        
    ,'Fundamentos_de_Computadores'                                    
    ,'Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas'            
    ,'GestioTZYn_de_Proyectos'                                        
    ,'GestioTZYn_de_la_InformacioTZYn'                                
    ,'Hardware_de_AplicacioTZYn_EspeciTZYfica'                            
    ,'InformaTZYtica_BaTZYsica'                                            
    ,'IngenieriTZYa_del_Software'                                        
    ,'IngleTZYs_Aplicado_a_la_InformaTZYtica'                            
    ,'InteraccioTZYn_HombreXxMaTZYquina'                                    
    ,'Mantenimiento_de_Equipos_InformaTZYticos'                        
    ,'MatemaTZYtica_Discreta'                                            
    ,'MetodologiTZYa_de_la_ProgramacioTZYn'                                
    ,'MineriTZYa_de_Datos'                                            
    ,'MeTZYtodos_Formales'                                            
    ,'MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn'                            
    ,'Nuevas_TecnologiTZYas_y_Empresa'                                
    ,'OrganizacioTZYn_y_GestioTZYn_de_Empresas'                            
    ,'Procesadores_del_Lenguaje'                                
    ,'ProgramacioTZYn'                                                
    ,'ProgramacioTZYn_Concurrente_y_de_Tiempo_Real'                    
    ,'ProgramacioTZYn_de_Sistemas_Operativos'                            
    ,'Redes'                                                    
    ,'Seguridad_InformaTZYtica'                                    
    ,'Sistemas_Distribuidos'                                        
    ,'Sistemas_Empotrados_y_de_Tiempo_Real'                        
    ,'Sistemas_Inteligentes'                                    
    ,'Sistemas_Operativos'                                            
    ,'ValidacioTZYn_y_Pruebas')
 
user_schema = UserSchema()
users_schema = UserSchema(many=True)

valoraciones_schema = ValoracionesSchema()
valoraciones_schema = ValoracionesSchema(many=True)
#endpoint to add a user
@app.route("/User_Add", methods=["POST"])
def add_user():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: alert
          properties:
            
            username:
              type: string
            email:
              type: string
            password:
              type: string
            rol:
              type: string
            
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_post_alert'
    """
    try:
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        rol = request.json['rol']
        # cifrado de contrasenTZYa
        password = password.rjust(32)
        password = base64.b64encode(cipher.encrypt(password.encode("iso-8859-15"))).decode('iso-8859-15').strip()
    
        new_user = User(username, email, password, rol)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
 
  
#endpoint for validate credentials    
@app.route("/User_Validate_Credentials", methods=["POST"])
def validate_credentials():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: alert
          properties:
            email:
              type: string
            password:
              type: string
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_post_alert'
    """
    try:
        email_requ = request.json['email']
        password_requ = request.json['password']
        password_requ = password_requ.rjust(32)
        password_requ_encr = base64.b64encode(cipher.encrypt(password_requ.encode("iso-8859-15")))    
        password_requ_encr = password_requ_encr.decode('iso-8859-15').strip()
    
        print("email_requ", email_requ)
        print("password_requ", password_requ)
        print("password_requ_encrip", password_requ_encr)
    
    # desencriptar password
    
        user = User.query.filter(and_(
            password_requ_encr==User.password
            ,         
            User.email == email_requ)).first()
            
        
        return jsonify(True) if user!= None  else  jsonify(False)
    except:
        return jsonify(False)
      

# endpoint to show all users
@app.route("/User_Get_All", methods=["GET"])
def get_all_users():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---    
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_get_alert'
    """
    try:
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)
    except:
        return jsonify(False)


# endpoint to update user
@app.route("/User_Update", methods=["PUT"])
def user_update():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
    parameters:

      - in: body
        name: body
        schema:
          id: alert
          properties:
            password_new:
              type: string
            password_old:
              type: string
            email_user:
              type: string
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_put_alert'
    """
    try:
        print("email_user")

        email_user = request.json['email']
        print(email_user)

        password_new = request.json['password_new']
        password_old = request.json['password_old']
        print(password_new)
        print(password_old)
        password_requ = password_old
        password_requ = password_requ.rjust(32)
        password_requ_encr = base64.b64encode(cipher.encrypt(password_requ.encode("iso-8859-15")))    
        password_requ_encr = password_requ_encr.decode('iso-8859-15').strip()
    
        #comprobar si la password vieja es valida.
        user = User.query.filter(and_(
            password_requ_encr==User.password
            ,         
            User.email == email_user)).first()
        if user!=None:
            password_new = password_new.rjust(32)
            password_new = base64.b64encode(cipher.encrypt(password_new.encode("iso-8859-15"))).decode('iso-8859-15').strip()        
            user.password = password_new     
            db.session.commit()
            return jsonify(True)
        else:
            return False
    except:
        return jsonify(False)
 

# endpoint to delete user
@app.route("/User_Dell", methods=["DELETE"])
def user_delete():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
    parameters:
    
      - in: body
        name: body
        schema:
          id: alert
          properties:
            password:
              type: string
            email:
              type: string
          
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_delete_alert'
    """
    try:
        email_actu = request.json['email']
        password_actu = request.json['password']
        print(password_actu)
        print(email_actu)
        password_actu = password_actu.rjust(32)
        password_requ_encr = base64.b64encode(cipher.encrypt(password_actu.encode("iso-8859-15")))    
        password_requ_encr = password_requ_encr.decode('iso-8859-15').strip() 
        print(password_requ_encr)

        user = User.query.filter(and_(
            password_requ_encr==User.password
            ,         
            User.email == email_actu)).first()
        print(user)
        if user!= None:
            db.session.delete(user)
            db.session.commit()
            return jsonify(True)
        else:
            return jsonify(False)  
    
    except:
        return jsonify(False)
 
# endpoint to show all valoraciones
@app.route("/Valoraciones_Get_All", methods=["GET"])
def get_all_valoraciones():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---    
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_get_alert'
    """
    try:
#         new_valora = Valoraciones("",2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
#         db.session.add(new_valora)
#         db.session.commit()
        all_users = Valoraciones.query.all()
        result = valoraciones_schema.dump(all_users)

        return jsonify(result)
    except Exception:
        return jsonify(traceback.print_exc())

# endpoint to delete all users
@app.route("/valoraciones/deleteall", methods=["DELETE"])
def Deleteall_user():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
   
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_delete_alert'
    """
    valoraciones = Valoraciones.query.all()
    number=0
    for i in valoraciones:        
        db.session.delete(i)
        db.session.commit()
        number+=1
 
    
    return jsonify(number)
 
@app.route("/Valoracion_Add", methods=["POST"])
def add_valoracion():
    """
    Test the compatibility
    This is just a test for flasgger 0.5.14 compat
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: alert
          properties:            
            username:
              type: string
           
            
    produces:
      application/json
    responses:
      200:
        description: Alert
        schema:
          $ref: '#/definitions/index_post_alert'
    """
    try:
        
        
        Arquitectura_de_Computadores=request.json["Arquitectura_de_Computadores"]
        Algoritmia=request.json["Algoritmia"]
        AnaTZYlisis_y_DisenTZYo_de_Sistemas=request.json["AnaTZYlisis_y_DisenTZYo_de_Sistemas"]
        Aplicaciones_de_Bases_de_Datos= request.json["Aplicaciones_de_Bases_de_Datos"]
        Arquitecturas_Paralelas=request.json["Arquitecturas_Paralelas"]
        Bases_de_Datos=request.json["Bases_de_Datos"]
        ComputacioTZYn_Neuronal_y_Evolutiva=request.json["ComputacioTZYn_Neuronal_y_Evolutiva"]
        Control_por_Computador=request.json["Control_por_Computador"]
        Desarrollo_Avanzado_de_Sistemas_Software=request.json["Desarrollo_Avanzado_de_Sistemas_Software"]
        DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales=request.json["DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales"]
        DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_=request.json["DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_"]
        DisenTZYo_y_Mantenimiento_del_Software=request.json["DisenTZYo_y_Mantenimiento_del_Software"]
        EstadiTZYstica=request.json["EstadiTZYstica"]
        Estructuras_de_Datos=request.json["Estructuras_de_Datos"]
        CaTZYlculo=request.json["CaTZYlculo"]
        Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC=request.json["Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC"]
        Fundamentos_FiTZYsicos_de_la_InformaTZYtica=request.json["Fundamentos_FiTZYsicos_de_la_InformaTZYtica"]
        Fundamentos_de_Computadores=request.json["Fundamentos_de_Computadores"]
        Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas=request.json["Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas"]
        GestioTZYn_de_Proyectos=request.json["GestioTZYn_de_Proyectos"]
        GestioTZYn_de_la_InformacioTZYn=request.json["GestioTZYn_de_la_InformacioTZYn"]
        Hardware_de_AplicacioTZYn_EspeciTZYfica=request.json["Hardware_de_AplicacioTZYn_EspeciTZYfica"]
        InformaTZYtica_BaTZYsica=request.json["InformaTZYtica_BaTZYsica"]
        IngenieriTZYa_del_Software=request.json["IngenieriTZYa_del_Software"]
        IngleTZYs_Aplicado_a_la_InformaTZYtica=request.json["IngleTZYs_Aplicado_a_la_InformaTZYtica"]
        InteraccioTZYn_HombreXxMaTZYquina=request.json["InteraccioTZYn_HombreXxMaTZYquina"]
        Mantenimiento_de_Equipos_InformaTZYticos=request.json["Mantenimiento_de_Equipos_InformaTZYticos"]
        MatemaTZYtica_Discreta=request.json["MatemaTZYtica_Discreta"]
        MetodologiTZYa_de_la_ProgramacioTZYn=request.json["MetodologiTZYa_de_la_ProgramacioTZYn"]
        MineriTZYa_de_Datos=request.json["MineriTZYa_de_Datos"]
        MeTZYtodos_Formales=request.json["MeTZYtodos_Formales"]
        MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn=request.json["MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn"]
        Nuevas_TecnologiTZYas_y_Empresa=request.json["Nuevas_TecnologiTZYas_y_Empresa"]
        OrganizacioTZYn_y_GestioTZYn_de_Empresas=request.json["OrganizacioTZYn_y_GestioTZYn_de_Empresas"]
        Procesadores_del_Lenguaje=request.json["Procesadores_del_Lenguaje"]
        ProgramacioTZYn=request.json["ProgramacioTZYn"]
        ProgramacioTZYn_Concurrente_y_de_Tiempo_Real=request.json["ProgramacioTZYn_Concurrente_y_de_Tiempo_Real"]
        ProgramacioTZYn_de_Sistemas_Operativos=request.json["ProgramacioTZYn_de_Sistemas_Operativos"]
        Redes=request.json["Redes"]
        Seguridad_InformaTZYtica=request.json["Seguridad_InformaTZYtica"]
        Sistemas_Distribuidos=request.json["Sistemas_Distribuidos"]
        Sistemas_Empotrados_y_de_Tiempo_Real=request.json["Sistemas_Empotrados_y_de_Tiempo_Real"]
        Sistemas_Inteligentes=request.json["Sistemas_Inteligentes"]
        Sistemas_Operativos=request.json["Sistemas_Operativos"]
        ValidacioTZYn_y_Pruebas=request.json["ValidacioTZYn_y_Pruebas"]
        aTZYlgebra_Lineal=request.json["aTZYlgebra_Lineal"]

        new_valora = Valoraciones(aTZYlgebra_Lineal,
Arquitectura_de_Computadores,
Algoritmia,
AnaTZYlisis_y_DisenTZYo_de_Sistemas,
Aplicaciones_de_Bases_de_Datos,
Arquitecturas_Paralelas,
Bases_de_Datos,
ComputacioTZYn_Neuronal_y_Evolutiva,
Control_por_Computador,
Desarrollo_Avanzado_de_Sistemas_Software,
DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales,
DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_,
DisenTZYo_y_Mantenimiento_del_Software,
EstadiTZYstica,
Estructuras_de_Datos,
CaTZYlculo,
Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC,
Fundamentos_FiTZYsicos_de_la_InformaTZYtica,
Fundamentos_de_Computadores,
Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas,
GestioTZYn_de_Proyectos,
GestioTZYn_de_la_InformacioTZYn,
Hardware_de_AplicacioTZYn_EspeciTZYfica,
InformaTZYtica_BaTZYsica,
IngenieriTZYa_del_Software,
IngleTZYs_Aplicado_a_la_InformaTZYtica,
InteraccioTZYn_HombreXxMaTZYquina,
Mantenimiento_de_Equipos_InformaTZYticos,
MatemaTZYtica_Discreta,
MetodologiTZYa_de_la_ProgramacioTZYn,
MineriTZYa_de_Datos,
MeTZYtodos_Formales,
MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn,
Nuevas_TecnologiTZYas_y_Empresa,
OrganizacioTZYn_y_GestioTZYn_de_Empresas,
Procesadores_del_Lenguaje,
ProgramacioTZYn,
ProgramacioTZYn_Concurrente_y_de_Tiempo_Real,
ProgramacioTZYn_de_Sistemas_Operativos,
Redes ,
Seguridad_InformaTZYtica,
Sistemas_Distribuidos,
Sistemas_Empotrados_y_de_Tiempo_Real,
Sistemas_Inteligentes,
Sistemas_Operativos,
ValidacioTZYn_y_Pruebas)

        db.session.add(new_valora)
        db.session.commit()
        return jsonify(True)
    except:
        db.session.rollback()
        return jsonify(False)
    
if __name__ == '__main__':
    app.run(debug=True)
