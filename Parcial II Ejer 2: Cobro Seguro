# =====================================================
# EJERCICIO 2
# Sistema de cobro seguro
# Conceptos:
# while, try-except, Decimal y f-string
# =====================================================

from decimal import Decimal

# Variable acumuladora
total = Decimal("0")

while True:

    try:
        entrada = input("Ingrese el precio del producto (0 para salir): ")

        # Convertir a Decimal
        precio = Decimal(entrada)

        # Condición de salida
        if precio == 0:
            break

        # Acumular total
        total += precio

    except ValueError:
        print("Advertencia: Debe ingresar un número válido.")

    except:
        print("Error en el sistema.")

# Mostrar total final
print(f"Total acumulado: ${total}")
