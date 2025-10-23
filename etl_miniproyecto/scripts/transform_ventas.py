import pandas as pd
from pathlib import Path


def limpiar_y_transformar(ruta_entrada, ruta_salida_limpia, ruta_salida_resumen):
    """
    Limpia y transforma un dataset de ventas.
    
    Parámetros:
    ruta_entrada (str | Path): Ruta del archivo CSV original
    ruta_salida_limpia (str | Path): Ruta para guardar los datos limpios
    ruta_salida_resumen (str | Path): Ruta para guardar el resumen de ventas
    """

    # === 1. EXTRACCIÓN ===
    print("📥 Leyendo archivo CSV...")
    df = pd.read_csv(ruta_entrada)

    # === 2. LIMPIEZA ===
    print("🧹 Limpiando datos...")

    # Rellenar valores faltantes
    df["Nombre"].fillna("Desconocido", inplace=True)
    df["Producto"].fillna("Sin especificar", inplace=True)
    df["Unidades"].fillna(df["Unidades"].mean(), inplace=True)

    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # Convertir fechas a tipo datetime
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")

    # Eliminar filas con fechas inválidas
    df.dropna(subset=["Fecha"], inplace=True)

    # === 3. TRANSFORMACIÓN ===
    print("🔧 Transformando datos...")

    # Crear columna total
    df["Total"] = df["Precio"] * df["Unidades"]

    # Extraer mes y año
    df["Mes"] = df["Fecha"].dt.month
    df["Año"] = df["Fecha"].dt.year

    # Agrupar ventas por persona
    resumen = (
        df.groupby("Nombre")["Total"]
        .sum()
        .reset_index()
        .sort_values(by="Total", ascending=False)
    )

    # === 4. CARGA (EXPORTACIÓN) ===
    print("💾 Guardando resultados...")

    df.to_csv(ruta_salida_limpia, index=False)
    resumen.to_csv(ruta_salida_resumen, index=False)

    print("✅ Transformación completada con éxito.")
    print(f"Datos limpios: {ruta_salida_limpia}")
    print(f"Resumen: {ruta_salida_resumen}")


if __name__ == "__main__":
    # Definir rutas
    base_dir = Path(__file__).resolve().parent.parent / "data"
    ruta_entrada = base_dir / "ventas.csv"
    ruta_salida_limpia = base_dir / "ventas_limpias.csv"
    ruta_salida_resumen = base_dir / "ventas_resumen.csv"

    # Ejecutar proceso
    limpiar_y_transformar(ruta_entrada, ruta_salida_limpia, ruta_salida_resumen)

