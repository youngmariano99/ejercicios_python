### **Ejercicio 3: Comprobar prefijos y sufijos**

# Dado el siguiente archivo, verifica si termina en `.pdf` y si empieza con `reporte_`.


archivo = "reporte_financiero.pdf"
# Tu código aquí

if ".pdf" in archivo and archivo.startswith("reporte_"):
    print("El arhivo cumple con los requisitos")
else:
    print("El archivo no cumple con los requisitos")
