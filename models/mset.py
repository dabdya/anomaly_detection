import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from utils.pipeline import Predictor


def kernel(x,y):

    '''
    s(x,y) = 1 - ||x-y||/(||x|| + ||y||)
    '''

    if all(x==y):
        # Handling the case of x and y both being the zero vector.
        return 1.
    else:
        return 1. - np.linalg.norm(x-y)/(np.linalg.norm(x) + np.linalg.norm(y))

def otimes(X, Y):

    m1,n = np.shape(X)
    m2,p = np.shape(Y)

    if m1!=m2:
        raise Exception('dimensionality mismatch between X and Y.')

    Z = np.zeros( (n,p) )

    if n != p:
        for i in range(n):
            for j in range(p):
                Z[i,j] = kernel(X[:,i], Y[:,j])
    else:
        for i in range(n):     
            for j in range(i, p):
                Z[i,j] = kernel(X[:,i], Y[:,j])
                Z[j,i] = Z[i,j]

    return Z


class MSET:
    
    def __init__(self, memory_frac=0.9):
        self.D = self.L = pd.DataFrame()
        
        self.SS = StandardScaler()
        self.W = None
        
        self.memory_frac = memory_frac
    
    def fit(self, health_df):
        
        # First, include max_value from each sensor
        max_values = health_df.loc[health_df.idxmax(axis=0)]
        self.D = pd.concat([self.D, max_values])
        
        # Second, compute norm for each timestamp
        df_copy = health_df.copy()
        df_copy["Norm"] = np.linalg.norm(df_copy, axis=1)
        
        # Sort dataset by norm and pick sample of memory_frac size
        df_copy.sort_values("Norm", inplace=True)
        df_copy.drop(self.D.index, inplace=True)

        sample = df_copy.sample(frac=self.memory_frac, random_state=1)
        self.D = pd.concat([self.D, sample])
        
        # Residuals in dataset determine L matrix
        self.L = df_copy.drop(sample.index)
        
        # Delete norm and sort by timestamp
        self.D.drop(["Norm"], inplace=True, axis=1)
        self.D.sort_index(inplace=True)
        
        self.L.drop(["Norm"], inplace=True, axis=1)
        self.L.sort_index(inplace=True)
        
        # Standardization
        self.D = self.SS.fit_transform(self.D).T
        self.L = self.SS.transform(self.L).T
        
        return self
    
    def predict(self, df):
        X_obs = self.SS.transform(np.array(df)).T
        
        DD = otimes(np.array(self.D), np.array(self.D))
        DX_obs = otimes(np.array(self.D), np.array(X_obs))
        self.W = np.linalg.inv(DD) @ DX_obs

        X_est = np.array(self.D) @ self.W
        X_est = self.SS.inverse_transform(X_est.T).T
        
        return X_est

