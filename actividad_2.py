#  ACTIVIDAD 2: Calculadora de Notas

print("=" * 45)
print("       CALCULADORA DE NOTAS - SENA ADSO")
print("=" * 45)

# PASO 1: Solicitar las calificaciones al usuario
nota1 = float(input("\nIngresa la calificación del Parcial 1: "))
nota2 = float(input("Ingresa la calificación del Parcial 2: "))
nota3 = float(input("Ingresa la calificación del Parcial 3: "))


# PASO 2: Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3
promedio_redondeado = round(promedio, 2)

# PASO 3: Calcular cuántos puntos le faltan para llegar a 5.0
NOTA_MAXIMA = 5.0
puntos_faltantes = round((NOTA_MAXIMA - promedio), 2)


# PASO 4: Determinar si el estudiante aprueba
NOTA_MINIMA_APROBACION = 3.0
aprueba = promedio >= NOTA_MINIMA_APROBACION


# Mostramos el resultado de aprobación con un mensaje claro
if aprueba:
    print(f"  Estado: APROBADO")
else:
    print(f"  Estado: NO APROBADO")
    

# PASO 5: Mostrar todos los resultados con formato legible
print("\n" + "=" * 45)
print("              REPORTE DE NOTAS")
print("=" * 45)
print(f"  Parcial 1:          {nota1:.2f}")
print(f"  Parcial 2:          {nota2:.2f}")
print(f"  Parcial 3:          {nota3:.2f}")
print("-" * 45)
print(f"  Promedio:           {promedio_redondeado:.2f}")
print(f"  Puntos para 5.0:    {puntos_faltantes:.2f}")
print("-" * 45)