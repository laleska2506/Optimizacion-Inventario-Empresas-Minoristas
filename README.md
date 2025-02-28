<h1>Sistema de Gestión de Inventarios para Empresas Minoristas</h1>

Este proyecto consiste en un Sistema de Gestión de Inventarios diseñado para empresas o usuarios que necesitan optimizar el manejo de sus productos, predecir tendencias de demanda, y generar alertas en tiempo real para prevenir escasez de inventarios. El sistema proporciona una interfaz gráfica interactiva y amigable desarrollada en Python utilizando la biblioteca Tkinter, permitiendo a los usuarios visualizar y gestionar datos de manera eficiente.
Funcionalidades Principales:

    Exploración de Datos:
        Analiza y presenta estadísticas descriptivas de los datos de inventarios.
        Genera visualizaciones gráficas de las ventas por categorías de productos.
        Proporciona información detallada de los datos globales y agrupados por línea de productos.

    Predicción de Demanda:
        Utiliza modelos de Machine Learning con TensorFlow para predecir la demanda futura de productos.
        Presenta los resultados en una tabla interactiva con columnas como:
            Actual (Real): Ventas reales del producto.
            Predicted (Predicción): Ventas estimadas por el modelo.
        Incluye una barra de búsqueda para filtrar productos específicos.

    Optimización de Inventarios:
        Calcula niveles óptimos de inventarios considerando las tendencias de ventas históricas.
        Proporciona datos detallados sobre el stock ideal para minimizar costos y evitar rupturas de inventarios.

    Generación de Alertas:
        Identifica productos con inventario bajo y genera alertas automáticas.
        Muestra productos críticos junto con recomendaciones para reabastecimiento.

Tecnologías y Herramientas Utilizadas:

    Lenguaje de Programación: Python.
    Frameworks y Librerías:
        Tkinter: Para la creación de la interfaz gráfica.
        TensorFlow: Para construir y entrenar modelos de predicción de demanda.
        Pandas: Para la manipulación y análisis de datos.
        Matplotlib: Para generar gráficos y visualizaciones.
        Psutil: Para monitorear el uso de recursos como memoria, CPU y disco durante la ejecución.

Diseño Visual:

    La interfaz utiliza un esquema de colores minimalista y elegante para mejorar la experiencia del usuario:
        Fondo: #F5F5F5 (Blanco Grisáceo).
        Texto Principal: #333333 (Negro Suave).
        Botones: #007BFF (Azul Brillante).
        Texto de Botones: #FFFFFF (Blanco).
        Encabezados: #4CAF50 (Verde Claro).
        Detalles/Resaltados: #FFC107 (Amarillo).

Objetivo del Proyecto:

El sistema busca simplificar y automatizar tareas críticas relacionadas con la gestión de inventarios, mejorar la toma de decisiones mediante el análisis de datos, y aumentar la eficiencia en la predicción de demanda y manejo de inventarios.
