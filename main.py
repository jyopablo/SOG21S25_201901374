import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde el archivo CSV
file_path = "./winequality-red.csv"  # Reemplaza con la ruta de tu archivo
df = pd.read_csv(file_path, delimiter=';')

# 1. Limpieza de datos
print("Datos faltantes por columna:\n", df.isnull().sum())

# 2. Resumen estadístico
print("\nResumen estadístico:")
print(df.describe())

# 3. Matriz de correlación
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación")
plt.show()

# 4. Gráficos

# Histograma del alcohol
plt.figure(figsize=(8, 4))
sns.histplot(df["alcohol"], bins=10, kde=True, color="blue")
plt.title("Distribución del alcohol")
plt.xlabel("Alcohol")
plt.ylabel("Frecuencia")
plt.show()

# Boxplot de la acidez fija según la calidad
plt.figure(figsize=(8, 4))
sns.boxplot(x="quality", y="fixed acidity", data=df)
plt.title("Acidez fija vs Calidad")
plt.xlabel("Calidad")
plt.ylabel("Acidez fija")
plt.show()

# Relación entre ácido cítrico y alcohol
plt.figure(figsize=(8, 4))
sns.scatterplot(x="citric acid", y="alcohol", data=df, hue="quality", palette="viridis")
plt.title("Ácido cítrico vs Alcohol")
plt.xlabel("Ácido Cítrico")
plt.ylabel("Alcohol")
plt.show()


