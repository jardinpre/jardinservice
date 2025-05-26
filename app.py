from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time
import datetime

app = Flask(__name__)
CORS(app)  # Permite recibir peticiones desde HTML local o navegador

# Configuración de conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'jardin_emanuel'
}

@app.route('/guardar_respuesta', methods=['POST'])
def guardar_respuesta():
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    autorizacion = data.get('autorizacion')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
        INSERT INTO respuestas_taller (nombre, telefono, autorizacion)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nombre, telefono, autorizacion))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'mensaje': 'Datos guardados correctamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
