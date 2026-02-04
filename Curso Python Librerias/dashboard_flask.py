# dashboard_flask_completo.py

from flask import Flask, render_template_string, request  # Flask y funciones de plantillas
import pandas as pd
import plotly.express as px
import plotly  # Necesario para PlotlyJSONEncoder
import json

# -----------------------------
# Crear la aplicación Flask
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Datos de ejemplo
# -----------------------------
data = {
    "Nombre": ["Ana", "Luis", "Sofia", "Carlos", "Marta"],
    "Edad": [22, 29, 24, 32, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
}
df = pd.DataFrame(data)

# -----------------------------
# Ruta principal
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Esta función maneja la página principal:
    - Permite filtrar los datos por ciudad
    - Muestra un gráfico de dispersión con Plotly
    - Muestra una tabla HTML con los datos filtrados
    """

    # -----------------------------
    # Obtener filtro de ciudad desde el formulario
    # -----------------------------
    ciudad_seleccionada = request.form.get("ciudad", "Todas")

    # -----------------------------
    # Filtrar DataFrame según la ciudad seleccionada
    # -----------------------------
    if ciudad_seleccionada != "Todas":
        df_filtrado = df[df["Ciudad"] == ciudad_seleccionada]
    else:
        df_filtrado = df.copy()

    # -----------------------------
    # Crear gráfico de dispersión interactivo con Plotly
    # -----------------------------
    fig = px.scatter(
        df_filtrado,
        x="Nombre",
        y="Edad",
        color="Ciudad",
        size="Edad",         # Tamaño de los puntos según edad
        hover_data=["Ciudad"],
        title="Edad por Nombre y Ciudad"
    )

    # Convertir gráfico a JSON para renderizar en la plantilla HTML
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Lista de ciudades para el select
    ciudades = ["Todas"] + df["Ciudad"].unique().tolist()

    # -----------------------------
    # Plantilla HTML con estilo y gráficos
    # -----------------------------
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Dashboard Flask + Plotly</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            table { border-collapse: collapse; width: 50%; margin: 20px auto; }
            th, td { padding: 8px; text-align: center; border: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            h1 { text-align: center; }
            form { text-align: center; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <h1>Mini Dashboard Flask + Plotly</h1>
        
        <!-- Formulario para filtrar por ciudad -->
        <form method="post">
            <label for="ciudad">Filtrar por Ciudad:</label>
            <select name="ciudad" id="ciudad">
                {% for c in ciudades %}
                    <option value="{{ c }}" {% if c == ciudad_seleccionada %}selected{% endif %}>{{ c }}</option>
                {% endfor %}
            </select>
            <input type="submit" value="Filtrar">
        </form>
        
        <!-- Gráfico interactivo -->
        <div id="grafico" style="width:70%; margin:auto;"></div>
        <script>
            var graphs = {{ graphJSON | safe }};
            Plotly.newPlot('grafico', graphs.data, graphs.layout);
        </script>
        
        <!-- Tabla de datos filtrados -->
        <h2>Tabla de Datos</h2>
        <table>
            <tr>
                {% for col in df_filtrado.columns %}
                    <th>{{ col }}</th>
                {% endfor %}
            </tr>
            {% for row in df_filtrado.itertuples() %}
            <tr>
                <td>{{ row.Nombre }}</td>
                <td>{{ row.Edad }}</td>
                <td>{{ row.Ciudad }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    # Renderizar la plantilla con los datos y el gráfico
    return render_template_string(
        html_template,
        df_filtrado=df_filtrado,
        graphJSON=graphJSON,
        ciudades=ciudades,
        ciudad_seleccionada=ciudad_seleccionada
    )

# -----------------------------
# Ejecutar la aplicación
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
# =====================================