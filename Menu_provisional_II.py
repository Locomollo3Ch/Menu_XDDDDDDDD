import os
from datetime import datetime
from Modulos import api_earthquakes, txt_manager, excel_manager, stats, graphs, utils

def mostrar_menu():
    print("\n" + "="*45)
    print("Sistema de análisis sísmico")
    print("="*45)
    print("\n1. Consulta web")
    print("2. Consulta de registros")
    print("3. Estadísticas")
    print("4. Generar Gráficas")
    print("5. Borrar registros")
    print("6. Guardar y salir\n")
    print("="*45)

def ejecutar_programa():
    datos_sismicos = []
    
    while True:
        mostrar_menu()
        try:
            opción = int(input("Seleccione una opción (1-6): "))
        except ValueError:
            print("\nError: Por favor, ingrese un número válido.")
            continue

        if opción == 1:
            print("\n---- Consulta Web ----")
            def obtener_datos_api():
                url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

                try:
                    respuesta = requests.get(url)
                    respuesta.raise_for_status()
                    return respuesta.json()
                except requests.exceptions.RequestException as e:
                    print("Error al obtener datos:", e)
                    return None


            def procesar_datos(data_json):
                resultados = []

                if not data_json:
                    return resultados

                for evento in data_json["features"]:
                    propiedades = evento["properties"]
                    geometria = evento["geometry"]

                    magnitud = propiedades.get("mag")
                    lugar = propiedades.get("place")
                    fecha = propiedades.get("time")

                    if fecha:
                        fecha = datetime.fromtimestamp(fecha / 1000).strftime("%Y-%m-%d %H:%M:%S")

                    profundidad = geometria["coordinates"][2]

                    resultados.append({
                        "magnitud": magnitud,
                        "lugar": lugar,
                        "fecha": fecha,
                        "profundidad": profundidad
                    })

                return resultados

            def guardar_datos(resultados):
                carpeta = "datos"
                archivo = "terremotos.csv"

                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)

                ruta_archivo = os.path.join(carpeta, archivo)

                try:
                    with open(ruta_archivo, "w", encoding="utf-8") as f:
                       f.write("Magnitud,Lugar,Fecha,Profundidad\n")

                    for dato in resultados:
                            linea = f"{dato['magnitud']},{dato['lugar']},{dato['fecha']},{dato['profundidad']}\n"
                            f.write(linea)

                    print("Datos guardados correctamente en:", ruta_archivo)

                except Exception as e:
                    print("Error al guardar datos:", e)


            def main():
                datos = obtener_datos_api()
                procesados = procesar_datos(datos)
                guardar_datos(procesados)


            if __name__ == "__main__":
                main()

        elif opción == 2:
            print("\n---- Registros en Memoria ----")
            if not datos_sismicos:
                print("No hay datos cargados.")
            else:
                for idx, sismo in enumerate(datos_sismicos, 1):
                    print(f"{idx}. {sismo['lugar']} - Mag: {sismo['magnitud']}")

        elif opción == 3:
            print("\n---- Estadísticas de Magnitud ----")
            if datos_sismicos:
                promedio = stats.calcular_promedio_magnitud(datos_sismicos)
                maximo = stats.calcular_maximo(datos_sismicos)
                print(f"Promedio: {promedio:.2f}")
                print(f"Magnitud Máxima: {maximo}")
            else:
                print("Cargue datos primero (Opción 1).")

        elif opción == 4:
            print("\n---- Generando Gráficas... ----")
            if datos_sismicos:
                graphs.generar_graficas(datos_sismicos)
                print("✅ Gráficas guardadas en la carpeta 'Gráficas/'")
            else:
                print("No hay datos para graficar.")

        elif opción == 5:
            confirmar = input("\n¿Seguro que desea borrar TODO? (s/n): ").lower()
            if confirmar == 's':
                datos_sismicos.clear()
                print("🗑️ Registros eliminados de la memoria.")
            else:
                print("Operación cancelada.")

        elif opción == 6:
            print("\nFinalizando y guardando reporte final...")
            if datos_sismicos:
                # Persona 4: Guarda en Excel antes de salir
                excel_manager.guardar_excel(datos_sismicos)
            print("👋 Sistema cerrado correctamente.")
            break
        
        else:
            print("\n Opción no válida (1-6).")

if __name__ == "__main__":
    ejecutar_programa()