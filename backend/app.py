from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Habilitar CORS para permitir que el frontend en React (puerto 5173) se comunique con Flask (puerto 5000)
CORS(app)

# Configuración centralizada de la base de datos
# IMPORTANTE: Cada miembro del equipo debe poner aquí su usuario y contraseña local de MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',      # Usuario por defecto en local
    'password': '',      # Pon tu contraseña aquí si tienes una configurada
    'database': 'SI_Zimbra'
}

def obtener_conexion():
    """Función para crear y retornar la conexión a la BD."""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error crítico al conectar con MySQL: {e}")
        return None

# Ruta de prueba para verificar que todo funciona
@app.route('/api/test-db', methods=['GET'])
def test_db():
    conexion = obtener_conexion()
    if conexion:
        conexion.close() # Siempre cerrar la conexión después de usarla
        return jsonify({"estado": "exito", "mensaje": "¡Backend conectado a MySQL correctamente!"}), 200
    else:
        return jsonify({"estado": "error", "mensaje": "Fallo la conexión a la base de datos."}), 500

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # debug=True reinicia el servidor automáticamente cuando guardas cambios
    app.run(debug=True, port=5000)