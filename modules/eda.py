import pandas as pd
import matplotlib.pyplot as plt

def run_exploration():
    # Cargar datos
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Visualizar ventas por categoría
    sales_by_category = data.groupby('Product line')['Total'].sum()
    fig, ax = plt.subplots(figsize=(8, 6))  # Definir tamaño de la figura
    sales_by_category.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Ventas por Categoría', fontsize=16)
    ax.set_xlabel('Categoría', fontsize=12)
    ax.set_ylabel('Ventas Totales', fontsize=12)

    # Ajustar los márgenes para evitar recortes
    plt.tight_layout()

    # Guardar la imagen
    plt.savefig('outputs/visualizations/sales_by_category.png')
    plt.close()

    # Estadísticas descriptivas globales
    global_stats = data.describe().round(2)  # Redondear a dos cifras
    global_stats.to_csv('outputs/visualizations/global_statistics.csv')
    print("Estadísticas globales guardadas en 'outputs/visualizations/global_statistics.csv'.")

    # Estadísticas agrupadas por Product line
    grouped_stats = data.groupby('Product line').agg({
        'Total': ['sum', 'mean', 'std', 'min', 'max'],
        'Quantity': ['sum', 'mean', 'std', 'min', 'max'],
        'Unit price': ['mean', 'std', 'min', 'max']
    }).round(2)  # Redondear a dos cifras
    grouped_stats.to_csv('outputs/visualizations/grouped_statistics.csv')
    print("Estadísticas agrupadas guardadas en 'outputs/visualizations/grouped_statistics.csv'.")

    print("Exploración de datos completada.")
