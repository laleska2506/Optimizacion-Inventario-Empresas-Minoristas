import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def run_prediction():
    # Cargar datos
    #data = pd.read_csv('data/augmented_supermarket_sales.csv')
    data = pd.read_csv('data/sales_data_500.csv')

    # Preprocesar datos
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce', dayfirst=True)
    data = data.dropna(subset=['Date'])  # Eliminar fechas inválidas

    # Extraer características de fecha
    data['Day'] = data['Date'].dt.day
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year

    # Seleccionar características, variable objetivo y columna de productos
    X = data[['Day', 'Month', 'Year', 'Quantity', 'Unit price']].values
    y = data['Total'].values
    products = data['Product line']  # Columna de productos

    # Escalar las características
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test, products_train, products_test = train_test_split(
        X, y, products, test_size=0.2, random_state=42
    )

    # Construir el modelo con TensorFlow
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)  # Salida de una sola neurona para regresión
    ])

    # Compilar el modelo
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Entrenar el modelo
    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

    # Evaluar el modelo en el conjunto de prueba
    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"MAE en el conjunto de prueba: {mae:.2f}")

    # Hacer predicciones
    predictions = model.predict(X_test).flatten()

    # Calcular el error cuadrático medio
    mse = mean_squared_error(y_test, predictions)
    print(f"MSE del modelo: {mse:.2f}")

    # Guardar las predicciones junto con los productos en un archivo CSV
    results = pd.DataFrame({
        'Product line': products_test.values,  # Agregar el producto correspondiente
        'Actual': y_test.round(2),             # Redondear valores reales
        'Predicted': predictions.round(2)      # Redondear predicciones
    })
    results.to_csv('outputs/predictions.csv', index=False)
    print("Predicciones guardadas en 'outputs/predictions.csv'")
