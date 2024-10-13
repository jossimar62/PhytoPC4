import requests
import sqlite3
from pymongo import MongoClient

# URL del API de SUNAT
url_api = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Conexión a la base de datos SQLite
sqlite_conn = sqlite3.connect('base.db')
sqlite_cursor = sqlite_conn.cursor()

# Crear tabla sunat_info si no existe
sqlite_cursor.execute('''
CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT PRIMARY KEY,
    compra REAL,
    venta REAL
)
''')

# Conexión a MongoDB (localhost en el puerto por defecto)
mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['sunat']
mongo_collection = mongo_db['sunat_info']

# Función para obtener el tipo de cambio de una fecha específica
def obtener_tipo_cambio(fecha):
    response = requests.get(f'{url_api}?fecha={fecha}')
    if response.status_code == 200:
        data = response.json()
        return data['compra'], data['venta']
    return None, None

# Recorrer todas las fechas del 2023
from datetime import datetime, timedelta

fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31)
delta = timedelta(days=1)

fecha_actual = fecha_inicio
while fecha_actual <= fecha_fin:
    fecha_str = fecha_actual.strftime('%Y-%m-%d')
    compra, venta = obtener_tipo_cambio(fecha_str)

    if compra and venta:
        # Insertar datos en SQLite
        sqlite_cursor.execute('''
        INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (fecha_str, compra, venta))

        # Insertar datos en MongoDB
        mongo_collection.update_one(
            {'fecha': fecha_str}, 
            {'$set': {'compra': compra, 'venta': venta}}, 
            upsert=True
        )

    fecha_actual += delta

# Guardar los cambios en SQLite
sqlite_conn.commit()

# Mostrar los datos de la tabla SQLite
sqlite_cursor.execute('SELECT * FROM sunat_info')
rows = sqlite_cursor.fetchall()

for row in rows:
    print(row)

# Cerrar conexiones
sqlite_conn.close()
mongo_client.close()
