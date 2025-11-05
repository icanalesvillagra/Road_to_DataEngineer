# 📊 Caso práctico: análisis de ventas con NumPy y Pandas
# 🎯 Objetivo

# Generar datos numéricos simulados usando NumPy (ventas, precios, unidades, etc.)

# Realizar operaciones vectorizadas para obtener métricas y transformar datos.

# Integrar con Pandas para un análisis tabular.

# 🧱 1. Importar librerías

import numpy as np
import pandas as pd

# 📦 2. Generar datos simulados

# Semilla para reproducibilidad
np.random.seed(42)

# Generar datos simulados
n = 1000
ids = np.arange(1, n + 1)
precios = np.random.randint(10, 1000, size=n)      # precios entre 10 y 1000
unidades = np.random.randint(1, 10, size=n)         # unidades vendidas entre 1 y 9
descuentos = np.random.uniform(0, 0.3, size=n)      # descuento entre 0% y 30%
dias = np.random.randint(1, 31, size=n)             # día del mes

# 🔢 3. Calcular métricas vectorizadas con NumPy

# Calcular total bruto (precio × unidades)
total_bruto = precios * unidades

# Aplicar descuento
total_neto = total_bruto * (1 - descuentos)

# Calcular promedio de ventas
promedio = np.mean(total_neto)
print(f"Promedio total de venta: ${promedio:,.2f}")

# 📊 4. Crear un DataFrame con Pandas

df = pd.DataFrame({
    "ID_Venta": ids,
    "Precio": precios,
    "Unidades": unidades,
    "Descuento": descuentos,
    "Total_Bruto": total_bruto,
    "Total_Neto": total_neto,
    "Día": dias
})

print(df.head())

# 🧹 5. Limpieza y transformación

# Clasificar ventas según su monto neto
df["Categoría_Venta"] = np.where(df["Total_Neto"] > 3000, "Alta", "Baja")

# Redondear valores monetarios
df[["Total_Bruto", "Total_Neto"]] = df[["Total_Bruto", "Total_Neto"]].round(2)

# 📈 6. Análisis estadístico

# Resumen general
print(df.describe())

# Promedio de ventas por categoría
promedio_categoria = df.groupby("Categoría_Venta")["Total_Neto"].mean()
print(promedio_categoria)

# 💾 7. Exportar resultados

df.to_csv("ventas_numpy.csv", index=False)