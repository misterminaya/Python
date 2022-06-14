# Condiciones 
None --> Es usado para definir un valor vacio

```python
resultado = None #Falso
print(resultado)
print(type(resultado))

resultado = [1, 2, 3]
print(resultado)
print(type(resultado))

```

¿Cómo se representa el valor **Falso** en python?
* False
* None
* 0
* 0.0
* '' / ""
* []
* ()
* {}

#### Estructura de código 


```python
resultado = 11 

if resultado > 10 and resultado < 20:
    print('La variable cumple con la condición')
else:
    print('La condición no se cumplio :( ')

```

#### ¿Cómo trabajar con multiples condiciones?
```python
calificacion = 8 

if calificacion == 10:
    print('Felicidades, aprobasta la materia con una calificación perfecta.')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, Aprobaste la materia')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste la materia.')
else:
    print('Reprobaste la materia.')

```

## ¿Ternario?
```python
calificacion = 10 

color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'


print(calificacion, color)

```

Implementando un nuevo refactor 

```python
color = 'Verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)

```


#### Asignar valores mediante operadores lógicos 

```python

variable = 'Cody' or 'Codigo'

print(variable)

variable = '' or 0 or [] or True
print(variable)

```

Es importante porque podemos esos valores cuando pertenezcan a otras variables

```python

listado = []
nombre = 'Cody'

if listado:
    variable = listado
else:
    variable = nombre 

print(variable)


# Simplificando codigo

variable = listado or nombre
print(variable)


```


## ¿Cómo usar While?
El while es recomendando usar cuando no sepamos cuántas iteraciones realizaremos



```python

contador = 1 
while contador <= 10:
    print(contador)

    contador = contador + 1

#El while es recomendado usar cuando no sepamos cuantas iteraciones realizaremos 


numero = 1234
contador_digitos = 0

while numero >= 1:
    contador_digitos = contador_digitos + 1


    numero = numero / 10


print(contador_digitos)


```

## ¿Qué es el ciclo foreach?

```python
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']

for usuario in usuarios:
    print(usuario)

```
Funcion Range, esto inicia desde 0 hasta el rango solicitado

```python
rango = range(11) # 0 - 10 
print(rango)
print(type(rango))


for valor in rango:
    print(valor)

```

Función Range, enviamos dos valores para definir desde donde y adonde finaliza 
el rango.

```python
rango = range(5, 21) # 5 - 20
print(rango)
print(type(rango))


for valor in rango:
    print(valor)

```

El tercer rango hace referencia a los saltos 


```python
rango = range(5, 21, 2) # 5 - 20
print(rango)
print(type(rango))


for valor in rango:
    print(valor)

```

Funcion Enumerate 

```python
numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    print(indice, numero)

```

Podemos definir el rango de los indices con un segundo parámetro

```python
for indice, numero in enumerate(numeros, 100):
    print(indice, numero)

```

### Break and Continue

```python
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
     print(caracter)
```

Usando condiciones  - Break

```python
for caracter in titulo_curso:

    if caracter == 'P':
        break

    print(caracter)

```

Usando condiciones - Continue 


```python
for caracter in titulo_curso:

    if caracter == ' ':
        continue

    print(caracter)

```

