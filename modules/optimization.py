import pandas as pd

# Margen de seguridad para optimización
SAFETY_BUFFER = 1.2

def run_optimization():
    # Cargar datos
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Calcular demanda histórica (promedio de ventas totales por línea de producto)
    demand = data.groupby('Product line')['Total'].mean()

    # Unir la demanda al dataset original
    data = data.merge(demand, on='Product line', suffixes=('', '_avg_demand'))

    # Calcular inventario óptimo
    data['Optimal Inventory'] = (data['Quantity'] * SAFETY_BUFFER).round()

    # Redondear la demanda promedio y los precios unitarios
    data['Total_avg_demand'] = data['Total_avg_demand'].round(2)
    data['Unit price'] = data['Unit price'].round(2)

    # Seleccionar columnas relevantes
    optimized_data = data[['Product line', 'Quantity', 'Unit price', 'Optimal Inventory', 'Total_avg_demand']]

    # Guardar datos optimizados
    optimized_data.to_csv('outputs/optimized_inventory.csv', index=False)
    print("Optimización completada y guardada en 'outputs/optimized_inventory.csv'.")
