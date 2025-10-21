import pandas as pd

#leer archivo csv
df = pd.read_csv("C:\Users\ticpa\Desktop\Workspace\DATA_ENGINEERING\ventas.csv")

#mostrar primera filas
print(df.head()) # head.() muestra las primeras 5 filas con todas las columnas
print(df) # muestra el archivo completo

# ---------------------------------------------------- #

#limpieza de datos
print(df.isnull().sum())

# ---------------------------------------------------- #

#rellenar o eliminar valores nulos 

# Rellenar 'Nombre' faltante con "Desconocido"
df["Nombre"].fillna("Desconocido", inplace=True)

# Rellenar 'Producto' faltante con "Sin especificar"
df["Producto"].fillna("Sin especificar", inplace=True)

# Rellenar 'Unidades' faltantes con el promedio de la columna
df["Unidades"].fillna(df["Unidades"].mean(), inplace=True)

# fillna() es un método en la biblioteca Pandas de Python 
# que se utiliza para reemplazar valores faltantes (NaN o None) 
# en un DataFrame o Serie con un valor especificado.

print(df)

# eliminar duplicados
df.drop_duplicates(inplace=True)
print(df)

# asegurarse que Fecha está en datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])
print(df)

# convertir columna de fecha a formato d, m, y
df["Fecha"] = df["Fecha"].dt.strftime('%d/%m/%Y')
print(df)

print("\n🔧 3. Transformación de datos\n")

# crear columna calculada: Total por venta
df["Total"] = df["Precio"] * df["Unidades"]
print(df)

# Crear columna de mes y año (útil para análisis) PENDIENTE

df["Mes"] = df["Fecha"].dt.month
df["Año"] = df["Fecha"].dt.year

# Agrupar datos (por vendedor o producto)
ventas_por_persona = df.groupby("Nombre")["Total"].sum().reset_index()
print(ventas_por_persona)

# Ordenar y filtrar resultados

# Ordenar por total de ventas descendente, para cambiar el orden a ascendente, cambiar el valor de ascending a True
ventas_ordenadas = ventas_por_persona.sort_values(by="Total", ascending=False)
print(ventas_ordenadas)

# Exportar los resultados limpios, utilizando la ultima versión del dataset mencionado
df.to_csv("ventas_limpias.csv", index=False) #dataset limpio y transformado
ventas_ordenadas.to_csv("ventas_resumen.csv", index=False) #resumen de ventas totales por persona

print("\nResumen de operaciones realizadas\n")

print("| Etapa          | Operación                           | Función usada                                      |")
print("| -------------- | ----------------------------------- | -------------------------------------------------- |")
print("| Extracción     | Lectura del CSV                     | `pd.read_csv()`                                    |")
print("| Limpieza       | Nulos, duplicados, formato de fecha | `.fillna()`, `.drop_duplicates()`, `to_datetime()` |")
print("| Transformación | Columnas nuevas, agrupación         | `.groupby()`, `.apply()`, cálculo de totales       |")
print("| Carga          | Exportar resultados                 | `.to_csv()`                                        |")
