# -*- coding: latin1 -*-
from scipy.optimize import minimize
import numpy as np
from proyecto.dicc.Nombres_Asignaturas import Nombres_Asignaturas

class Filtro_Modelos:
    def __init__(self,tabla):
        self.tabla=tabla
        self.recomendaciones_cuarto=[]
        self.filtro_cola()
    def filtro_cola(self):
        """
        M�todo que obtiene las tablas Y y R para el c�lculo del filtro colaborativo basado en Modelos
        """
        tabla2=self.tabla.T
        Y,R=self.matrices_Y_R(tabla2)
        def cofi_cost_funct(parameters, Y, R, n_users,n_items, n_features, lamb):
            """
            M�todo que calcula la funci�n del coste para obtener el coste y el gradiente. 
            """
            # Si pasamos R como argumento, esto sobra 
            #R = np.zeros_like(Y)
            #R[Y != 0] = 1

            Theta= np.reshape(parameters[0: n_users* n_features], (n_users, n_features))
            X= np.reshape(parameters[n_users*n_features:] , (n_items,n_features))

            # Para reducir el n�mero de multiplicaciones matriciales
            error=(X.dot(Theta.T)- Y )*R

            J= (1/2)*sum(sum(np.power(error,2)))
            cost= J + ((lamb/2) * sum(sum(np.power(X,2))))+((lamb/2) * sum(sum(np.power(Theta, 2))))
            X_gradient = error.dot(Theta) + X*lamb               
            Theta_gradient = error.T.dot(X) + Theta*lamb
            # Hay que pasar los gradientes (que son matrices) a vectores
            Theta_gradient_vector=np.reshape(Theta_gradient,n_users*n_features)
            X_gradient_vector=np.reshape(X_gradient,n_items*n_features)    

            gradient=np.concatenate((Theta_gradient_vector,X_gradient_vector))
            return (cost, gradient)
        n_users=Y.shape[1]
        n_items=Y.shape[0]
        n_features = 100

        X=np.random.random((n_items,n_features))
        Theta=np.random.random((n_users,n_features))

        initial_parameters = np.append(Theta.flatten(),X.flatten())
        # Set the regularization parameter
        lamb = 10

        # Define a function to be minimized
        def cofiCostFunc_minimize(parameters):
            """
            M�todo que minimiza la funci�n coste para el c�lculo del sistema de recomendaci�n basado en modelo. 
            """
            return cofi_cost_funct(parameters,Y, R, n_users, n_items, n_features,lamb)

        # Set the number of iteations
        max_iter=200
        # Minimize the function using minimize from the package scipy.optimize and get the optimized parameters
        parameters = (minimize(cofiCostFunc_minimize,initial_parameters,method="CG",jac=True,
                           options={'maxiter':max_iter, "disp":True})).x
        # Unfold the returned optimized parameters back into X and Theta
        # Your code ..............
        Theta=parameters[0:n_users*n_features].reshape(n_users,n_features)
        X=parameters[n_users*n_features:].reshape(n_items,n_features)
        predictions = np.dot(X,Theta.T)
        self.predict_cuarto(Y,predictions,tabla2)
    def matrices_Y_R(self,tabla2):
        """
        M�todo que crea las matrices Y y R para el c�lculo de la funci�n coste
        """
        # Crear matriz de ratings Y
        Y=tabla2.values
        # Convertir espacios en ceros
        Y[Y=='']=0 # eliminar los espacios
        # Crear matriz R
        R=np.zeros_like(Y)
        R[Y>0]=1
        return Y,R
    
    def predict_cuarto(self,Y,predictions,tabla2):
        """
        M�todo que calcula la predicci�n de las asignaturas del cuarto curso
        """
        u=Y.shape[1]-1
        p=predictions[:,u]
        recommendations=[]
        nombres_Asignaturas=Nombres_Asignaturas()
        asignaturas=nombres_Asignaturas.get_asignaturas_cuarto()
        for i in asignaturas:
            maxp= np.max(p)
            [rm]=np.where(p==maxp)
            recommendations.append(i)
            p[rm[0]]=0
            self.recomendaciones_cuarto.append((i, round(maxp,0)))