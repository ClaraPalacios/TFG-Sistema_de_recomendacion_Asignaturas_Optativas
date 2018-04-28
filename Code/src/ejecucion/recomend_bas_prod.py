import pandas as pd
 
class recomend_bas_prod:
    def __init__(self, tabla, usu, asignatura):
        self.tabla= tabla
        self.usu= usu
        self.asignatura = asignatura
    
    def mezl_dat(self, tabla1, matrizSim, usu, asignatura):
        vot_usu= pd.isnull(tabla1.ix[usu])
        vot_usu[asignatura]=True
        for i,k,j in zip(matrizSim[self.asignatura], self.tabla1.ix[self.usu],vot_usu):
            if j== False:
                yield (k, i)
                
    def predicc_usu_asign(self, listDatos, n):
        divis=0.0
        div=0.0
        for i in listDatos[0: n]:
            if i[1]>0:
                div+=abs(i[1])
                divis+=(i[1]*i[0])
        return divis/div if div!=0 else 0
    
    def dev_recom_productos(self, tabla1, matrizSim, asignatura, usu, n):
        listDatos=list(self.mezl_dat(tabla1,matrizSim,usu, asignatura))
        listDatos.sort(key=lambda x:x[1],reverse=True)
        return round(self.predicc_usu_asign(listDatos,n),0)