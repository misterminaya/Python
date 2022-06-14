# Funciones

Los valores que van dentro de la parentesis le llaman parametro

```python
def suma():
    numero_uno = int(input('Ingresa el primer numero entero: '))
    numero_dos = int(input('Ingresa el segundo numero entero: '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma()
```

#### ¿Cuál es la diferencia entre parámetro y argumento? 

Argumento es el valor que pasamos al llamar la función y Parámetro es la 
variable definida en la función la cual recibirá un valor de entrada. 

```python
def suma(numero1): return numero1 + 10
suma(20)
```

Para este ejemplo 20 es el **argumento** y numero1 el **parámetro**


#### ¿Cómo mandar un argumento?

```python
def suma(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print(resultado)


numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))


suma(numero_uno, numero_dos)
```

#### ¿Cómo retornar valores en una función?


```python

def suma(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    return resultado


numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))


resultado = suma(numero_uno, numero_dos)
print(resultado)

```

#### ¿Cómo retornar valores en una función? - reduciendo código


```python
def suma(numero_uno, numero_dos):
    return = numero_uno + numero_dos
    
numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))


resultado = suma(numero_uno, numero_dos)

print('El resultado es: ', resultado)

```

#### ¿Cómo retornar dos valores en una función? 

```python
def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos, 'La funcióń retornar 2 valores'

numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))


resultado, mensaje = suma(numero_uno, numero_dos)
print('El resultado es: ', resultado)
print(mensaje) #Nos devuelve una tupla el resultado

```

Nos devuelve un tupla el resultado


#### ¿Parámetros opcionales?
Los valores que tiene data por default van a la derecha

```python
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)
```


#### ¿Argumentos?
* Argumento parte 1

```python
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)
```

Si queremos que nuestro parámetro reciba una cantidad infinita de ¿Parámetros

```python
def promedio(*args):
    print(args)
    print(type(args))

    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10, 20, 15, 20)
print(resultado)
```

Por convención Python todos los parámetros que tenga *, deben nombrarse como **args**

* Argumento parte 2

```python
def promedio(*args):
    return sum(args) / len(args)


def combinacion(p1, p2, *args, p3=500):
    print(p1)
    print(p2)
    print(args)
    print(p3)

combinacion(10, 20, 1, 2, 3, 4, 5, p3=600)

```

Kwargs 
Cuando usamos solo *  se genera una tupla
```python
def promedio(*args):
    return sum(args) / len(args)

```

Cuando tiene doble *  , lo convierte automáticamente a un diccionario.
```python
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])

```

Podemos crear una función con un solo * o con dos ** 

```python
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')

```
Scopes 

```python
animal = 'León' # Variable global --> funcion, Condicion o Ciclo

def imprimir_animal():
    print(animal)

imprimir_animal()

```

Scopes 1 


```python
def imprimir_animal():
    animal = 'Ballena' # Variable Local -->

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

```

Scopes 2 - (Cómo modificar una variable global en una local)

```python
def imprimir_animal():
    global animal 
    animal = 'Ballena'

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

```

Funciones Anidadas

```python
def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance

    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    print(deposito(10, 20))
    print(retiro(50, 30))

operacion()

```

Funciones Anidadas con Refactor 


```python
def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance

    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado = operacion(10, 30)
print(resultado)

```

Funciones son ciudadanos de primera clase, la funciones pueden ser
argumento de otras funciones 


```python
def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32


mi_funcion = centigrados_a_farhenheit #Almacenamos una funcion dentro de una variable, no poner ()

print(type(mi_funcion))
print(mi_funcion(10))
```


#### Funciones Lambda
**lambda**  <párametros> : <cuerpo de la función>

```python
funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))
```

Funciones lambda sin parámetros 

```python
sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)
```

### ¿Callbacks?


 * 1
```python
promedio = lambda *args : sum(args) / len(args)
print(promedio(10, 10, 9, 8, 7)) 
```


* 2 
```python
aprobatorio = lambda calificacion : calificacion >= 7
print(aprobatorio(5))
```

* 3
```python
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print('No aprobaste la materia')

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 9)
```

### Variables No Locales

```python
e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variables Locales
    b = 'b' # Variables locales


    def funcion_anidada():
        c = 'c' # Variables locales

        nonlocal b  #Con esto hacemos que queremos usar el mismo valor de la variable b
        b = 'Cambio de valor' 

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
    print(b)
    print(id(b))
    #print(c)


funcion_principal()
```

Retornar Funciones 

```python
def saludar():

    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de Python.')

    return mostrar_mensaje


respuesta = saludar()
respuesta()
print(respuesta)
print(type(respuesta))

```

###  Closures
Ya que retorna una funcion la cual puede acceder a la variables 
locales aunque la primera ya haya finalizado

```python
def saludar(username):
    mensaje = f'Hola {username}' # Variable Local


    def mostrar_mensaje(): #Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

respuesta()

```


### Decoradores 
Una funciona toma otra función y retorna otra función, input, output, una funcion

```python
a -> La funcion principal (Decorador)
b -> La funcion de decorar
c -> La funcion decorada 

a(b) -> c
```


Estructura básica de un Decorador

*  Decorador 1

```python
def funcion_a(funcion_b):

    def funcion_c():
        print('>>> Antes del llamado.')
        funcion_b()
        print('>>> Después del llamado.')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una función')

saludar()
```

* Decorador 2 
```python
def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print('>>> Antes del llamado.')

        resultado = funcion_b(*args, **kwargs)

        print('>>> Después del llamado.')

        return resultado

    return funcion_c

@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(10, 20)
print(resultado)
```

### Generador 

```python 
def pares(): # Generador  -> Lazy Iterator
    for numero in range(0, 100, 2):
        yield numero #La funcion suspende su ejecución
        print('Se reanuda la ejecución')


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizado')
```

#### ¿Por qué usar un generador? Son ventajas para interar el uso de la memoria


### Usar Docstring para documentar código

**__doc__** (Quedaran registrados en este documento los Módulos, Clases, Métodos y Funciones)

```python
def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retoma la suma de los parámetros.

    TODO:
        *

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    500

    """
    return numero_1 + numero_2
```

* imprimir la documentacion

```python
print(suma.__doc__)
print(help(suma))
```

* Ejecutar una funcion test 
 * python -m doctest funciones.py(nombre_del_archivo)

La función es un bloque de código que no le pertenece a nadie. Por su parte los métodos son funciones que le 
pertenecen a una clase, y dependiendo del tipo de método (De instancia, clases, estáticos etc... ) 
pueden acceder a los atributos y/o métodos de la clase :D