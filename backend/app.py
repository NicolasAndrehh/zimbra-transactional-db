from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from flask import request

app = Flask(__name__)


CORS(app)


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'zimbra_db'
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

@app.route('/api/track-event', methods=['POST'])
def track_event():
    data = request.json
    prospecto_id = data.get('prospecto_id')
    tipo_evento = data.get('tipo_evento')
    url_visitada = data.get('url_visitada')

    if not prospecto_id or not tipo_evento or not url_visitada:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    conexion = obtener_conexion()
    if not conexion:
        return jsonify({"error": "Fallo la conexión a BD"}), 500

    cursor = conexion.cursor()

    try:
        # Iniciar transacción
        conexion.start_transaction()

        # HU04: Guardar el evento web en tu tabla actividades_web
        insert_event_query = """
            INSERT INTO actividades_web (prospecto_id, tipo_evento, url_visitada) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_event_query, (prospecto_id, tipo_evento, url_visitada))

        # Lógica de Lead Scoring (Puntajes de ejemplo)
        puntos_a_sumar = 0
        if tipo_evento == 'Visita Precios':
            puntos_a_sumar = 10
        elif tipo_evento == 'Descarga':
            puntos_a_sumar = 5
        elif tipo_evento == 'Login':
            puntos_a_sumar = 2

        if puntos_a_sumar > 0:
            # HU05: Actualizar puntaje usando INSERT ... ON DUPLICATE KEY UPDATE
            # Esto maneja el caso donde el prospecto aún no tenga registro en puntajes_scoring
            update_scoring_query = """
                INSERT INTO puntajes_scoring (prospecto_id, puntos_acumulados)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE puntos_acumulados = puntos_acumulados + %s
            """
            cursor.execute(update_scoring_query, (prospecto_id, puntos_a_sumar, puntos_a_sumar))

            # Lógica adicional: Cambiar estado a 'Tibio' si pasa de 15 puntos (opcional)
            # cursor.execute("UPDATE prospectos SET estado_prospecto = 'Tibio' WHERE prospecto_id = %s AND (SELECT puntos_acumulados FROM puntajes_scoring WHERE prospecto_id = %s) > 15", (prospecto_id, prospecto_id))

        conexion.commit()
        return jsonify({"estado": "exito", "mensaje": "Evento registrado y scoring actualizado"}), 201

    except Error as e:
        conexion.rollback()
        return jsonify({"estado": "error", "mensaje": f"Error en transacción: {e}"}), 500
    finally:
        cursor.close()
        conexion.close()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # debug=True reinicia el servidor automáticamente cuando guardas cambios
    app.run(debug=True, port=5000)
