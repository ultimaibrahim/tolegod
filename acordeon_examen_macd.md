# 🎯 Acordeón Ejecutivo: Examen 1 de Matemáticas Aplicadas a Ciencia de Datos
**Estudiante:** Saúl Ibrahim García Morales  
**Profesor:** Iván Alejandro Toledano Juárez (`IvTole`)  
**Sede / Aula:** Martes 29 de Septiembre · 09:00 AM · Aula N 105  
**Plataforma:** MoLab (`molab.marimo.io`) y Jupyter Notebook  

---

## 📌 Tabla Maestra de Respuestas Numéricas (`student-mat.csv`)

| Inciso | Parámetro / Pregunta | Expresión / Código | Valor Exacto | Interpretación Resumida |
| :--- | :--- | :--- | :---: | :--- |
| **1.1 a** | Media ($\mu$) | `df['G3'].mean()` | **`10.4152`** | Rendimiento justo en el corte aprobatorio mínimo (10/20) |
| **1.1 a** | Mediana | `df['G3'].median()` | **`11.0000`** | 50% de la cohorte obtiene $\le 11$ y 50% $\ge 11$ |
| **1.1 a** | Moda | `df['G3'].mode()[0]` | **`10`** | La calificación más frecuente es 10 |
| **1.1 b** | Desviación Estándar ($s$) | `df['G3'].std()` | **`4.5814`** | Alta dispersión en las notas de los alumnos |
| **1.1 b** | Varianza ($s^2$) | `df['G3'].var()` | **`20.9896`** | Variabilidad cuadrática muestral ($ddof=1$) |
| **1.1 b** | Cuartil 1 ($Q_1$) | `df['G3'].quantile(0.25)` | **`8.00`** | 25% de alumnos tiene nota $\le 8$ |
| **1.1 b** | Cuartil 3 ($Q_3$) | `df['G3'].quantile(0.75)` | **`14.00`** | 75% de alumnos tiene nota $\le 14$ |
| **1.1 b** | Rango Intercuartílico (IQR) | $Q_3 - Q_1$ | **`6.00`** | El 50% central se dispersa en una ventana de 6 puntos |
| **1.2 b** | Outliers Boxplot (Tukey) | $[Q_1 - 1.5 IQR, Q_3 + 1.5 IQR]$ | **`0 outliers`** | Límites $[-1, 23]$; notas van de 0 a 20. Hay 38 ceros. |
| **1.2 c** | Correlación $G2$ vs $G3$ | `df['G2'].corr(df['G3'])` | **`r = 0.9049`** | Correlación lineal positiva sumamente fuerte |
| **2.1 a** | Parámetros Normal $\mathcal{N}(\mu, \sigma^2)$ | Media y Desv. Estándar | **$\mu = 10.42, \sigma = 4.58$** | Parámetros del modelo continuo |
| **2.2 a** | $P(G3 > 15)$ | `1 - stats.norm.cdf(15, mu, sigma)` | **`0.1585` (15.85%)** | $Z = 1.0007$ · `area_cdf_c(z)` |
| **2.2 b** | $P(10 \le G3 \le 14)$ | `cdf(14) - cdf(10)` | **`0.3191` (31.91%)** | $Z_1 = -0.0906, Z_2 = 0.7825$ · `area_between(z1, z2)` |
| **2.2 c** | Percentil 75 ($P_{75}$) | `stats.norm.ppf(0.75, mu, sigma)` | **`13.51 puntos`** | El 75% de los alumnos obtiene $\le 13.51$ |
| **2.2 d** | Límite Riesgo (Percentil 25) | `stats.norm.ppf(0.25, mu, sigma)` | **`7.33 puntos`** | Alumnos con nota $\le 7.33$ están en riesgo |
| **2.2 e** | Probabilidad Reprobar ($G3 < 10$) | `stats.norm.cdf(10, mu, sigma)` | **`0.4639` (46.39%)** | $Z = -0.0906$ · `area_cdf(z)` |
| **2.3 a** | Esperados con $G3 > 16$ en $N=500$ | $500 \times P(G3 > 16)$ | **`55.71` ($\approx 56$ alumnos)** | $P(G3 > 16) = 0.1114$ ($Z = 1.2190$) |
| **2.3 b** | Corte Tutorías (20% más bajo) | `stats.norm.ppf(0.20, mu, sigma)` | **`6.56 puntos`** | Alumnos con $G3 \le 6.56$ van a tutorías |

---

## 📝 Respuestas Teóricas y Reflexivas Redactadas

### 1.1 c) Desempeño General:
> la calificación final promedio se sitúa en 10.42 con mediana de 11.00 sobre 20, lo que refleja un rendimiento general apenas por encima del límite aprobatorio (10). la dispersión es amplia (desviación estándar de 4.58 y un iqr de 6.00 puntos, con el 50% central entre 8 y 14), evidenciando alta heterogeneidad en el aprovechamiento del curso.

### 1.2 b) Outliers en Boxplot:
> formalmente, bajo la regla de tukey ($1.5 \times \text{IQR}$), no existen outliers estadísticos fuera de los bigotes (0 valores anómalos), ya que el rango aceptable es $[-1.0, 23.0]$ y las calificaciones están acotadas entre 0 y 20. no obstante, existe un grupo anómalo de 38 estudiantes con calificación 0 (desertores o inasistencias) que no son detectados como outliers por el boxplot pero distorsionan la distribución.

### 1.2 c) Relación G2 vs G3:
> se observa una relación lineal positiva muy fuerte ($r = 0.9049$). los alumnos con alto desempeño en el segundo periodo replican casi con certeza notas altas en el examen final. los únicos casos discordantes son alumnos en la línea inferior ($G3 = 0$ teniendo $G2 \ge 8$), atribuibles a faltas o abandono previo al examen final.

### 1.3 a) Forma y Sesgo de la Distribución:
> la distribución presenta una ligera asimetría a la izquierda (sesgo negativo). en el cuerpo principal ($G3 > 0$) tiene una silueta acampanada aproximadamente simétrica en torno a 10-12, pero el cúmulo artificial de 38 estudiantes con calificación 0 alarga la cola izquierda y rompe la simetría gaussiana pura.

### 1.3 b) Comparación Media vs Mediana:
> al ser $\text{media} < \text{mediana}$ ($10.42 < 11.00$), se confirma numéricamente el sesgo hacia la izquierda. la media es sensible a valores extremos y fue arrastrada hacia abajo por los 38 ceros, mientras que la mediana resistió el sesgo manteniéndose en 11.00.

### 2.1 c) Gráfico Q-Q Plot:
> los datos siguen aproximadamente una normal únicamente en el segmento central (entre cuantiles teóricos -1.0 y +1.5, notas de 6 a 16), donde los puntos se adhieren a la diagonal roja. sin embargo, no se ajusta en las colas: en la cola inferior hay un desvío severo hacia abajo por los 38 ceros (inflación de ceros), y en la cola superior la curva se aplana por el límite superior de 20 puntos.

### 2.3 c) Reflexión Crítica del Modelo Normal y Limitaciones:
> la distribución normal es una buena aproximación didáctica para estimar probabilidades en el rango medio, pero tiene 3 limitaciones severas en datos académicos:
> 1. **soporte infinito vs escala acotada**: la normal asigna probabilidad a notas $< 0$ y $> 20$, lo cual es físicamente imposible.
> 2. **inflación de ceros (zero-inflation)**: el abandono escolar crea una masa artificial en $0$ que genera bimodalidad y distorsiona media y varianza.
> 3. **naturaleza discreta**: las calificaciones son enteras, mientras que la normal asume una variable continua real.

---

## 🚗 Blindaje de Emergencia: Variantes Automóviles (`mpg.csv`)

Si en el aula N 105 el profesor aplica las variantes alternas del repositorio (`acceleration` y `weight`):

### Parámetros Generales:
- **Variable**: `acceleration` (segundos de 0 a 60 mph)
- **Media ($\mu$)**: `15.5681 s` | **Mediana**: `15.5000 s` | **Moda**: `14.5 s`
- **Desviación Estándar ($\sigma$)**: `2.7577 s` | **Varianza**: `7.6048 s^2` | **IQR**: `3.3500 s`
- **Outliers**: 7 valores fuera de bigotes: `[8.5, 8.5, 8.0, 23.5, 24.8, 23.7, 24.6]`
- **Correlación Weight vs Acceleration**: `r = -0.4175` (moderada negativa: a mayor peso, menor aceleración/más lento)

### Variante Cars V1 (`MAT_Examen1.py`):
1. $P(\text{acc} > 18)$: **`0.1889` (18.89%)** | $Z = 0.8819$
2. $P(14 \le \text{acc} \le 17)$: **`0.4134` (41.34%)**
3. Aceleración rápida (Percentil 25): **`13.71 segundos`**
4. $P(\text{acc} < 12)$: **`0.0979` (9.79%)** | $Z = -1.2939$
5. Esperados acc $> 20$ en 1000 autos: **`54 autos`** ($P = 0.0540$)
6. Top 15% mejor aceleración (Percentil 15): **`12.71 segundos`**

### Variante Cars V2 (`MAT_Examen1_V2.py`):
1. $P(\text{acc} < 13)$: **`0.1759` (17.59%)** | $Z = -0.9312$
2. $P(15 \le \text{acc} \le 19)$: **`0.4749` (47.49%)**
3. Aceleración lenta (20% más lentos, mayores tiempos = Percentil 80): **`17.89 segundos`**
4. $P(\text{acc} > 17)$: **`0.3018` (30.18%)** | $Z = 0.5192$
5. Esperados en 800 autos entre 13 y 16 s: **`309 autos`** ($P = 0.3864$)
6. Top 10% mejor aceleración (Percentil 10): **`12.03 segundos`**
