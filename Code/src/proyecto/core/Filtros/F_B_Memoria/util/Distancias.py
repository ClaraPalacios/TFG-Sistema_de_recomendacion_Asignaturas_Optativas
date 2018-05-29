import warnings
warnings.filterwarnings("ignore")

import numpy as np
class Distancias:
    def coef_corr_pearson(self,dataframe,a,b,rows=True):
        dataframe
        if rows:
            common_ratings= dataframe.ix[[a,b]].dropna(axis=1).as_matrix()
            a_average = dataframe.ix[a].mean()
            b_average = dataframe.ix[b].mean()       
        else:
            common_ratings= dataframe[[a,b]].dropna(axis=0).as_matrix().T
            a_average=dataframe[a].mean()
            b_average=dataframe[b].mean()              
        if common_ratings.any(): 
            a_common_ratings=common_ratings[0,:]
            b_common_ratings=common_ratings[1,:]
            pcorr = np.dot(a_common_ratings-a_average,b_common_ratings-b_average) / ( 
                     np.sqrt(np.dot(a_common_ratings-a_average,a_common_ratings-a_average))*
                     np.sqrt(np.dot(b_common_ratings-b_average,b_common_ratings-b_average)))
            if np.isnan(pcorr):
                return 0
            else:
                return pcorr
        else:
            return 0