import requests
import zipfile
import os

# Paso 1: Descargar la imagen desde la URL
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
imagen_nombre = "imagen_descargada.jpg"

# Realizar la solicitud GET para descargar la imagen
respuesta = requests.get(url)

# Guardar la imagen en el disco local
with open(imagen_nombre, 'wb') as archivo_imagen:
    archivo_imagen.write(respuesta.content)

print(f"Imagen descargada y guardada como {imagen_nombre}")

# Paso 2: Crear un archivo ZIP que contenga la imagen
nombre_zip = "imagen_comprimida.zip"
with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
    archivo_zip.write(imagen_nombre)

print(f"Imagen comprimida y guardada como {nombre_zip}")

# Paso 3: Descomprimir el archivo ZIP
directorio_extraido = "imagen_extraida"
with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
    archivo_zip.extractall(directorio_extraido)

print(f"Imagen extraída en la carpeta {directorio_extraido}")

# Limpiar: eliminar archivo de imagen original y ZIP
os.remove(imagen_nombre)
os.remove(nombre_zip)
