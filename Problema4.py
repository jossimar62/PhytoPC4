# Paso 1: Leer el archivo temperaturas.txt y procesar las temperaturas
temperaturas = []

with open('temperaturas.txt', 'r') as archivo:
    for linea in archivo:
        # Ignorar posibles líneas vacías
        if linea.strip():
            fecha, temperatura = linea.strip().split(',')
            temperaturas.append(float(temperatura))

# Paso 2: Calcular la temperatura promedio, máxima y mínima
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
temperatura_promedio = sum(temperaturas) / len(temperaturas)

# Paso 3: Escribir los resultados en el archivo resumen_temperaturas.txt
with open('resumen_temperaturas.txt', 'w') as archivo_resumen:
    archivo_resumen.write(f"Temperatura máxima: {temperatura_maxima:.2f}°C\n")
    archivo_resumen.write(f"Temperatura mínima: {temperatura_minima:.2f}°C\n")
    archivo_resumen.write(f"Temperatura promedio: {temperatura_promedio:.2f}°C\n")

print("Cálculos completados y resultados guardados en resumen_temperaturas.txt")
