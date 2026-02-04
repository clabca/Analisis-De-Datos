
from flask import Flask, render_template_string
# Crear una aplicación Flask
app = Flask(__name__)
# Definir una ruta para la página principal
@app.route("/")
def home():
    # Datos de ejemplo
    data = [
        {"nombre": "Ana", "edad": 22, "ciudad": "Madrid"},
        {"nombre": "Luis", "edad": 29, "ciudad": "Barcelona"},
        {"nombre": "Sofia", "edad": 24, "ciudad": "Valencia"}
    ]
    # Plantilla HTML simple
    html_template = """
    <html>
        <head>
            <title>Ejemplo Básico de Flask</title>
        </head>
        <body>
            <h1>Lista de Personas</h1>
            <table border="1">
                <tr>
                    <th>Nombre</th>
                    <th>Edad</th>
                    <th>Ciudad</th>
                </tr>
                {% for persona in data %}
                <tr>
                    <td>{{ persona.nombre }}</td>
                    <td>{{ persona.edad }}</td>
                    <td>{{ persona.ciudad }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """
    # Renderizar la plantilla con los datos
    return render_template_string(html_template, data=data)
# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
# =====================================