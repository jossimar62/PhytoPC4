
import csv
import sqlite3
from datetime import datetime

# Conectar a la base de datos SQLite (o crear una si no existe)
conn = sqlite3.connect('tipos_de_cambio.db')
cursor = conn.cursor()

# Crear la tabla tipo_cambio (solo si no existe ya)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipo_cambio (
    fecha TEXT PRIMARY KEY,
    tipo_cambio REAL
)
''')

# Suponiendo que ya tenemos los tipos de cambio en la tabla, los registros serían algo como:
# cursor.execute("INSERT INTO tipo_cambio (fecha, tipo_cambio) VALUES ('2023-09-15', 3.85)")
# cursor.execute("INSERT INTO tipo_cambio (fecha, tipo_cambio) VALUES ('2023-09-17', 3.90)")
# cursor.execute("INSERT INTO tipo_cambio (fecha, tipo_cambio) VALUES ('2023-10-01', 3.87)")
# conn.commit()

# Función para obtener el tipo de cambio según la fecha
def obtener_tipo_cambio(fecha_compra):
    cursor.execute("SELECT tipo_cambio FROM tipo_cambio WHERE fecha = ?", (fecha_compra,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return None  # Manejar caso si no hay tipo de cambio para esa fecha

# Leer el archivo CSV y procesar los precios
def procesar_ventas(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        print(f"{'Producto':<15}{'Precio en Dólares':<20}{'Precio en Soles':<20}{'Fecha de Compra':<15}")
        print("-" * 70)
        for fila in lector:
            producto = fila['producto']
            precio_dolares = float(fila['precio_dolares'])
            fecha_compra = fila['fecha_compra']
            
            tipo_cambio = obtener_tipo_cambio(fecha_compra)
            
            if tipo_cambio:
                precio_soles = precio_dolares * tipo_cambio
                print(f"{producto:<15}{precio_dolares:<20.2f}{precio_soles:<20.2f}{fecha_compra:<15}")
            else:
                print(f"No se encontró tipo de cambio para la fecha: {fecha_compra}")

# Procesar las ventas del archivo CSV
procesar_ventas('ventas.csv')

# Cerrar la conexión
conn.close()
