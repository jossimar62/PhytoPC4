import os

def contar_lineas_codigo(ruta_archivo):
    # Validar si el archivo termina en .py
    if not ruta_archivo.endswith(".py"):
        print("El archivo no tiene una extensión .py")
        return

    # Intentar abrir el archivo
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                linea_limpia = linea.strip()  # Eliminar espacios en blanco al inicio y fin de la línea
                if linea_limpia and not linea_limpia.startswith("#"):  # Excluir comentarios y líneas en blanco
                    lineas_codigo += 1

        print(f"Número de líneas de código (sin comentarios ni líneas en blanco): {lineas_codigo}")
    
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, verifique la ruta e intente nuevamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Función principal para solicitar la ruta al usuario
def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

# Ejecutar el programa
if __name__ == "__main__":
    main()
