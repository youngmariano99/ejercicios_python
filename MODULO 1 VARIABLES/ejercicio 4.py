"""**Ejercicio 4:**

Define dos números enteros en variables y
muestra en pantalla el resultado de su suma,
resta, multiplicación y división."""

numeros = [0,1]
numero_elegido = [0] * len(numeros)
for numero in numeros:
    numero_elegido[numero] = int (input("ELije un numero: "))

suma = numero_elegido[0] + numero_elegido [1]
resta = numero_elegido[0] - numero_elegido [1]
multiplicacion = numero_elegido[0] * numero_elegido [1]

print(f"Resultado suma = {suma}")
print(f"Resultado resta = {resta}")
print(f"Resultado multiplicacion = {multiplicacion}")