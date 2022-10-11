#Estructuras de datos

#list.append
'''Agrega un ítem al final de la lista.'''
#Ejemplo
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#list.extend

'''Extiende la lista agregándole todos los ítems del iterable.'''
#Ejemplo
car = ['Sonic', 'Am4', 'F-150']

cars = ['Ford', 'BMW', 'Volvo']
car.extend(cars)
print(car)

#list.insert

'''Inserta un ítem en una posición especificada. El primer argumento es el índice del ítem delante del cual se insertará.'''
#Ejemplo
fruits = ['apple', 'banana', 'cherry']
fruits.insert(2, "kiwi")
print(fruits)


#list.remove
'''Quita el primer ítem de la lista cuando el valor sea x. Lanza un ValueError si no existe el ítem.'''
#Ejemplo
list = ["pear", "kiwi", "cherry"]
list.remove("kiwi")
print(list)


#list.pop
'''Quita el ítem en la posición dada de la lista y lo retorna.'''
#Ejemplo
cars = ['BMW', 'FORD', 'CHEVROLET']
cars.pop(1)
print(cars)


#list.clear()
'''Elimina todos los elementos de la lista.'''
#Ejemplo
fruits = ["kiwi", "banana", "cherry"]
fruits.clear()
print(fruits)


#list.index
'''Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. '''
#Ejemlo
fruits = ['kiwi', 'orange', 'cherry']
x = fruits.index("cherry")
print(x)


#list.count(x)
'''Retorna el número de veces que x aparece en la lista.'''
#Ejemplo
fruits = ["apple", "banana", "cherry","kiwi","cherry","orange","cherry"]
x = fruits.count("cherry")
print(x)


#list.sort
'''Ordena los elementos de la lista .'''
#Ejemplo
cars = ['Ford', 'BMW', 'Volvo','Chevrolet','Renault']
cars.sort()
print(cars)


#list.reverse()
'''invierte los elementos de la lista.'''
#Ejemplo
list = ['1', '2', '3','4','5','6','7','8','9','10']
list.reverse()
print(list)


#list.copy()
'''Retorna una copia superficial de la lista.'''
#Ejemplo
fruits = ["apple", "kiwi", "orange"]
x = fruits.copy()
print(x)


#Usando listas como pilas
'''El último elemento agregado es el primero en retirarse, para agregar elementos utilizamos append(), para retirar un elemento utilizamos pop(). '''
number = [1,2,3]
number.append(4)
number.append(5)
print
number.pop()
number.pop()
number.pop()

print(number)


#Usando listas como colas
'''El primer elemento añadido es el primer elemento retirado,las listas no son eficientes, agregar y sacar del final de la lista es bastante rápido, pero insertar o sacar de la lista es lento.'''
from collections import deque
names = deque(["Eric","Andres","Alexs",])
names.append("Cesar")
names.append("Brayan")
names.popleft()
names.popleft()
print(deque)


#Compresión de lista
'''Podemos crear listas concisas, su uso es para hacer nuevas listas, cada elemento es el resultado de operaciones aplicadas, o para crear un segmento de un segmento '''

#Ejemplo
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Lisras por comprension anidadas
'''Comprension de listas que puede ser cualquier expresion incluyendo otra comprension de listas.'''

#Ejemplo

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print(matrix)

#La instruccion

''' Quitar un ítem de una lista dado su índice en lugar de su valor, la instrucción del. Esta es diferente del método pop(), el cual retorna un valor. La instrucción del también puede usarse para quitar secciones de una lista o vaciar la lista completa'''
#Ejemplo
x = ["apple", "banana", "cherry"]

del x[0]

print(x)
 
'''del tambien puede eliminar variables.'''

#Tuplas y secuencias
'''La construcción de tuplas que contengan 0 o 1 ítem, Las tuplas vacías se construyen mediante un par de paréntesis vacío,na tupla con un ítem se construye poniendo una coma a continuación del valor'''
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
0
len(singleton)
1
singleton
('hello',)
print(singleton)

#Conjuntos
'''Colección no ordenada y sin elementos repetidos, su uso es la verificación de pertenencia y eliminación de entradas duplicadas.'''
#Ejemplo
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#Diccionarios
'''Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.Un diccionario es una colección ordenada*, modificable y que no admite duplicados.'''
#Ejemplo
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Tecnicas de iteracion
'''Cuando iteramos sobre los diccionarios, se pueden obtener al mismo tiempo la clave y su valor correspondiente usando el método items().'''

#Ejemplo
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k,v)

#Mas acerca de condiciones
'''Las condiciones usadas en las instrucciones while e if contienen cualquier operador, no sólo comparaciones.'''

#Ejemplo
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

#Comparando secuencias y otros tipos
'''Las secuencias pueden compararse con otros objetos del mismo tipo de secuencia.'''

