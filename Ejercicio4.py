# =====================================================
# EJERCICIO 4
# Auditoría de registros
# Conceptos:
# range, continue, break y operador %
# =====================================================

# Recorrer registros del 1 al 50
for numero in range(1, 51):

    # Saltar múltiplos de 3
    if numero % 3 == 0:
        continue

    # Detener proceso en 42
    if numero == 42:
        print("Brecha de seguridad detectada.")
        break

    # Procesar registros válidos
    print(f"Procesando registro ID: {numero}")
