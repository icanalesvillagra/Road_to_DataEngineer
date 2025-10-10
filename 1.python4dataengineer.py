# 🧠 PUNTO 1: PROGRAMACIÓN PARA DATA ENGINEERING

print("🐍 A. PYTHON PARA DATA ENGINEERS\n")

# 1. Fundamentos del lenguaje

# Tipos de datos (int, float, str, list, dict, tuple, set)

## int ##
edad = 25
    
print(edad)           # 25
print(type(edad))     # <class 'int'>

## float ##
altura = 1.75
print(altura)         # 1.75
print(type(altura))   # <class 'float'>

## str ##
nombre = "Ignacio"
print(nombre)         # Ignacio
print(type(nombre))   # <class 'str'>

## list ##
numeros = [10, 20, 30, 40]
print(numeros)        # [10, 20, 30, 40]
print(type(numeros))  # <class 'list'>

    # Ejemplo de acceso y modificación en una lista
numeros[2] = 99
print(numeros)        # [10, 20, 99, 40]

## dict ##
persona = {
    "nombre": "Ignacio",
    "edad": 28,
    "profesion": "Ingeniero"
}
print(persona["nombre"])  # Ignacio
print(type(persona))      # <class 'dict'>

## tupla ##
coordenadas = (10.5, 20.3)
print(coordenadas)      # (10.5, 20.3)
print(type(coordenadas))# <class 'tuple'>

## set ##
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)         # {'azul', 'verde', 'rojo'}
print(type(colores))   # <class 'set'>

print("\nControl de flujo: if, for, while\n")

## if ##
edad = 18

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años, justo la mayoría de edad")
else:
    print("Eres mayor de edad")
    
## for ##
#ejemplo 1#
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

#ejemplo 2#    
for i in range(5):
    print(i)

## while ##
contador = 0

while contador < 5:
    print(f"Contador vale: {contador}")
    contador += 1  # Incrementa el contador

## break & continue ##
for numero in range(1, 10):
    if numero == 5:
        break  # detiene el bucle
    if numero % 2 == 0:
        continue  # salta a la siguiente iteración si es par
    print(numero)

print("\nFunciones y argumentos (def, *args, **kwargs)\n")

## función sin parámetros ##
def saludar():
    print("Hola, bienvenido a Python!")

saludar()

## función con parámetros y valor de retorno ##
def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(5, 3))  # 8
# a y b son parámetros.
# return devuelve un resultado al programa.

## función con argumentos por defecto ##
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar("Ignacio")  # Hola, Ignacio!
saludar()           # Hola, Invitado!
# Si no se pasa un argumento, se usa el valor por defecto "Invitado"

## *args - argumentos variables (posicionales) ##
def sumar_todos(*args):
    total = sum(args)
    print(f"Suma total: {total}")

sumar_todos(3, 5, 10)
sumar_todos(1, 2, 3, 4, 5)
# *args permite pasar cualquier cantidad de argumentos posicionales.
# Dentro de la función, args se comporta como una tupla.

## *kwargs - argumentos variables (por nombres)
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ignacio", edad=28, profesion="Ingeniero")
# **kwargs permite recibir argumentos con nombre, sin importar cuántos sean.
# Dentro de la función, se comporta como un diccionario.

## combinando todo (args, kwargs y parámetros normales) ##
def mostrar_datos(ciudad, *args, **kwargs):
    print(f"Ciudad: {ciudad}")
    print("Datos adicionales (args):", args)
    print("Detalles nombrados (kwargs):", kwargs)

mostrar_datos("Santiago", "Chile", 2025, nombre="Ignacio", profesion="Ingeniero")
# ciudad es un argumento normal.
# *args captura argumentos adicionales sin nombre.
# **kwargs captura los argumentos nombrados.

print("\n## Funciones LAMBDA (anonimas) ##\n")

# Las funciones lambda son funciones pequeñas,
# sin nombre, que se usan cuando necesitas algo 
# rápido o dentro de otra función.

# Función normal
def cuadrado(x):
    return x ** 2

# Equivalente en lambda
cuadrado_lambda = lambda x: x ** 2

print(cuadrado(5))         # 25
print(cuadrado_lambda(5))  # 25

#lambda x: x ** 2 crea una función que recibe un argumento x y devuelve x ** 2.
#Se usa mucho con funciones como map(), filter() o sorted().

## ejemplo práctico con lambda y map() ##
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda n: n ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

## funciones anidadas ##
def operacion(a, b):
    def sumar(x, y):
        return x + y
    def multiplicar(x, y):
        return x * y
    
    suma = sumar(a, b)
    producto = multiplicar(a, b)
    
    return suma, producto

resultado = operacion(3, 5)
print(resultado)  # (8, 15)

## funciones con multiples valores de retorno ##
def calcular(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

resultado = calcular(10, 4)
print(resultado)           # (14, 6, 40)

# También puedes desempaquetar los valores:
suma, resta, producto = calcular(10, 4)
print(suma, resta, producto)  # 14 6 40

## combinación de lambda y retorno multiple ##
def operaciones(a, b):
    suma = lambda x, y: x + y
    mult = lambda x, y: x * y
    return suma(a, b), mult(a, b)

print(operaciones(3, 7))  # (10, 21)

print("\nManejo de errores y excepciones (try-except)\n")

## Manejo de Excepciones con try y except ##
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

## multiples excepciones ##
try:
    valor = int("abc")
    resultado = 10 / valor
except ValueError:
    print("Error: el valor no es un número válido.")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

## capturar cualquier error genérico ##
try:
    x = 10 / 0
except Exception as e:
    print(f"Ocurrió un error: {e}")

print("\nLectura/escritura de archivos (open, .read(), .write())\n")

## crear y escribir en un archivo (write) ##
# Abrir (o crear) un archivo en modo escritura
archivo = open("ejemplo.txt", "w")

# Escribir texto
archivo.write("Hola, este es un archivo de prueba.\n")
archivo.write("Segunda línea de texto.")

# Cerrar el archivo
archivo.close()
# "w" = modo escritura (si el archivo no existe, lo crea; si existe, lo sobrescribe).
# Es importante cerrar el archivo con .close() después de escribir.

## leer todo el contenido (read) ##
archivo = open("ejemplo.txt", "r")  # modo lectura
contenido = archivo.read()
print(contenido)
archivo.close()
# "r" = modo lectura (el archivo debe existir).
# .read() lee todo el contenido como una cadena.

## leer línea por línea (redline y readlines) ##
archivo = open("ejemplo.txt", "r")

# Leer una línea
linea1 = archivo.readline()
print("Primera línea:", linea1)

# Leer todas las líneas restantes como lista
resto = archivo.readlines()
print("Resto:", resto)

archivo.close()
# .readline() → lee solo una línea.
# .readlines() → devuelve una lista donde cada elemento es una línea del archivo.

## agregar contenido a un archivo (append) ##
archivo = open("ejemplo.txt", "a")  # modo append
archivo.write("\nNueva línea añadida al final.")
archivo.close()
# "a" = modo append, agrega texto al final sin borrar el contenido previo.

## comprobación de archivo con linea agregada ##
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
# No necesitas llamar a .close().
# El archivo se cierra automáticamente al salir del bloque with.
# Es la forma más segura y moderna de trabajar con archivos.   

print("\n Ejemplo completo - Escribir y luego Leer \n")

# Escribir
with open("datos.txt", "w") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")

# Leer
with open("datos.txt", "r") as f:
    for linea in f:
        print(linea.strip())  # .strip() quita saltos de línea

print("\n Escribir una lista o diccionario \n")

# Escribir una lista línea por línea
nombres = ["Ana", "Ignacio", "Pedro"]

with open("nombres.txt", "w") as f:
    for nombre in nombres:
        f.write(nombre + "\n")

# Leer el archivo
with open("nombres.txt", "r") as f:
    print(f.read())