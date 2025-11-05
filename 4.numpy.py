print("\n🔹 1. Importar y crear arreglos (arrays)\n")
import numpy as np

# Crear un arreglo (vector)
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Crear una matriz (2D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

print("\n🔹 2. Propiedades básicas de un array\n")
print(arr.shape)   # (5,) → dimensiones del array
print(matriz.shape) # (2, 3)
print(arr.dtype)   # tipo de dato (int64, float64, etc.)
print(arr.ndim)    # número de dimensiones

print("\n🔹 3. Crear arrays con funciones útiles")
array_zeros = np.zeros((3, 3))     # matriz 3x3 llena de ceros
array_ones = np.ones((2, 4))      # matriz 2x4 llena de unos
array_arange = np.arange(0, 10, 2)  # array de 0 a 8, de 2 en 2
array_linspace = np.linspace(0, 1, 5) # 5 valores entre 0 y 1
array_eye = np.eye(3)            # matriz identidad 3x3

print("\nMatriz 3x3 llena de ceros")
print(array_zeros)
print("\nMatriz 2x4 llena de unos")
print(array_ones)
print("\nArray de 0 a 8, de 2 en 2")
print(array_arange)
print("\n5 valores entre 0 y 1")
print(array_linspace)
print("\nMatriz identidad 3x3")
print(array_eye)

print("\n🔹 4. Operaciones vectorizadas (clave de NumPy)")
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("\nOperaciones elemento a elemento\n")
print("Suma")
print(a + b)   # [11 22 33 44]
print("Resta")
print(a - b)   # [ 9 18 27 36]
print("Multiplicación")
print(a * b)   # [10 40 90 160]
print("División")
print(a / b)   # [10. 10. 10. 10.]

print("\nOperaciones escalares")
print(a * 2)   # [20 40 60 80]

## 📈 Estas operaciones están vectorizadas, 
# lo que significa que NumPy las realiza en 
# paralelo internamente, sin necesidad de for.

print("\n🔹 5. Operaciones estadísticas y matemáticas")

data = np.array([10, 20, 30, 40, 50])

print("\nPromedio")
print(data.mean())   # promedio
print("\nPromedio")
print(data.sum())    # suma total
print("\nMínimo")
print(data.min())    # mínimo
print("\nMáximo")
print(data.max())    # máximo
print("\nDesviación estándar")
print(data.std())    # desviación estándar

print("\n🔹 6. Indexación y slicing (acceso a element os)")

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])     # primer elemento
print(arr[-1])    # último elemento
print(arr[1:4])   # subarray [20, 30, 40]

print("\n🔹 6. Indexación para Matrices")

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matriz[0, 0])    # elemento (fila 0, col 0)
print(matriz[:, 1])    # segunda columna
print(matriz[1, :])    # segunda fila
print(matriz[0:2, 1:3]) # submatriz

print("\n🔹 7. Operaciones entre matrices")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Suma y resta elemento a elemento
print(A + B)

# Multiplicación elemento a elemento
print(A * B)

# Producto matricial (algebra lineal)
print(np.dot(A, B))   # o A @ B

print("\n🔹 8. Funciones útiles de álgebra lineal")

from numpy.linalg import inv, det, eig

mat = np.array([[2, 1], [5, 3]])

print("\nDeterminante")
print(det(mat))       # determinante
print("\nMatriz inversa")
print(inv(mat))       # matriz inversa
valores, vectores = eig(mat)  # valores y vectores propios
print("\nValores")
print(valores)
print("\nVectores")
print(vectores)

print("\n🔹 9. Broadcasting (expansión automática de dimensiones)")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

# b se replica por cada fila de A
print(A + b)

print("\n🔹 10. Ejemplo práctico: normalización de datos")

datos = np.array([100, 200, 300, 400, 500])

print("\n Normalizar (0 a 1)")
norm = (datos - datos.min()) / (datos.max() - datos.min())
print(norm)

print("\n RESUMEN")

print("| Categoría                | Descripción                     | Ejemplo                       |")
print("| ------------------------ | ------------------------------- | ----------------------------- |")
print("| Creación                 | Arrays y matrices               | `np.array()`, `np.zeros()`    |")
print("| Indexación               | Acceso a elementos              | `arr[1:3]`, `matriz[:,0]`     |")
print("| Operaciones vectorizadas | Suma, multiplicación, etc.      | `a + b`, `a * 2`              |")
print("| Estadística              | Promedio, suma, desviación      | `.mean()`, `.std()`           |")
print("| Álgebra lineal           | Inversa, determinante, producto | `np.dot()`, `np.linalg.inv()` |")
