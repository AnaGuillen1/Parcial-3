# =====================================================
# EJERCICIO 5
# Privacidad de usuarios
# Conceptos:
# split(), slicing negativo y for anidado
# =====================================================

# Solicitar nombre completo
nombre_completo = input("Ingrese su nombre completo: ")

# Convertir en lista
nombres = nombre_completo.split()

# Invertir usando slicing negativo
invertido = nombres[::-1]

# Recorrer palabras
for palabra in invertido:

    # Recorrer letras
    for letra in palabra:
        print(letra, end=".")

    # Separación entre palabras
    print(" ", end="")
