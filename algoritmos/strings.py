# 1. - Reemplaza vocales por  @. 

mensaje = 'Hola Mundo'
vocales_minusculas = ['a', 'e', 'i', 'o', 'u']
vocales_mayusculas = ['A', 'E', 'I', 'O', 'U' ]

nuevo_mensaje = ''

for caracter in mensaje:
    if caracter in vocales_minusculas or caracter in vocales_mayusculas:
        caracter = '@'
    
    nuevo_mensaje = nuevo_mensaje + caracter

print(nuevo_mensaje)