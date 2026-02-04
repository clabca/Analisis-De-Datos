import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Crear DataFrame de ejemplo
data = {
    "Nombre": ["Ana", "Luis", "Sofia", "Carlos", "Marta"],
    "Edad": [22, 29, 24, 32, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
}
df = pd.DataFrame(data)

# Función para crear gráfico de dispersión
def crear_grafico(df):
    fig = px.scatter(
        df,
        x="Nombre",
        y="Edad",
        color="Ciudad",
        title="Edad por Nombre y Ciudad",
        size="Edad",  # Opcional: tamaño de los puntos según edad
        hover_data=["Ciudad"]
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Crear figura
fig = crear_grafico(df)

# Definir layout
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'margin': '20px'}, children=[
    html.H1("Ejemplo Básico de Dash", style={'textAlign': 'center'}),
    
    dcc.Graph(
        id="grafico-dispersion",
        figure=fig
    ),
    
    html.H2("Tabla de Datos", style={'marginTop': '40px'}),
    
    dash_table.DataTable(
        id='tabla-datos',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': '#f1f1f1', 'fontWeight': 'bold'}
    )
])

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
