### **Ejercicio 2: Agregar y modificar valores en un diccionario**

#Dado el siguiente diccionario de productos, agrega un nuevo producto y actualiza el precio de la "leche".

productos = {
    "pan": 150,
    "leche": 200,
    "huevos": 300
}
# Tu código aquí

productos["leche"] = 250
productos.update({"manteca" : 250})

print(productos)
