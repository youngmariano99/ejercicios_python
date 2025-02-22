### **Ejercicio 1: Manipulación de cadenas**

"""Dada la siguiente cadena, realiza las siguientes operaciones:

1. Convierte toda la cadena a mayúsculas.
2. Reemplaza la palabra "rápido" por "lento".
3. Divide la cadena en una lista de palabras. """

texto = "El zorro rápido salta sobre el perro perezoso"
# Tu código aquí

texto_mayuscula = texto.upper()
texto_cambiado = texto_mayuscula.replace("RÁPIDO", "LENTO")

print(texto_cambiado)