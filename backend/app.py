from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from flask import request

app = Flask(__name__)

# =========================================
# CORS
# =========================================
CORS(app)

# =========================================
# CONFIGURACIÓN MYSQL
# =========================================
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'zimbra_db'
}

# =========================================
# FUNCIÓN CONEXIÓN
# =========================================
def obtener_conexion():

    try:

        conexion = mysql.connector.connect(**DB_CONFIG)

        if conexion.is_connected():
            return conexion

    except Error as e:

        print(f"Error crítico al conectar con MySQL: {e}")

        return None


# =========================================
# RUTA PRINCIPAL
# =========================================
@app.route('/')
def home():

    return "Backend Flask funcionando correctamente"


# =========================================
# PRUEBA CONEXIÓN BD
# =========================================
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


# =========================================
# OBTENER PROSPECTO POR ID
# =========================================
@app.route('/api/prospecto/<int:id>', methods=['GET'])
def obtener_prospecto(id):

@app.route('/api/track-event', methods=['POST'])
def track_event():
    data = request.json
    prospecto_id = data.get('prospecto_id')
    tipo_evento = data.get('tipo_evento')
    url_visitada = data.get('url_visitada')

    if not prospecto_id or not tipo_evento or not url_visitada:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    conexion = obtener_conexion()

    if conexion:

        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT
            prospecto_id,
            nombre_empresa,
            estado_prospecto
        FROM prospectos
        WHERE prospecto_id = %s
        """

        cursor.execute(sql, (id,))

        prospecto = cursor.fetchone()

        cursor.close()
        conexion.close()

        if prospecto:

            return jsonify(prospecto)

        else:

            return jsonify({
                "mensaje": "Prospecto no encontrado"
            }), 404

    else:

        return jsonify({
            "mensaje": "Error conexión BD"
        }), 500


# =========================================
# HU06 - REGISTRO DE CONTRATOS
# =========================================
@app.route('/api/contratos', methods=['POST'])
def registrar_contrato():

    data = request.json

    prospecto_id = data['prospecto_id']
    monto_total = data['monto_total']
    fecha_cierre = data['fecha_cierre']
    metodo_pago = data['metodo_pago']
    plan_adquirido = data['plan_adquirido']

    conexion = obtener_conexion()

    if conexion:

        try:

            cursor = conexion.cursor(dictionary=True)

            # =====================================
            # VALIDAR ESTADO DEL PROSPECTO
            # =====================================

            consulta_estado = """
            SELECT estado_prospecto
            FROM prospectos
            WHERE prospecto_id = %s
            """

            cursor.execute(consulta_estado, (prospecto_id,))

            prospecto = cursor.fetchone()

            if not prospecto:

                return jsonify({
                    "mensaje": "Prospecto no encontrado"
                }), 404

            estado_actual = prospecto['estado_prospecto']

            estados_permitidos = [
                    'Nuevo Lead',
                    'En Seguimiento',
                    'En Negociacion',
                    'Propuesta Enviada'
            ]

            if estado_actual not in estados_permitidos:

                return jsonify({
                    "mensaje":
                    f"No se puede cerrar contrato porque el prospecto está en estado: {estado_actual}"
                }), 400
            # =====================================
            # LLAMAR AL PROCEDIMIENTO ALMACENADO (ACID)
            # =====================================
            
            cursor.execute(
                "CALL sp_registrar_contrato(%s, %s, %s, %s, %s)", 
                (prospecto_id, monto_total, fecha_cierre, metodo_pago, plan_adquirido)
            )
            conexion.commit()

            cursor.close()
            conexion.close()

            return jsonify({
                "mensaje": "Contrato registrado correctamente"
            }), 201

        except Exception as e:

            return jsonify({
                "mensaje": str(e)
            }), 500

    else:

        return jsonify({
            "mensaje": "Error conexión BD"
        }), 500


# =========================================
# HU07 - REPORTES
# =========================================
@app.route('/api/reportes', methods=['GET'])
def obtener_reportes():

    conexion = obtener_conexion()

    if conexion:

        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT

            p.prospecto_id,
            p.nombre_empresa,
            p.email_contacto,
            p.estado_prospecto,

            c.monto_total,
            c.metodo_pago,
            c.plan_adquirido,
            c.fecha_cierre

        FROM prospectos p

        LEFT JOIN contratos_comerciales c
        ON p.prospecto_id = c.prospecto_id
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return jsonify(resultados)

    else:

        return jsonify({
            "mensaje": "Error conexión BD"
        }), 500


# =========================================
# EJECUTAR SERVIDOR
# =========================================
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

    app.run(debug=True, port=5000)
