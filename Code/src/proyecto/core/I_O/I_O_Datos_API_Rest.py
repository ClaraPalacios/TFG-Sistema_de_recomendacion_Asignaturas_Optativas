# -*- coding: latin1 -*-
import requests
import pandas as pd
import numpy as np

class I_O_Datos_API_Rest:
    def __init__(self,nombreArchivo):
        self._nombreArchivo=nombreArchivo
        fieldsName = ['ids','Algoritmia' ,'AnaTZYlisis_y_DisenTZYo_de_Sistemas','Aplicaciones_de_Bases_de_Datos' ,'Arquitecturas_Paralelas','Bases_de_Datos',                                                
    'ComputacioTZYn_Neuronal_y_Evolutiva','Control_por_Computador','Desarrollo_Avanzado_de_Sistemas_Software','DisenTZYo_e_ImplementacioTZYn_de_Sistemas_Digitales',
    'DisenTZYo_y_AdministracioTZYn_de_Sistemas_y_Redes_','DisenTZYo_y_Mantenimiento_del_Software' ,'EstadiTZYstica','Estructuras_de_Datos','CaTZYlculo',                                                        
    'Fundamentos_DeontoloTZYgicos_y_JuriTZYdicos_de_las_TIC' ,'Fundamentos_FiTZYsicos_de_la_InformaTZYtica' ,'Fundamentos_de_Computadores'                                    
    ,'Fundamentos_de_OrganizacioTZYn_y_GestioTZYn_de_Empresas' ,'GestioTZYn_de_Proyectos' ,'GestioTZYn_de_la_InformacioTZYn'                                
    ,'Hardware_de_AplicacioTZYn_EspeciTZYfica','InformaTZYtica_BaTZYsica' ,'IngenieriTZYa_del_Software','IngleTZYs_Aplicado_a_la_InformaTZYtica'                            
    ,'InteraccioTZYn_HombreXxMaTZYquina' ,'Mantenimiento_de_Equipos_InformaTZYticos' ,'MatemaTZYtica_Discreta' ,'MetodologiTZYa_de_la_ProgramacioTZYn'                                
    ,'MineriTZYa_de_Datos','MeTZYtodos_Formales','MeTZYtodos_NumeTZYricos_y_OptimizacioTZYn','Nuevas_TecnologiTZYas_y_Empresa','OrganizacioTZYn_y_GestioTZYn_de_Empresas'                            
    ,'Procesadores_del_Lenguaje','ProgramacioTZYn' ,'ProgramacioTZYn_Concurrente_y_de_Tiempo_Real','ProgramacioTZYn_de_Sistemas_Operativos'                            
    ,'Redes','Seguridad_InformaTZYtica','Sistemas_Distribuidos','Sistemas_Empotrados_y_de_Tiempo_Real','Sistemas_Inteligentes'                                    
    ,'Sistemas_Operativos','ValidacioTZYn_y_Pruebas','Arquitectura_de_Computadores','aTZYlgebra_Lineal']
        
        self.dicFieldName={}
        for i in fieldsName:
            self.dicFieldName[i]=i.replace('_',' ').replace('Xx','-').replace('nTZY','ñ').replace('aTZY','á').replace('oTZY','ó').replace('iTZY','í').replace('eTZY','é')
    
    #formato binario
    def obtener_datos(self):
        """
        Método que obtiene el dataframe del json de la base de datos. Renombra las columnas por las asignaturas ya que en la base de datos se almacenan sin tildes ni espacios. 
        """
        try:
            r = requests.get(self._nombreArchivo)
            dataframeTabla = pd.DataFrame(data=r.json()["data"])
            dataframeTabla=dataframeTabla.rename(columns=self.dicFieldName)
            return dataframeTabla
        except: 
            r = requests.get(self._nombreArchivo)
            dataframeTabla = pd.DataFrame(data=r.json()[0])
            if(r.json()[0]!=None):
                dataframeTabla=dataframeTabla.rename(columns=self.dicFieldName)
            return dataframeTabla.convert_objects(convert_numeric=True)
    
    def guardarDatos(self, tabla1):
        pass
        
    def transfor_datos(self,tabla):
        """
        método que elimina las columnas no necesarias del dataframe, y transforma la cadena "nan" por Nan de la librería numpy. 
        Devuelve el dataframe ordenado. 
        """
        
        #almacenar en un diccionario de diccionarios cuya clave sea el usuario, y como valor un conjunto de  diccionarios
        #(clave=nombre asignatura, valor=ponderacion). No introducimos el Token ni la fecha en la que se realizó el cuestionario. 
        asignaturas= list(tabla.columns)
        diccAsi={}
        diccAsi.setdefault(1,{})
        for k in asignaturas:
            if k != 'Token'and k!='Submitted At' and k!='ids':
                for i, j in zip(tabla[k], range(len(tabla)) ):
                    diccAsi.setdefault(j,{})
                    diccAsi[j][k]=i
        tabla1 = pd.DataFrame.from_dict(diccAsi)
        tabla1= tabla1.T
        #transformamos los vacíos en NaN para evitar el error de calcular el coeficiente de correlación de pearson entre un int y un string ('' equivale a un str)
        tabla1= tabla1.replace('', np.nan, regex=True).replace('nan', np.nan, regex=True)
        return tabla1.convert_objects(convert_numeric=True)
