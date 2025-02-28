import pandas as pd

def duplicate_csv(input_file, output_file, target_rows):
    try:
        # Cargar datos del archivo CSV original
        data = pd.read_csv(input_file)
        current_rows = len(data)

        if current_rows == 0:
            print("El archivo CSV original está vacío. No se pueden duplicar los datos.")
            return

        # Calcular cuántas veces duplicar los datos
        repeat_count = -(-target_rows // current_rows)  # Redondeo hacia arriba
        extended_data = pd.concat([data] * repeat_count, ignore_index=True)

        # Cortar el conjunto de datos al número exacto de filas deseadas
        extended_data = extended_data.iloc[:target_rows]

        # Guardar el nuevo archivo CSV
        extended_data.to_csv(output_file, index=False)
        print(f"Archivo generado: '{output_file}' con {target_rows} filas.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Parámetros para la generación de archivos
if __name__ == "__main__":
    input_file = "data/augmented_supermarket_sales.csv"  # Ruta del archivo original
    output_file_10k = "data/sales_10000.csv"             # Archivo para 10,000 filas
    output_file_20k = "data/sales_20000.csv"             # Archivo para 20,000 filas

    # Generar archivos con 10,000 y 20,000 filas
    duplicate_csv(input_file, output_file_10k, 10000)
    duplicate_csv(input_file, output_file_20k, 20000)
