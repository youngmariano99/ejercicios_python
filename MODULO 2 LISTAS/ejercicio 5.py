### **Ejercicio 5: Matrices en listas**

# Crea una matriz de 3x3 representada como una lista de listas e imprime su contenido de forma estructurada.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Tu código aquí

for fila in matriz:
    print(" ".join(map(str, fila)))