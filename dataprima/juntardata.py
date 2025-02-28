import pandas as pd
import random

# Cargar el dataset original
retail_sales = pd.read_csv('retail_sales_dataset.csv')  # Cambia a la ruta correcta del archivo
supermarket_sales = pd.read_csv('supermarket_sales.csv')  # Cambia a la ruta correcta del archivo

# Datos adicionales proporcionados
additional_data = [
    ["Electronic accessories", "226-31-3081", "C", "Naypyitaw", "Normal", "Female", 15.28, 5, 3.82, 80.22, "3/8/2019", "10:29", "Cash", 76.4, 4.761904762, 3.82, 9.6],
    ["Electronic accessories", "699-14-3026", "C", "Naypyitaw", "Normal", "Male", 85.39, 7, 29.8865, 627.6165, "3/25/2019", "18:30", "Ewallet", 597.73, 4.761904762, 29.8865, 4.1],
    ["Electronic accessories", "355-53-5943", "A", "Yangon", "Member", "Female", 68.84, 6, 20.652, 433.692, "2/25/2019", "14:36", "Ewallet", 413.04, 4.761904762, 20.652, 5.8],
    ["Electronic accessories", "529-56-3974", "B", "Mandalay", "Member", "Male", 25.51, 4, 5.102, 107.142, "3/9/2019", "17:03", "Cash", 102.04, 4.761904762, 5.102, 6.8],
    ["Electronic accessories", "365-64-0515", "A", "Yangon", "Normal", "Female", 46.95, 5, 11.7375, 246.4875, "2/12/2019", "10:25", "Ewallet", 234.75, 4.761904762, 11.7375, 7.1],
    ["Electronic accessories", "300-71-4605", "C", "Naypyitaw", "Member", "Male", 86.04, 5, 21.51, 451.71, "2/25/2019", "11:24", "Ewallet", 430.2, 4.761904762, 21.51, 4.8],
    ["Electronic accessories", "636-48-8204", "A", "Yangon", "Normal", "Male", 34.56, 5, 8.64, 181.44, "2/17/2019", "11:15", "Ewallet", 172.8, 4.761904762, 8.64, 9.9],
    ["Electronic accessories", "272-65-1806", "A", "Yangon", "Normal", "Female", 60.88, 9, 27.396, 575.316, "1/15/2019", "17:17", "Ewallet", 547.92, 4.761904762, 27.396, 4.7],
    ["Electronic accessories", "132-32-9879", "B", "Mandalay", "Member", "Female", 93.96, 4, 18.792, 394.632, "3/9/2019", "18:00", "Cash", 375.84, 4.761904762, 18.792, 9.5],
    ["Electronic accessories", "669-54-1719", "B", "Mandalay", "Member", "Male", 18.93, 6, 5.679, 119.259, "2/10/2019", "12:45", "Credit card", 113.58, 4.761904762, 5.679, 8.1],
]

# Convertir los datos adicionales en un DataFrame
additional_df = pd.DataFrame(additional_data, columns=[
    "Product line", "Invoice ID", "Branch", "City", "Customer type", "Gender", 
    "Unit price", "Quantity", "Tax 5%", "Total", "Date", "Time", "Payment", 
    "cogs", "gross margin percentage", "gross income", "Rating"
])

# Convertir fechas y asegurarse de que coincidan en formato
additional_df['Date'] = pd.to_datetime(additional_df['Date'])

# Agregar filas aleatoriamente al dataset original
merged_data = pd.concat([supermarket_sales, additional_df.sample(frac=1)], ignore_index=True)

# Guardar el dataset final
output_path = 'augmented_supermarket_sales.csv'
merged_data.to_csv(output_path, index=False)

print(f"Datos aumentados guardados en: {output_path}")
print(merged_data.tail())
