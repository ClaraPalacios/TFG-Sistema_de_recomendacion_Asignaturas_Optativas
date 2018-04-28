import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

class RW_Datos_Drive:
    
    def __init__(self):
        print('hola')

        
    
    def obtener_datos(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("DatosTFG_SistemasRecomendacion").sheet1
        tabla = pd.DataFrame(data=sheet.get_all_records())
        return tabla
    
    def transformarDatos(self):
        tabla=self.obtener_datos()
        asignaturas= list(tabla.columns)
        diccAsi={}
        diccAsi.setdefault(1,{})
        for k in asignaturas:
            if k != 'Token'and k!='Submitted At':
                for i, j in zip(tabla[k], range(len(tabla['Algoritmia'])) ):
                    diccAsi.setdefault(j,{})
                    diccAsi[j][k]=i
        tabla1 = pd.DataFrame.from_dict(diccAsi)
        tabla1= tabla1.T
        #transformamos los vacíos en NaN para evitar el error de calcular el coeficiente de correlación de pearson entre un int y un string ('' equivale a un str)
        tabla1= tabla1.replace('', np.nan, regex=True)
        return tabla1

