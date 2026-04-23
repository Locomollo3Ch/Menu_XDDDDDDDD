def mostrar_menu():
    print("\n" + "="*45)
    print("Sistema de análisis sísmico")
    print("="*45)
    print("\n" + "1. Consulta web")
    print("2. Consulta de registros")
    print("3. Estadísticas")
    print("4. Gráficas")
    print("5. Borrar registros")
    print("6. Guardar y salir\n")
    print("="*45)

print(int(input("\nIngrese una opción:\n")))


def ejecutar_opción(opción):
    if opción == "1":
        xd = 2
        print(xd)

print(mostrar_menu())