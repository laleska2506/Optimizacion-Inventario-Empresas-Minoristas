import pandas as pd

def create_data_copy(input_file, output_file, num_rows):
    try:
        # Cargar el archivo original
        data = pd.read_csv(input_file)

        # Verificar si el número de filas solicitado es válido
        if num_rows > len(data):
            print(f"El archivo original solo tiene {len(data)} filas. Se copiarán todas.")
            num_rows = len(data)

        # Seleccionar las filas solicitadas
        data_copy = data.iloc[:num_rows]

        # Guardar la copia en un nuevo archivo
        data_copy.to_csv(output_file, index=False)
        print(f"Copia creada con éxito en '{output_file}' con {num_rows} filas.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Parámetros de entrada
if __name__ == "__main__":
    input_file = "data/augmented_supermarket_sales.csv"  # Ruta del archivo original
    output_file = "data/sales_data_10000.csv"            # Ruta del archivo de salida
    num_rows = int(input("Ingrese la cantidad de filas que desea copiar: "))
    create_data_copy(input_file, output_file, num_rows)
