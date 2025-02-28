import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk
from modules import prediction ,eda,alerts ,optimization # Asegúrate de que este módulo esté configurado correctamente
import pandas as pd
from PIL import Image, ImageTk
import os
import time # Importar el módulo time
import psutil  # Para monitorear recursos del sistema

# Paleta de colores Minimalista y Elegante
COLORS = {
    "background": "#F5F5F5",  # Blanco Grisáceo
    "button": "#007BFF",  # Azul Brillante
    "button_text": "#FFFFFF",  # Blanco
    "header": "#4CAF50",  # Verde Claro
    "footer": "#FFC107",  # Amarillo
    "text": "#333333"  # Negro Suave
}

# Función para ejecutar Exploración de Datos
def run_eda():
    start_time = time.time()  # Iniciar el temporizador
    eda.run_exploration()
    elapsed_time = time.time() - start_time  # Calcular tiempo transcurrido

    try:
        global_stats = pd.read_csv('outputs/visualizations/global_statistics.csv')
        show_table(
            global_stats,
            "Estadísticas Globales",
            f"Este cuadro muestra estadísticas generales de las ventas, incluyendo totales, promedios y otros cálculos globales.\nTiempo de ejecución: {elapsed_time:.2f} segundos."
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'global_statistics.csv'.")

    try:
        grouped_stats = pd.read_csv('outputs/visualizations/grouped_statistics.csv')
        show_table(
            grouped_stats,
            "Estadísticas Agrupadas por Línea de Producto",
            f"Incluye estadísticas detalladas de ventas, agrupadas por línea de productos.\nTiempo de ejecución: {elapsed_time:.2f} segundos."
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'grouped_statistics.csv'.")

    try:
        show_graph(
            "outputs/visualizations/sales_by_category.png",
            "Gráfico de Ventas por Categoría",
            f"Representación gráfica de las ventas totales por categoría de producto.\nTiempo de ejecución: {elapsed_time:.2f} segundos."
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'sales_by_category.png'.")


# Función para mostrar un gráfico en una ventana emergente
def show_graph(image_path, title, footer_text=None):
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"No se encontró la imagen {image_path}")
        return

    # Crear una nueva ventana emergente
    top = Toplevel()
    top.title(title)
    top.geometry("800x600")

    try:
        # Cargar la imagen
        img = Image.open(image_path)
        img.thumbnail((700, 500))  # Ajustar el tamaño de la imagen para que encaje
        photo = ImageTk.PhotoImage(img)

        # Mostrar la imagen
        img_label = tk.Label(top, image=photo)
        img_label.image = photo  # Mantener referencia para evitar que sea recolectada por la basura
        img_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {str(e)}")

    # Pie de página con texto explicativo
    if footer_text:
        tk.Label(top, text=footer_text, font=("Arial", 10, "italic"), fg="gray").pack(pady=10)

    # Botón para cerrar la ventana
    tk.Button(top, text="Cerrar", font=("Arial", 12), command=top.destroy).pack(pady=10)


# Función para mostrar tablas en ventanas emergentes
def show_table(data, title, footer_text=None):
    top = Toplevel()
    top.title(title)
    top.geometry("800x500")

    # Título de la ventana emergente
    tk.Label(top, text=title, font=("Arial", 14, "bold")).pack(pady=10)

    # Marco para la tabla
    table_frame = tk.Frame(top)
    table_frame.pack(fill="both", expand=True)

    # Configurar la tabla
    tree = ttk.Treeview(table_frame, columns=list(data.columns), show="headings")
    tree.pack(fill="both", expand=True)

    # Configurar las cabeceras de las columnas
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Insertar los datos en la tabla
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

    # Pie de página con texto explicativo
    if footer_text:
        tk.Label(top, text=footer_text, font=("Arial", 10, "italic"), fg="gray").pack(pady=10)

    # Botón para cerrar la ventana emergente
    tk.Button(top, text="Cerrar", font=("Arial", 12), command=top.destroy).pack(pady=10)


# Función para ejecutar Optimización de Inventarios
def run_optimization():
    start_time = time.time()  # Iniciar el temporizador
    optimization.run_optimization()
    elapsed_time = time.time() - start_time  # Calcular tiempo transcurrido

    try:
        optimized_data = pd.read_csv('outputs/optimized_inventory.csv')
        # Mostrar la tabla con el tiempo de ejecución en el pie de página
        show_table(
            optimized_data,
            "Optimización de Inventarios",
            f"Muestra el inventario óptimo calculado con base en las ventas históricas y un margen de seguridad.\nTiempo de ejecución: {elapsed_time:.2f} segundos."
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'optimized_inventory.csv'.")


# Función para ejecutar Generación de Alertas
def run_alerts():
    start_time = time.time()  # Iniciar el temporizador
    alerts.generate_alerts()
    elapsed_time = time.time() - start_time  # Calcular tiempo transcurrido

    try:
        alerts_data = pd.read_csv('outputs/alerts.csv')
        # Mostrar la tabla con el tiempo de ejecución en el pie de página
        show_table(
            alerts_data,
            "Alertas Generadas",
            f"Lista de productos con inventario bajo y el valor asociado de dicho inventario.\nTiempo de ejecución: {elapsed_time:.2f} segundos."
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró 'alerts.csv'.")

# Función para ejecutar predicción y mostrar resultados en una ventana emergente con búsqueda
def run_prediction():
    # Iniciar el temporizador y obtener el estado inicial de los recursos
    start_time = time.time()
    memory_before = psutil.virtual_memory().used / (1024 ** 2)  # Memoria usada en MB
    disk_before = psutil.disk_usage('/').used / (1024 ** 3)  # Disco usado en GB
    cpu_before = psutil.cpu_percent(interval=None)  # Uso de CPU en %

    # Ejecutar el módulo de predicción
    prediction.run_prediction()

    # Calcular tiempo transcurrido después de completar la predicción
    elapsed_time = time.time() - start_time

    # Obtener el estado final de los recursos
    memory_after = psutil.virtual_memory().used / (1024 ** 2)  # Memoria usada en MB
    disk_after = psutil.disk_usage('/').used / (1024 ** 3)  # Disco usado en GB
    cpu_after = psutil.cpu_percent(interval=None)  # Uso de CPU en %

    # Calcular la diferencia en recursos usados
    memory_used = memory_after - memory_before
    disk_used = disk_after - disk_before
    cpu_change = cpu_after - cpu_before

    # Leer los resultados generados
    try:
        results = pd.read_csv('outputs/predictions.csv')  # Archivo generado por prediction.py
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontraron resultados de predicción.")
        return

    # Crear una nueva ventana emergente
    top = Toplevel()
    top.title("Resultados de Predicción")
    top.geometry("800x600")  # Ajustar altura para incluir el pie de página

    # Título de la ventana emergente
    tk.Label(top, text="Resultados de Predicción: Top Productos Demandados", font=("Arial", 14, "bold")).pack(pady=10)

    # Marco para la búsqueda
    search_frame = tk.Frame(top)
    search_frame.pack(pady=5)

    tk.Label(search_frame, text="Buscar Producto:", font=("Arial", 12)).pack(side="left", padx=5)

    search_entry = tk.Entry(search_frame, font=("Arial", 12), width=30)
    search_entry.pack(side="left", padx=5)

    # Marco para la tabla
    table_frame = tk.Frame(top)
    table_frame.pack(fill="both", expand=True)

    # Configurar la tabla
    tree = ttk.Treeview(table_frame, columns=list(results.columns), show="headings")
    tree.pack(fill="both", expand=True)

    # Configurar las cabeceras de las columnas
    for col in results.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Función para cargar datos en la tabla
    def load_table(data):
        # Limpiar la tabla
        for row in tree.get_children():
            tree.delete(row)
        # Insertar los datos
        for _, row in data.iterrows():
            tree.insert("", "end", values=list(row))

    # Cargar los datos iniciales
    load_table(results)

    # Función para filtrar la tabla
    def search_product():
        query = search_entry.get().strip().lower()
        if query:
            # Filtrar en base a "Product line"
            filtered_results = results[results['Product line'].str.lower().str.contains(query)]
        else:
            filtered_results = results
        load_table(filtered_results)

    # Vincular la entrada de texto con la búsqueda
    search_entry.bind("<KeyRelease>", lambda event: search_product())

    # Pie de página con texto explicativo y métricas de rendimiento
    footer_text = (
        f"Este cuadro muestra los productos más demandados con sus ventas actuales y predichas.\n"
        f"Use la barra de búsqueda para filtrar por nombre de producto.\n"
        f"Tiempo total de ejecución: {elapsed_time:.2f} segundos.\n"
        f"Memoria utilizada: {memory_used:.2f} MB.\n"
        f"Disco utilizado: {disk_used:.2f} GB.\n"
        f"Cambio en el uso de CPU: {cpu_change:.2f}%."
    )
    tk.Label(top, text=footer_text, font=("Arial", 10, "italic"), fg="gray").pack(pady=10)

    # Botón para cerrar la ventana emergente
    tk.Button(top, text="Cerrar", font=("Arial", 12), command=top.destroy).pack(pady=10)

# Ventana principal
root = tk.Tk()
root.configure(bg=COLORS["background"])
root.title("Sistema de Gestión de Inventarios")
root.geometry("500x400")

tk.Label(root, text="Sistema de Gestión de Inventarios", font=("Arial", 16), bg=COLORS["header"], fg=COLORS["button_text"]).pack(pady=10)

tk.Button(root, text="Exploración de Datos", font=("Arial", 12), bg=COLORS["button"], fg=COLORS["button_text"], command=run_eda).pack(pady=10)
tk.Button(root, text="Predicción de Demanda", font=("Arial", 12), bg=COLORS["button"], fg=COLORS["button_text"], command=run_prediction).pack(pady=10)
tk.Button(root, text="Optimización de Inventarios", font=("Arial", 12), bg=COLORS["button"], fg=COLORS["button_text"], command=run_optimization).pack(pady=10)
tk.Button(root, text="Generar Alertas", font=("Arial", 12), bg=COLORS["button"], fg=COLORS["button_text"], command=run_alerts).pack(pady=10)
tk.Button(root, text="Salir", font=("Arial", 12), bg=COLORS["button"], fg=COLORS["button_text"], command=root.quit).pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
