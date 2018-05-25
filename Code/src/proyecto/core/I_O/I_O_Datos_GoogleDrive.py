import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from proyecto.core.I_O.I_I_O_Datos import I_I_O_Datos
class I_O_Datos_GoogleDrive(I_I_O_Datos):
    def __init__(self,scope,creds_file,GDriveName):
        self._scope=scope
        self._creds_file=creds_file
        self._GDriveName=GDriveName
        
    def obtener_datos(self):
        # use creds to create a client to interact with the Google Drive API
        #scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        scope = self._scope
        #creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        creds = ServiceAccountCredentials.from_json_keyfile_name(self._creds_file, scope)
        
        client = gspread.authorize(creds)
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open(self._GDriveName).sheet1

        # Extract and print all of the values
#         list_of_hashes = sheet.get_all_records()
        #print(list_of_hashes
        tabla = pd.DataFrame(data=sheet.get_all_records())
        return tabla
    
    def transfor_datos(self,tabla):
        #almacenar en un diccionario de diccionarios cuya clave sea el usuario, y como valor un conjunto de  diccionarios
        #(clave=nombre asignatura, valor=ponderacion). No introducimos el Token ni la fecha en la que se realizó el cuestionario. 
        asignaturas= list(tabla.columns)
        diccAsi={}
        diccAsi.setdefault(1,{})
        for k in asignaturas:
            if k != 'Token'and k!='Submitted At':
                for i, j in zip(tabla[k], range(len(tabla)) ):
                    diccAsi.setdefault(j,{})
                    diccAsi[j][k]=i
        tabla1 = pd.DataFrame.from_dict(diccAsi)
        tabla1= tabla1.T
        #transformamos los vacíos en NaN para evitar el error de calcular el coeficiente de correlación de pearson entre un int y un string ('' equivale a un str)
        tabla1= tabla1.replace('', np.nan, regex=True)
        return tabla1