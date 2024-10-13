import os

# Función para crear un archivo con la tabla de multiplicar de un número dado
def crear_tabla_multiplicar(n):
    nombre_fichero = f"tabla-{n}.txt"
    with open(nombre_fichero, 'w') as fichero:
        for i in range(1, 11):
            fichero.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}")

# Función para leer y mostrar la tabla de multiplicar desde un archivo
def leer_tabla_multiplicar(n):
    nombre_fichero = f"tabla-{n}.txt"
    try:
        with open(nombre_fichero, 'r') as fichero:
            contenido = fichero.readlines()
            print(f"Tabla de multiplicar del {n}:")
            for linea in contenido:
                print(linea, end="")
    except FileNotFoundError:
        print(f"El archivo {nombre_fichero} no existe.")

# Función para leer una línea específica de la tabla de multiplicar
def leer_linea_tabla_multiplicar(n, m):
    nombre_fichero = f"tabla-{n}.txt"
    try:
        with open(nombre_fichero, 'r') as fichero:
            contenido = fichero.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m} de la tabla del {n}: {contenido[m-1]}", end="")
            else:
                print("El número m debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo {nombre_fichero} no existe.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea específica de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                crear_tabla_multiplicar(n)
            else:
                print("El número debe estar entre 1 y 10.")
        
        elif opcion == '2':
            n = int(input("Ingrese un número entre 1 y 10 para leer la tabla: "))
            if 1 <= n <= 10:
                leer_tabla_multiplicar(n)
            else:
                print("El número debe estar entre 1 y 10.")

        elif opcion == '3':
            n = int(input("Ingrese un número entre 1 y 10 para leer la tabla: "))
            m = int(input("Ingrese la línea de la tabla que desea leer (1-10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                leer_linea_tabla_multiplicar(n, m)
            else:
                print("Ambos números deben estar entre 1 y 10.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecución del menú principal
if __name__ == "__main__":
    menu()
