from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


CORS(app)


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': ''
}

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)

        if conexion.is_connected():
            return conexion

    except Error as e:
        print(f"Error crítico al conectar con MySQL: {e}")
        return None


@app.route('/')
def home():
    return "Backend Flask funcionando correctamente"


@app.route('/api/test-db', methods=['GET'])
def test_db():

    conexion = obtener_conexion()

    if conexion:
        conexion.close()

        return jsonify({
            "estado": "exito",
            "mensaje": "¡Backend conectado a MySQL correctamente!"
        }), 200

    else:
        return jsonify({
            "estado": "error",
            "mensaje": "Fallo la conexión a la base de datos."
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
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
