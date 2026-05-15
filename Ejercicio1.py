# =====================================================
# EJERCICIO 1
# Empresa de envíos - Clasificación de paquetes
# Conceptos:
# input(), validación, slicing y operador ternario
# =====================================================

# Solicitar etiqueta al usuario
etiqueta = input("Ingrese la etiqueta de rastreo: ")

# Validación de seguridad
if etiqueta == "" or etiqueta is None:
    print("Error: La etiqueta no puede estar vacía.")
else:

    # Separar usando split
    partes = etiqueta.split("-")

    # Extraer categoría usando slicing
    categoria = partes[1][:]

    print(f"Categoría detectada: {categoria}")

    # Operador ternario
    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"

    print(ruta)