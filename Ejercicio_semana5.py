# Determina si un estudiante cumple los requisitos para obtener una beca.

print("EVALUACIÓN DE BECA ESTUDIANTIL")

try:
    # Solicitar el promedio, la asistencia y la participación en el programa.
    promedio = float(input("Ingrese el promedio académico (0 a 100): "))
    asistencia = float(input("Ingrese el porcentaje de asistencia (0 a 100): "))
    programa_apoyo = input("¿Pertenece a un programa de apoyo? (si/no): ").strip().lower()

    # Comprobar que los datos ingresados sean válidos.
    if not (0 <= promedio <= 100 and 0 <= asistencia <= 100):
        print("Error: el promedio y la asistencia deben estar entre 0 y 100.")
    elif programa_apoyo != "si" and programa_apoyo != "sí" and programa_apoyo != "no":
        print("Error: debe responder si o no a la pregunta del programa de apoyo.")
    else:
        pertenece_apoyo = programa_apoyo == "si" or programa_apoyo == "sí"

        # Basta con cumplir una de las dos condiciones para obtener la beca.
        # Condición 1: promedio de al menos 80 y asistencia de al menos 85%.
        # Condición 2: pertenecer al programa y tener al menos 75% de asistencia.
        if (promedio >= 80 and asistencia >= 85) or (pertenece_apoyo and asistencia >= 75):
            print("El estudiante obtiene la beca.")
        else:
            print("El estudiante no obtiene la beca.")

except ValueError:
    # Evitar que el programa falle si se escribe texto en un campo numérico.
    print("Error: ingrese números válidos para el promedio y la asistencia.")

# Mantener la ventana abierta si se ejecuta el archivo con doble clic.
input("Presione Enter para salir...")