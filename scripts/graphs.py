import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class Graficos:

    def __init__ (self, df):
        """"
        Inicializa la clase con un DataFrame

        Parámetros
        df(pd.DataFrame): Dataframe con las columnas POZO, FECHA, AGUA_INYECTDA Y PIA

        """

        self.df=df

    def grafico_1 (self):
        """Genera el grafico Agua Inyectada - Presión de Inyección vs Tiempo
        """   
        self.df = self.df.sort_values(by="FECHA")

         #Creamos el segundo eje
        fig=make_subplots(specs=[[{"secondary_y":True}]])

        #Grafica de agua inyectada
        fig.add_trace(
            go.Scattergl(
                x=self.df["FECHA"],
                y=self.df['AGUA_INYECTADA'],
                name="Agua Inyectada",
                mode="lines",
                line=dict(color='blue', width=2),
                customdata= self.df[["FECHA_FORMAT", "AGUA_INYECTADA"]],
                hovertemplate="Fecha :%{customdata[0]}<br> Agua Iny. %{customdata[1]:, .0f} BWIPD"
            ),
            secondary_y=False
            )
        
        #Grafica de Presión en eje secundario
        fig.add_trace(
            go.Scattergl(
                x=self.df['FECHA'],
                y=self.df['PIA'],
                name="Presión de Inyección",
                mode='lines',
                line=dict(color="red", width=2, dash='dot'),
                customdata=self.df[['FECHA_FORMAT','PIA']],
                hovertemplate="Fecha :%{customdata[0]}<br> Presión: %{customdata[1]:,0f} psi"
            ),
            secondary_y=True
        )

        #Configura el eje x 
        fig.update_xaxes(title_text="Fecha", tickformat="%b-%Y" , dtick='M3', tickangle=90)


        # Configurar ejes y
        fig.update_yaxes(title_text="Agua inyectada BWIPD", secondary_y=False)
        fig.update_yaxes(title_text="PResión de Inyección psi", secondary_y=True)

        fig.update_layout(title_text= f"Agua Inyectada-Presión de Inyección vs Tiempo",
                          width=1200,height=800)
        
        

        return fig
    
    def grafico_2(self):
        """genera grafico HallPlot con derivada
        """        
        self.df = self.df.sort_values(by="FECHA")
        self.df = self.df.sort_values(by='acumulado_wi')
        self.df=self.df.dropna()
        inyector=self.df['POZO'].unique()[0]


        fig=go.Figure()


        #GRafico Hall_plot
        fig.add_trace(
            go.Scatter(
                x=self.df['acumulado_wi'],
                y=self.df['acumulado_delta_presion'],
                mode='lines',
                name='hall',
                line=dict(width=2,color='blue'),
                customdata= self.df[["FECHA_FORMAT", 'acumulado_wi','acumulado_delta_presion']],
                hovertemplate="Fecha :%{customdata[0]}<br> aum_wi:% {customdata[1]:,0f}, acu_delta_p: %{customdata[2]:,0f}" 
            )
        )

        #Linea de Derivada
        fig.add_trace(
            go.Scatter(
                x=self.df['acumulado_wi'],
                y=self.df['derivada_'],
                mode='markers',
                name='Dhi',
                line=dict(width=1, color='orange'),
                customdata= self.df[["FECHA_FORMAT", 'acumulado_wi','derivada_']],
                hovertemplate="Fecha :%{customdata[0]}<br>  aum_wi:% {customdata[1]:,0f} , derivada: %{customdata[1]:,0f} psi"    
            )
        )

        fig.update_layout(
            title=f"{inyector}",
            xaxis_title="wi",
            yaxis_title="Dhi",
            width=800,
            height=800,
            plot_bgcolor='white'

        )

        fig.update_xaxes(range=[0,max(self.df['acumulado_wi'])], showgrid=True, gridcolor='lightgrey')
        fig.update_yaxes(range=[0,max(self.df['derivada_'])], showgrid=True, gridcolor='lightgrey')
        
        return fig


            
