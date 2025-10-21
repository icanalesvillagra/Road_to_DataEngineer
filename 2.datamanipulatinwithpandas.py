# 🧠 ¿Qué es Pandas?

# Pandas es una librería de Python para análisis y manipulación de datos estructurados 
# (tablas, hojas de cálculo, CSV, bases de datos, etc.).
# Se construye sobre NumPy y ofrece estructuras eficientes para manejar datos tabulares:

# Series: columna unidimensional (como una lista con etiquetas).

# DataFrame: tabla de datos bidimensional (como una hoja de Excel).

print("\n📊 1. Manipulación tabular básica\n")
print("\n📥 Crear un DataFrame\n")

import pandas as pd

# Crear un DataFrame desde un diccionario
data = {
    "Nombre": ["Ignacio", "Ana", "Pedro"],
    "Edad": [28, 25, 31],
    "Ciudad": ["Santiago", "Valparaíso", "Concepción"]
}

df = pd.DataFrame(data)
print(df)

print("\n🔎 Acceder a filas y columnas\n")

# Acceder a una columna
print(df["Nombre"])

# Acceder a varias columnas
print(df[["Nombre", "Ciudad"]])

# Acceder a una fila por índice
print(df.loc[1])    # usando etiqueta (índice)
print(df.iloc[0])   # usando posición

print("\n➕ Agregar o eliminar columnas\n")

df["País"] = "Chile"        # Nueva columna
df.drop("Ciudad", axis=1, inplace=True)  # Eliminar columna
print(df)

print("\n🔄 Filtrar filas\n")

# Filtrar por condición
mayores = df[df["Edad"] > 26]
print(mayores)

print("\n📈 Ordenar datos\n")

df_ordenado = df.sort_values(by="Edad", ascending=False)
print(df_ordenado)

# 🧹 2. Limpieza de datos

# En ingeniería de datos, esto es crucial.
# Pandas tiene muchas funciones para detectar,
# reemplazar y eliminar datos erróneos o faltantes.

import pandas as pd

print("\n❓ Detectar valores nulos\n")

df = pd.DataFrame({
    "Nombre": ["Ignacio", "Ana", None],
    "Edad": [28, None, 31]
})

print(df.isnull())     # Muestra True donde hay valores nulos
print(df.isnull().sum())  # Cuenta los nulos por columna

print("\n🧽 Eliminar o rellenar valores nulos\n")

df_sin_nulos = df.dropna()                # Elimina filas con NaN
df_relleno = df.fillna({"Edad": 0})       # Reemplaza nulos por 0
df["Nombre"].fillna("Desconocido", inplace=True)

print(df)

print("\n🔄 Reemplazar valores específicos\n")

df["Nombre"].replace("Ana", "Andrea", inplace=True)

print(df)

print("\n✂️ Eliminar duplicados\n")

df.drop_duplicates(inplace=True)

print("\n🧹 Renombrar columnas\n")

df.rename(columns={"Nombre": "Persona", "Edad": "Años"}, inplace=True)

print("\n🔧 3. Transformación de datos\n")
# Esto se refiere a modificar, agrupar o combinar 
# datos para prepararlos para análisis o carga en un Data Warehouse.

print("\n📏 Crear columnas calculadas\n")

# df["Edad_duplicada"] = df["Edad"] * 2

print("\n📊 Agrupar datos (groupby)\n")

ventas = pd.DataFrame({
    "Vendedor": ["Ignacio", "Ana", "Ana", "Pedro"],
    "Monto": [200, 150, 100, 300]
})

agrupado = ventas.groupby("Vendedor")["Monto"].sum()
print(agrupado)

print("\n🔗 Unir o combinar DataFrames (merge, concat)\n")

df1 = pd.DataFrame({"ID": [1, 2, 3], "Nombre": ["Ignacio", "Ana", "Pedro"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "Ciudad": ["Santiago", "Valpo", "Conce"]})

df_combinado = pd.merge(df1, df2, on="ID")
print(df_combinado)

print("\n🔄 Concatenar DataFrames (uno debajo de otro)\n")

df_concat = pd.DataFrame({"Nombre": ["Lucía"], "Años": [29], "Ciudad": ["La Serena"]})
df_total = pd.concat([df_combinado, df_concat], ignore_index=True)
print(df_total)

print("\n🧮 Aplicar funciones a columnas (apply)\n")

df["Años_categoria"] = df["Años"].apply(lambda x: "Joven" if x < 30 else "Adulto")
print(df)

print("\n🧠 Resumen visual\n")

print("| Categoría           | Función principal            | Ejemplo                     |")
print("| ------------------- | ---------------------------- | --------------------------- |")
print("| Lectura / Escritura | .pd.read_csv(), .to_csv()    | Leer o guardar archivos CSV |")
print("| Limpieza            | .dropna(),      .fillna()    | Manejo de nulos             |")
print("| Transformación      | .apply(),       .groupby()   | Crear columnas o agrupar    |")
print("| Combinación         | .merge(),       .concat()    | Unir DataFrames             |")
print("| Selección           | .loc[],         .iloc[]      | Filtrar datos               |")
