import pandas as pd
import numpy as np

class Hall_Plot():
    def __init__(self, df, estatica, py, pmp):
        self.df=df
        self.estatica=estatica
        self.py=py
        self.pmp=pmp

    def data(self):

        self.df['acumulado_wi']=self.df['AGUA_INYECTADA'].cumsum()
        #Calculo depresión de aproximación de fondo fluyente
        self.df['pwf']= self.df['PIA']+ self.pmp*0.425
        #calculo de delta de presión
        self.df['delta_presion']=self.df['pwf']-self.py
        self.df.at[0,'delta_presion']=0
        self.df['acumulado_delta_presion']=self.df['delta_presion'].cumsum().astype('int')
        self.df['derivada']=self.df['acumulado_delta_presion'].diff()/self.df['acumulado_wi'].diff()
        self.df['derivada_']=self.df['derivada']*self.df['acumulado_wi']
        self.df.at[0,'derivada']=0
        self.df.at[0,'derivada_']=0

        Q3=self.df['derivada_'].quantile(0.75)
        Q1=self.df['derivada_'].quantile(0.25)

        IQR=Q3-Q1

        outliers=Q3+1.5*IQR


        self.df=self.df[~(self.df['derivada_']>=outliers)]
        

        return self.df

