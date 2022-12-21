# Variables 

```python
curso = 'Curso profesional de python'
print(curso)

# Modfificar el contenido de la variables

curso = 'Curso python'

```

## Variables contantes
Por convencio, la variables constantes se nombran en mayúsculas

```python
TITULO_CURSO = 'Python'
print(TITULO_CURSO)
```



# Palabras reservadas en python
Toda la lista de palabras reservadas [link](https://linktodocumentation)


# Tipos de datos 

- **INT** : Amacena valores enteros que pueden ser positivos o negativos y no contienen ningun punto decimal

```python
num1 = 10
num2 = 15 

```
- **FLOAT** : Estos son números reales de coma flotante que almacenan los valores decimales. se trata de partes enteras y fraccionarias.

```python
fnum1 = 23,5
fnum2 = 67,8 
```

- **COMPLEJO** : Números complejos especificados como parte real y parte imaginaria. Se almacenan de forma de a + bj  donde **a** es la parte real y **bj** representa la parte imaginaria.

```python
cnum1 = 2 + 3j
cnum2 = 5 - 7j

type(cnum1)
<class 'complex'>
```

- **BOOL** :  True - False 

```python
valor = False
```

# Operadores Básicos 


### Operadores Relacionales

Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleando (true o false) basado en la condición

| OPERADOR  | DESCRIPCIÓN                                                                                   | USO                       |
| ----------| --------------------------------------------------------------------------------------------- | ------------------------- |
|    >      | Devuelve True si el operador de la izquierda es mayor que el operador de la derecha           | 12 > 3 devuelve True      |
|   <       | Devuelve True si el operador de la derecha es mayor que el operador de la izquierda           | 12 < 3 devuelve False     |
|   ==      | Devuelve True si ambos operandos son iguales                                                  | 	12 == 3 devuelve False  |
|   >=      | Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha   | 12 >= 3 devuelve True     |
|   <=      | Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	| 12 <= 3 devuelve False    |
|   !=      | Devuelve True si ambos operandos no son iguales                                               | 12 != 3 devuelve True     |


### Operadores Aritméticos

Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.

| OPERADOR  | DESCRIPCIÓN                                            | USO                       |
| ----------| -------------------------------------------------------| ------------------------- |
|    +      | Realiza Adición entre los operandos                    | 12 + 3 = 15               |
|   -       | Realiza Substracción entre los operandos               | 12 - 3 = 9                |
|    *      | Realiza Multiplicación entre los operandos             | 12 * 3 = 36               |
|   /       | Realiza División entre los operandos                   | 12 / 3 = 4                |
|    %      | Realiza un módulo entre los operandos	                 | 16 % 3 = 1                |
|   **      | Realiza la potencia de los operandos                   | 12 ** 3 = 1728            |
|   //      | Realiza la división con resultado de número entero     | 18 // 5 = 3               |



### Operadores Bit a Bit

Un operador bit a bit realiza operaciones en los operandos bit a bit
- Consideremos a = 2 (en binario = 10) y b = 3 (en binario = 11) para los siguientes casos.

| OPERADOR  | DESCRIPCIÓN                                                                                                            | USO                       |
| ----------| -----------------------------------------------------------------------------------------------------------------------| ------------------------- |
|    &      | Realiza bit a bit la operación AND en los operandos                                                                    |a & b = 2 (Binario: 10 & 11 = 10)            |
|    !      | Realiza bit a bit la operación OR en los operandos                                                                     | a or b = 3 (Binario: 10 | 11 = 11)              |
|    ^      | Realiza bit a bit la operación XOR en los operandos                                                                    | a ^ b = 1 (Binario: 10 ^ 11 = 01)              |
|    ~      | Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando                                         | ~a = -3 (Binario: ~(00000010) = (11111101))          |
|    >>     | Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha          | a >> b = 0 (Binario: 00000010 >> 00000011 = 0)          |
|    <<     | Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha   | a << b = 16 (Binario: 00000010 << 00000011 = 00001000)|


### Operadores de Asignación

Se utiliza un operador de asignación para asignar valores a una variable. Esto generalmente se combina con otros operadores
(como aritmetica, bit a bit) donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.

| OPERADOR  | DESCRIPCIÓN                                    |
| ----------| -----------------------------------------------|
|    =      |  a = 5. El valor 5 es asignado a la variable a |
|   +=      |  a += 5 es equivalente a a = a + 5             |
|   -=      |  a -= 5 es equivalente a a = a - 5             |
|   *=      |  a *= 3 es equivalente a a = a * 3             |
|   /=      |  a /= 3 es equivalente a a = a / 3             |
|   %=      |  a %= 3 es equivalente a a = a % 3             |
|   **=     |  a **= 3 es equivalente a a = a ** 3           |
|   //=     |  a //= 3 es equivalente a a = a // 3           |
|   &=      |  a &= 3 es equivalente a a = a & 3             |
|   1=      |  a 1= 3 es equivalente a a = a 1 3             |
|   ^=      |  a ^= 3 es equivalente a a = a ^ 3             |
|   >>=     |  a >>= 3 es equivalente a a = a >> 3           |
|   <<=     |  a <<= 3 es equivalente a a = a << 3           |


### Operadores Lógicos 
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los
operadores lógicos utilizados en Python son and, or, y not


| OPERADOR  | DESCRIPCIÓN                                            | USO                       |
| ----------| -------------------------------------------------------| ------------------------- |
|    and    | Devuelve True si ambos operandos son True              | 	a and b                  |
|    or     | Devuelve True si alguno de los operandos es True       |  a or b                   |
|    not    | Devuelve True si alguno de los operandos False         |  not a                    |


### Operadores de pertenencia

Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia(lista, strings, tuplas)

- **in** y **not in** son operadores de pertenencia
- **in** devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
- **not in** devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.

```python

a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print 3 in a # Muestra True 
  
#No está 12 en la lista a?
print 12 not in a # Muestra True
  
str = "Hello World"
  
#Contiene World el string str?
print "World" in str # Muestra True
  
#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print "world" in str # Muestra False  

print "code" not in str # Muestra True

```

### Operadores de Identidad 

Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

- **is** y **is not** son operadores de identidad
- **is** devuelve True si los operadores se refieren al mismo objeto. En caso contrario devuelve False
- **is not** devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.

```python

a = 3
b = 3  
c = 4
print a is b # muestra True
print a is not b # muestra False
print a is not c # muestra True

x = 1
y = x
z = y
print z is 1 # muestra True
print z is x # muestra True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print str1 is str2 # muestra True
print "Code" is str2 # muestra False

a = [10,20,30]
b = [10,20,30]

print a is b # muestra False (ya que las listas son objetos mutables en Python)  

```





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

# Clases

Para crear las clases se usa la nomenclatura CamelCase por convención

```python
class Usuario:
    pass


cody = Usuario()
print(cody)

```

Los atributos de la clase: 

* Se puede dividir los atributos en dos partes
* Attrs de la clase: Atributos pertenecen a una clase.
* Attrs de instancia: Atributos pertenecen a un objeto

```python
class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = ''



Usuario.username = 'User1' #Moficando el atributo de clase Usuario

print(Usuario.username)
```

#### Atributos de instancia
```python
class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = ''


# El objeto es user1
# __dict__
user1 = Usuario()
user1 = Usuario()

#1. Verificar si el attr existe dentro del objeto.
#2. Verificasi el attrs existe dentro de la clase --> Lectura.
#3. Lanzar un error en caso no encuentra un attr en el objeto o dentro de la clase.

print(user1.username)
print(Usuario.username)


print(user1.__dict__) # Dict
```

#### Atributos dinámicos

```python
class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = ''


# El objeto es user1
# __dict__
user1 = Usuario()
user1 = Usuario()

#1. Verificar si el attr existe dentro del objeto.
#2. Verificasi el attrs existe dentro de la clase --> Lectura.
#3. Lanzar un error en caso no encuentra un attr en el objeto o dentro de la clase.

print(user1.username)
print(Usuario.username)


print(user1.__dict__) # Dict


user1.username = 'Cody' # Añadimos el attrs al objeto 
user1.password = '1234'

print(user1.username) # De instancia


print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__) # Dict
```

## Métodos
Como crear métodos dentro de una clase,  (Basta con crear funciones)


```python
class Usuario:

    def inicializar(self, username, password):
        # Agregando atributos al objeto
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()

user1.inicializar('user1', 'password1')
user2.inicializar('user2', 'password2')

print(user1.__dict__)
print(user2.__dict__)

```

### Usar el método INIT
```python
class Usuario:
    # __Object__
    def __init__(self, username='', password='') -> None:
        self.username = username
        self.password = password


user1 = Usuario('user1', 'password1')
user2 = Usuario('user2', 'password2')
user3 = Usuario('user3', 'password3')
user4 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)

```

### ¿Que son las herencias? ???????
```python
class Mascota: # Clase padre
    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')

class Perro(Mascota): # Clase hija
    pass


class Gato(Mascota):
    pass


duke = Perro()
duke.comer()
duke.dormir()


patricio =  Gato()
patricio.comer()
patricio.dormir()

```

### ¿Que son las herencias multiples?
```python

class Animal(): # Clase Padre 
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal): # Clase padre
    pass


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino): #Clase hija
    pass


patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()

```

### SObreescritura de métodos o sobrecarga de métodos
```python
class Animal(): # Clase Padre 
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal): # Clase padre
    def comer(self):
        print('La mascota come')


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino): #Clase hija
    pass

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')

patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
```

### SObreescritura 2 parte

```python
class Animal(): # Clase Padre 
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal): # Clase padre
    def comer(self):
        print('La mascota come')


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino): #Clase hija
    pass

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')

patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()

```

## ¿Que son los métodos? 


```python
class Circulo:
    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)


resultado = Circulo.area(14)
print(resultado)
```

Self por convención lo usaremos siempre que nuestro método sea un método de
 instancias, es decir cuando un objeto pueda llamar al método.
Por su parte cls lo usaremos cuando el método sea un método de clases,
esto quiere decir que  sea la clases misma quien pueda llamar a ese método.

# Diccionario 


```python
diccionario = {}
diccionario = dict()
```

{ llave : El valor el cual queremos asociar}

```python
diccionario = {"total": 55}
diccionario = {"total":55, "descuento": True, "subtotal": 15}
diccionario = {"total":55, 10: "Curso de Python", (1,2,3):True}
```


```python
usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23,
    'curso' : 'Curso de Python',
    'skills' : {
        'programacion' : True,
        'base_de_datos' : False

        },
    'medallas' : ['básico', 'intermedio']
 }

```

Creaccion del diccionario 

```python
diccionario = dict()
```

Agregar nuevo valor a la llave 

```python
diccionario['Usuario'] = 'eduardo'
```

Actualizar valor mediante una llave
```python
diccionario['usuario'] = 'eduardo_gpg'
```

Obtener valor mediante una llave 
```python
print(diccionario['usuario'])

diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
diccionario.keys()
```

Usando los **gets**
```python
usuario = {
    'name': 'Junior Lastname',
    'age' : 26,
    'job' : 'Software developer',
 }

calificaciones = usuario.get('calificaciones', [])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)


usuarios = [ 'Eduardo', 'Fernando', 'Uriel', 'Rafael']
diccionario = {usuario:position + 1 
                        for position, usuario in enumerate(usuarios)}

print(diccionario)

```

¿Cómo saber la longitud de un diccionario?

```python
elementos = {}
elementos['nombre'] = 'Cody'

print(elementos)
print(len(elementos))

```

¿Cómo obtener elementos?

```python
diccionario = {'a':1, 'b':2, 'c':3, 'd':4}
valor = diccionario['d']

print(valor)
print('a' in diccionario)


#get 

valor = diccionario.get('d')
print(valor)

```

En caso la llave no existe en el diccionario

* Modelo 1 

```python
valor = diccionario.get('z')
print(valor)
```

* Modelo 2 

```python
valor = diccionario.get('z', 'La llave no existe en el dict.')
print(valor)
```

* Modelo 3  --  **setDefault**

```python
valor = diccionario.get('z', 5)
print(valor)

```

llaves, items, valores

```python
diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

llaves = diccionario.keys()
print(llaves)


```

¿Cómo convertir la llaves en tuplas?

```python
llaves = tuple(diccionario.keys())
print(llaves)

valores = diccionario.values()
print(valores)

```

¿Otra manera de convertir las llaves en tuplas?

```python

valores = tuple(diccionario.values())
print(valores)

elementos = diccionario.items()
print(elementos)

```

¿Podemos convertir los items de esa llave en una tupla de esta manera:
```python
elementos = tuple(diccionario.items())
print(elementos)


diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

```

¿Cómo podemos eliminar elementos de nuestro diccionario?

* 1 manera 

```python
del diccionario['a']
print(diccionario)
```

*  2 manera 

```python
valor = diccionario.pop('b')
print(valor)

print(diccionario)
```

* 3 manera  / elimina todo los elementos del diccionario
```python
diccionario.clear()
print(diccionario)

```
# Listas 

```python
lista_cursos = ['Python','Django', 'Flask','Ruby','Java']
```

En las listas el indice comienza con 0

```python
primer_curso = lista_cursos[0]
print(primer_curso)

primer_curso = lista_cursos[-5]
print(primer_curso)
```

Actualizar elementos de una lista
```python
lista_cursos[4] = 'Rust'

ultimo_curso = lista_cursos[4]
print(ultimo_curso)


```

* [start : end]
* [start : ] --> Obtenemos los últimos elementos de la lista.
* [: end] --> obtenemos los primeros elementos de la lista.
* [start : end : skip] con el tercer elemento generamos saltos dentro de la lista seleccionada.


```python
sub_lista = lista_cursos[0:3]
print(sub_lista)
```

Agregando Cursos 
```python
cursos_adicionales = ['PHP','MYSQL','C++']
cursos = ['Python','Django', 'Flask','Ruby','Java']
cursos.append('MongoDB')
```

cursos = ['Python','Django', 'Flask','Ruby','Java','MongoDB']


Agregar una lista con un indice especifico, se envia dos valores,
primero la posición y la segunda el dato
```python
cursos.insert(1, 'Rails')
```

#### ¿Cómo agregamos una lista en otra lista?
```python
cursos.extend(cursos_adicionales)
```

#### ¿Cómo eliminamos un dato de una lista?
```python
cursos.remove('MongoDB')
```

#### ¿Cómo eliminamos un dato usando el indice?
```python
del cursos[0]
```

#### ¿Cómo eliminamos todos los datos de una lista?
```python
cursos.clear()
```


#### ¿Cómo ordenamos una lista de manera ascendente?
```python
numeros = [8,11,1,400,500,358,6,505]
numeros.sort()
```

#### ¿Cómo ordenamos una lista de manera descendente?
```python
numeros.sort(reverse=True)
```

#### ¿Cómo sabemos cual es el número mayor y el número menor de la lista?
```python
numeros.sort()
print(numeros[0]) #min
print(numeros[-1]) #max
```

#### Usando funciones para saber cual es el número mayor y menor número de la lista
```python
print(min(numeros))
print(max(numeros))
```

#### ¿Cómo sabemos si un elemento esta dentro de la lista?
```python
print(10 in numeros)
```

#### ¿Cómo hacemos para confirmar que un número no este dentro d ela lista?
```python
print(11 not in numeros)
```

#### ¿Cómo saber en que indice se encuentra un elemento de la lista?
```python
elemento = numeros.index(5)
print(elemento)
```

#### ¿Cómo trabajar matrices usando listas?
```python
columna_a = [10,20]
columna_b = [30,40]
```

#### ¿Cómo crear una matriz bidimensional?

```python
matriz = [columna_a, columna_b] # 2 x 2 
print(matriz)
```

#### ¿Cómo obtener la posición de una matriz?
```python
print(matriz[0][0])
```
# Strings 

Dividir los strings 

```python
lenguajes = 'Python Ruby Java Rust  C++ C'

listado_lenguajes = lenguajes.split() # el split divide tomando espacios
print(listado_lenguajes)
```


Dividir los strings en base a un carácter - 

```python
lenguajes = 'Python-Ruby-Java-Rust-C++-C'

listado_lenguajes = lenguajes.split('-') # el split divide tomando base  - 
print(listado_lenguajes)
```

Dividir los strings en base a un caracter pero solo con una cantidad
```python
lenguajes = 'Python-Ruby-Java-Rust-C++-C'

listado_lenguajes = lenguajes.split('-', 2) # el split divide tomando base  - , y una cantidad solicitada
print(listado_lenguajes)
```

### String usando Joins
```python
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']

string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)
print(type(string_lenguajes))


string_lenguajes = '-'.join(lenguajes)
print(string_lenguajes)
```

### String Concatenando

```python
nombre = 'Gerardo Lastname'
apellido = 'Garcia'


nombre_completo = 'Mr.' + nombre + ' ' + apellido + '.'
print(nombre_completo)


nombre_completo_dos = 'Mr. %s %s %s.' %(nombre, apellido, 'Pérez')
print(nombre_completo_dos)
```

### String Concatenando Format

```python
nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Pérez')
print(nombre_completo)


nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
        nombre = nombre, 
        primer_apellido = apellido, 
        segundo_apellido = 'Pérez')

print(nombre_completo)
```

### Buscar String dentro de otro String 

```python
titulo_curso = 'Curso profesional de Python'

contador = titulo_curso.count('Python')
print(contador)
```


El método **Count** nos permite realizar una búsqueda de ciertas palabras

* Usando la palabra reserva IN

```python
print('Python' in titulo_curso)
```

* Buscar palabras en minusculas

```python
print('python' in titulo_curso.lower())
print('matematicas' not in titulo_curso.lower())
```

* Buscar si un String comienza con otro String 

```python
print(titulo_curso.startswith('Curso'))
```

* Buscar finaliza con otro string 

```python
print(titulo_curso.endswith('Python'))
```



###  Usando la funcion Print 

```python
print(nombre, apellido, 'Pérez')
print(nombre, apellido, 'Pérez', (12, 34, 55), sep='%') #con la variable sep, definimos como queremos separar los strings 
```

### Usando FString interpolando

```python
nombre_completo = f'Mr. {nombre} {apellido} {"Pérez"} {10 * 20}'
print(nombre_completo)
```


### Justificar Texto 

```python
mensaje = 'Hola mundo!'
```

* ljust -> Justificar a la izquierda
```python
mensaje = mensaje.ljust(20)
print(mensaje, '.')
```

* rjust -> Justificar a la derecha 
```python
mensaje = mensaje.rjust(20)
print(mensaje)
```

* center -> centrar el texto
```python
mensaje = mensaje.center(20)
print(mensaje)
```

# Tuplas

La tuplas no se pueden modificar sus datos, ni agregar


```python
#Indices     0     1    2     3      4        5
tupla = ('String',10, 15.4, True, [1,2,3], (4,5,6))
print(tupla)
```

Las tuplas son más rapidas que las listas en caso que quieras
obtener alguno de sus elementos

```python
 #             0        1        2         3         4

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')


#         -5       -4        -3         -2            -1

primer_curso = cursos[0]
print(primer_curso)
```


#### ¿Cómo crear subtuplas?
```python
sub_tupla = cursos[0:3]
print(sub_tupla)

#('Python', 'Flask', 'Django')
```

#### ¿Cómo usar tuplas y listas?
```python
courses = ['Python', 'Django', 'Flask']

courses_tuples =  tuple(courses)
print(courses_tuples)
print(type(courses_tuples))
```
```python
nivel = ('Básico', 'Intermedio', 'Avanzado')

nivel_lista = list(nivel)
print(nivel_lista)
print(type(nivel_lista))
```

#### ¿Cómo desempaquetar?
```python
uno, dos, tres, cuatro = 1, 2, 3, 4
print(uno)
print(dos)
print(tres)
print(cuatro)

numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
```

#### ¿Cómo desempaquetar? Cuando no sabes la cantidad de números

```python
numeros = (1, 2, 3, 4, 5, 6, 7)
uno, dos, tres, cuatro, *resto_valores = numeros #El * denota listas 
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)
```

#### ¿Cómo desempaquetar? cuando quieres omitir el resto de las variables
```python
numeros = (1, 2, 3, 4, 5, 6, 7)
uno, dos, tres, cuatro, *_ = numeros #El * denota listas, _ sirve para omitir valor
print(uno)
print(dos)
print(tres)
print(cuatro)
```

#### ¿Cómo desempaquetar? Cuando quieres omitir las variables pero quieres traer las ultimas para imprimir
```python
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = numeros #El * denota listas, _ sirve para omitir valor
print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)
```

#### ¿Cómo generar elementos para generar tuplas?
```python
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) #retornar un tipo de objeto zip
resultado = tuple(resultado)

print(resultado)
```