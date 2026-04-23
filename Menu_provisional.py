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

def ejecutar_opción(opción):
    if opción == 1:
        print("\n---- Consulta web ----")

    elif opción == 2:
        print("\n---- Consulta de registros ----")

    elif opción == 3:
        print("\n---- Estadísticas ----")

    elif opción == 4:
        print("\n---- Gráficas ----")

    elif opción == 5:
        print("\n---- Borrar registros ----")
        respuesta = input("¿Está seguro de eliminar todos los registros? (s/n):\n")
        if respuesta == "s":
            xd1 = 2 #Son solo para rellenar, al rato es modificado.

        elif respuesta == "n":
            xd2 = 3
        
        else:
            print("\nError. Ingrese 's' o 'n'.")

    elif opción == 6:
        print("\nGuardando información...")
    
    else:
        print("\nOpcion no válida. Ingrese un valor entre el 1 al 6.")

def main():
    xd3=4

print(mostrar_menu())