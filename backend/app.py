from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

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
    'database': ''
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
if __name__ == '__main__':

    app.run(debug=True, port=5000)
