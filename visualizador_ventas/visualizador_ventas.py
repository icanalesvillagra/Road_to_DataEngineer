import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ventas_numpy.csv")

# 🎨 3. Configurar estilo visual

sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (8, 5)

# 📈 4. Histograma de precios

plt.hist(df["Precio"], bins=30, edgecolor="black")
plt.title("Distribución de precios")
plt.xlabel("Precio ($)")
plt.ylabel("Frecuencia")
plt.show()

# 📊 5. Gráfico de dispersión (Precio vs Total Neto)

plt.scatter(df["Precio"], df["Total_Neto"], alpha=0.6)
plt.title("Relación entre precio y total neto")
plt.xlabel("Precio ($)")
plt.ylabel("Total Neto ($)")
plt.show()

# 📦 6. Boxplot por categoría de venta

sns.boxplot(data=df, x="Categoría_Venta", y="Total_Neto")
plt.title("Distribución de ventas netas por categoría")
plt.show()

# 📊 7. Promedio de ventas por día (usando groupby)

ventas_por_dia = df.groupby("Día")["Total_Neto"].mean().reset_index()

sns.lineplot(data=ventas_por_dia, x="Día", y="Total_Neto", marker="o")
plt.title("Promedio diario de ventas netas")
plt.xlabel("Día del mes")
plt.ylabel("Promedio ($)")
plt.show()

# 📈 8. Comparativa entre unidades y descuento

sns.scatterplot(data=df, x="Unidades", y="Descuento", hue="Categoría_Venta")
plt.title("Relación entre unidades vendidas y descuento aplicado")
plt.show()

# 📉 9. Matriz de correlación

corr = df[["Precio", "Unidades", "Descuento", "Total_Neto"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlación")
plt.show()
