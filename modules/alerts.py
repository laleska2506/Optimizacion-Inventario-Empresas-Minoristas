import pandas as pd

# Umbral de inventario bajo
LOW_INVENTORY_THRESHOLD = 5

def generate_alerts():
    # Cargar datos
    data = pd.read_csv('data/augmented_supermarket_sales.csv')

    # Filtrar productos con inventario bajo
    low_inventory = data[data['Quantity'] < LOW_INVENTORY_THRESHOLD]

    # Calcular el valor total del inventario bajo
    low_inventory['Inventory Value'] = (low_inventory['Quantity'] * low_inventory['Unit price']).round(2)

    # Ordenar las alertas por el valor del inventario (descendente)
    low_inventory = low_inventory[['Product line', 'Quantity', 'Unit price', 'Inventory Value']]
    low_inventory['Unit price'] = low_inventory['Unit price'].round(2)  # Redondear precios
    low_inventory = low_inventory.sort_values(by='Inventory Value', ascending=False)

    # Guardar alertas
    low_inventory.to_csv('outputs/alerts.csv', index=False)
    print("Alertas generadas y guardadas en 'outputs/alerts.csv'.")
