# 🎯 Acordeón Ejecutivo: Examen 1 (Versión 2) — MACD 2026B
**Estudiante:** Saúl Ibrahim García Morales  
**Profesor:** Iván Alejandro Toledano Juárez (`IvTole`)  
**Fecha & Sede:** Martes 29 de Septiembre · 09:00 AM · Aula N 105  
**Examen Oficial:** `MAT_Examen1_V2.py` / `GarciaSaul-Examen1-V2.py`  
**Dataset:** `mpg.csv` (Auto MPG — variable objetivo: `acceleration` en segundos)

---

## 📌 Tabla Maestra de Respuestas Numéricas (`MAT_Examen1_V2.py`)

| Inciso | Pregunta | Expresión / Código | Valor Exacto | Unidades |
| :--- | :--- | :--- | :---: | :---: |
| **1. a** | Media ($\mu$) | `df['acceleration'].mean()` | **`15.5681`** | **segundos** |
| **1. a** | Mediana | `df['acceleration'].median()` | **`15.5000`** | **segundos** |
| **1. a** | Moda | `df['acceleration'].mode()[0]` | **`14.5000`** | **segundos** |
| **1. b** | Desviación Estándar ($s$) | `df['acceleration'].std()` | **`2.7577`** | **segundos** |
| **1. b** | Varianza ($s^2$) | `df['acceleration'].var()` | **`7.6048`** | **segundos²** |
| **1. b** | Cuartil 1 ($Q_1$) | `df['acceleration'].quantile(0.25)` | **`13.8250`** | **segundos** |
| **1. b** | Cuartil 3 ($Q_3$) | `df['acceleration'].quantile(0.75)` | **`17.1750`** | **segundos** |
| **1. b** | Rango Intercuartílico (IQR) | $Q_3 - Q_1$ | **`3.3500`** | **segundos** |
| **Vis. b** | Outliers Boxplot (Tukey) | $[Q_1 - 1.5 IQR, Q_3 + 1.5 IQR]$ | **7 outliers** (`[8.0, 8.5, 8.5, 23.5, 23.7, 24.6, 24.8]`) | **segundos** |
| **Vis. c** | Relación `weight` vs `acceleration` | `df['weight'].corr(df['acceleration'])` | **`r = -0.4175`** (Moderada negativa) | Adimensional |
| **Dist. b** | Comparación Media vs Mediana | Diferencia $\mu - \text{Mediana}$ | **$\approx 0$** ($15.57 \approx 15.50$, simétrica) | **segundos** |
| **Gauss. a** | Parámetros Normal $\mathcal{N}(\mu, \sigma^2)$ | Media y Desv. Estándar | **$\mu = 15.5681\text{ s}, \sigma = 2.7577\text{ s}$** | **segundos** |
| **Prob. a** | $P(\text{acceleration} < 13)$ | `stats.norm.cdf(13, mu, sigma)` | **`0.1759` (17.59%)** · $Z = -0.9312$ | Probabilidad |
| **Prob. b** | $P(15 \le \text{acceleration} \le 19)$ | `cdf(19) - cdf(15)` | **`0.4749` (47.49%)** · $Z_1=-0.21, Z_2=1.24$ | Probabilidad |
| **Prob. c** | Aceleración Lenta (20% mayores tiempos) | `stats.norm.ppf(0.80, mu, sigma)` | **`17.8890` ($\approx 17.89\text{ s}$)** | **segundos** |
| **Prob. d** | $P(\text{acceleration} > 17)$ | `1 - stats.norm.cdf(17, mu, sigma)` | **`0.3018` (30.18%)** · $Z = 0.5192$ | Probabilidad |
| **Aplic. a** | Esperados entre 13 y 16 s en lote de 800 | $800 \times P(13 \le X \le 16)$ | **`309.09` ($\approx 309$ automóviles)** ($P=38.64\%$) | Automóviles |
| **Aplic. b** | Revista Top 10% Rápido (menor tiempo) | `stats.norm.ppf(0.10, mu, sigma)` | **`12.0340` ($\approx 12.03\text{ s}$)** | **segundos** |

---

## 📝 Respuestas Conceptuales de Examen (Listas para Copiar)

- **1. c) Interpretación EDA**:
  > el tiempo promedio de aceleración es de 15.57 segundos con mediana de 15.50 s y moda de 14.50 s. la dispersión es moderada (desviación estándar de 2.76 s e iqr de 3.35 s), concentrándose el 50% central entre 13.83 y 17.18 segundos. refleja un conjunto automotriz con desempeño homogéneo centrado en los 15.5 s, con ligeras colas derivadas de la disparidad entre compactos y sedanes de la época.

- **Vis. b) Outliers**:
  > bajo la regla de tukey ($1.5 \times \text{IQR}$, límites $[8.80, 22.20]$ s), existen **7 outliers estadísticos**: 3 vehículos de aceleración rápida en la cola inferior (`[8.0, 8.5, 8.5]` s) y 4 vehículos lentos en la cola superior (`[23.5, 23.7, 24.6, 24.8]` s).

- **Vis. c) Relación Peso vs Aceleración**:
  > correlación lineal negativa moderada ($r = -0.4175$). a mayor peso del automóvil, menor tiempo en segundos para alcanzar 60 mph. históricamente, los autos más pesados montaban motores v8 potentes con gran torque, permitiéndoles acelerar en menos segundos que los autos pequeños y ligeros de baja cilindrada.

- **Dist. a) y b) Simetría**:
  > la distribución es **aproximadamente simétrica con un leve sesgo positivo a la derecha**. la media (15.57 s) y la mediana (15.50 s) son prácticamente idénticas ($\Delta = 0.068$ s, diferencia menor al 0.4%), lo que ratifica la simetría central con un estiramiento mínimo en la cola derecha por los 4 autos muy lentos.

- **Gauss. c) Gráfico Q-Q**:
  > los datos siguen aproximadamente una distribución normal de manera muy satisfactoria. entre los cuantiles teóricos -2 y +2, los puntos se adhieren casi con precisión milimétrica a la recta roja de 45°. únicamente en el extremo superior derecho (cuantiles > 2.5) los vehículos más lentos se dispersan levemente, pero el ajuste general es de alta calidad para fines inferenciales.

- **Aplic. c) Reflexión Crítica y Limitaciones**:
  > el modelo gaussiano es una excelente aproximación univariada por la simetría de los datos, pero presenta 3 limitaciones físicas:
  > 1. *soporte no acotado*: asigna probabilidades a tiempos negativos ($t < 0$), físicamente imposibles.
  > 2. *límites biomecánicos y de adherencia*: ningún auto de combustión puede acelerar en 0 o 1 s por fricción de neumáticos y potencia.
  > 3. *simplificación univariada*: la aceleración en la física automotriz depende de una relación no lineal multivariada (torque, caballos de fuerza, masa, relación de diferencial y aerodinámica) que no puede ser capturada por una única variable aislada.
