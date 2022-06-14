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