# ⚡ ToleGod: Examen 1 — Matemáticas Aplicadas a Ciencia de Datos

> **Autor:** Ibrahim García (`ultimaibrahim`)  
> **Profesor:** Iván Alejandro Toledano Juárez (`IvTole`)  
> **Semestre:** 2026B — Aula N 105 (09:00 - 11:00 AM)  
> **Plataformas:** [MoLab Cloud](https://molab.marimo.io) & Jupyter Notebook  

---

## 🎯 Acceso Rápido y Modos de Uso

### Opción 1: Abrir en MoLab (`molab.marimo.io`)
1. Entra a [molab.marimo.io](https://molab.marimo.io/).
2. Haz clic en **Upload / Import** y selecciona [`examen_student_performance.py`](examen_student_performance.py) de este repositorio.
3. Sube también [`student-mat.csv`](student-mat.csv) al workspace de MoLab (o en el mismo directorio).
4. ¡El notebook reactivo se ejecutará automáticamente con todas las celdas, gráficos y respuestas ya resueltas!

### Opción 2: Ver Offline en el Navegador
- Abre [`examen_student_performance_RESUELTO.html`](examen_student_performance_RESUELTO.html) en Chrome, Brave, Firefox o Edge para interactuar con el reporte completo sin necesidad de conexión.

### Opción 3: Ejecución Local con Marimo o Jupyter
```bash
# Con Marimo
pip install marimo
marimo run examen_student_performance.py
# o en modo edición
marimo edit examen_student_performance.py

# Con Jupyter Notebook
jupyter notebook examen_student_performance_RESUELTO_SaulGarcia.ipynb
```

---

## 📊 Tabla Maestra de Respuestas Numéricas (`student-mat.csv`)

| Inciso | Parámetro / Pregunta | Expresión / Código | Valor Exacto | Interpretación Resumida |
| :--- | :--- | :--- | :---: | :--- |
| **1.1 a** | Media ($\mu$) | `df['G3'].mean()` | **`10.4152`** | Desempeño justo en el límite aprobatorio institucional (10/20) |
| **1.1 a** | Mediana | `df['G3'].median()` | **`11.0000`** | 50% de la cohorte obtiene $\le 11$ y 50% $\ge 11$ |
| **1.1 a** | Moda | `df['G3'].mode()[0]` | **`10`** | Calificación modal más repetida |
| **1.1 b** | Desviación Estándar ($s$) | `df['G3'].std()` | **`4.5814`** | Alta dispersión en las calificaciones |
| **1.1 b** | Varianza ($s^2$) | `df['G3'].var()` | **`20.9896`** | Variabilidad cuadrática muestral ($ddof=1$) |
| **1.1 b** | Cuartil 1 ($Q_1$) | `df['G3'].quantile(0.25)` | **`8.00`** | 25% de alumnos con nota $\le 8$ |
| **1.1 b** | Cuartil 3 ($Q_3$) | `df['G3'].quantile(0.75)` | **`14.00`** | 75% de alumnos con nota $\le 14$ |
| **1.1 b** | Rango Intercuartílico (IQR) | $Q_3 - Q_1$ | **`6.00`** | El 50% central se ubica entre 8 y 14 puntos |
| **1.2 b** | Outliers Boxplot (Tukey) | $[Q_1 - 1.5 IQR, Q_3 + 1.5 IQR]$ | **`0 outliers`** | Límites $[-1, 23]$. Escala de 0 a 20. Hay 38 notas en cero |
| **1.2 c** | Correlación $G2$ vs $G3$ | `df['G2'].corr(df['G3'])` | **`r = 0.9049`** | Correlación lineal positiva sumamente fuerte |
| **2.1 a** | Parámetros Normal $\mathcal{N}(\mu, \sigma^2)$ | Media y Desv. Estándar | **$\mu = 10.42, \sigma = 4.58$** | Parámetros del modelo continuo |
| **2.2 a** | $P(G3 > 15)$ | `1 - stats.norm.cdf(15, mu, sigma)` | **`0.1585` (15.85%)** | $Z = 1.0007$ · `area_cdf_c(z)` |
| **2.2 b** | $P(10 \le G3 \le 14)$ | `cdf(14) - cdf(10)` | **`0.3191` (31.91%)** | $Z_1 = -0.0906, Z_2 = 0.7825$ · `area_between(z1, z2)` |
| **2.2 c** | Percentil 75 ($P_{75}$) | `stats.norm.ppf(0.75, mu, sigma)` | **`13.51 puntos`** | El 75% de alumnos obtiene $\le 13.51$ puntos |
| **2.2 d** | Límite Riesgo (Percentil 25) | `stats.norm.ppf(0.25, mu, sigma)` | **`7.33 puntos`** | Alumnos con nota $\le 7.33$ están en riesgo |
| **2.2 e** | Probabilidad Reprobar ($G3 < 10$) | `stats.norm.cdf(10, mu, sigma)` | **`0.4639` (46.39%)** | $Z = -0.0906$ · `area_cdf(z)` |
| **2.3 a** | Esperados con $G3 > 16$ en $N=500$ | $500 \times P(G3 > 16)$ | **`55.71` ($\approx 56$ alumnos)** | $P(G3 > 16) = 0.1114$ ($Z = 1.2190$) |
| **2.3 b** | Corte Tutorías (20% más bajo) | `stats.norm.ppf(0.20, mu, sigma)` | **`6.56 puntos`** | Alumnos con $G3 \le 6.56$ van a tutorías |

---

## 📝 Respuestas Conceptuales de Bolsillo

- **1.1 c) Desempeño General**: Promedio de 10.42 y mediana de 11.00 sobre 20. Desempeño apenas aprobatorio con alta dispersión ($s=4.58$, IQR$=6$), indicando gran heterogeneidad en el grupo.
- **1.2 b) Outliers**: 0 outliers formales bajo la regla de Tukey ($1.5 \times \text{IQR}$) porque los límites son $[-1.0, 23.0]$ y las notas están acotadas en $[0, 20]$. No obstante, hay **38 ceros** por deserción/inasistencias al examen final.
- **1.2 c) Relación G2 vs G3**: Correlación lineal positiva muy fuerte ($r=0.9049$). Buen rendimiento en G2 predice fielmente buen resultado en G3.
- **1.3 a) y b) Distribución y Asimetría**: Sesgo leve a la izquierda ($\text{media} < \text{mediana}$, $10.42 < 11.00$). Los 38 ceros jalaron la media hacia abajo mientras que la mediana resistió el sesgo.
- **2.1 c) Gráfico Q-Q**: Los datos se ajustan a la normal en el cuerpo central (cuantiles -1 a +1.5, notas de 6 a 16). Se desvían severamente en las colas por la inflación de 38 ceros abajo y el truncamiento en 20 arriba.
- **2.3 c) Limitaciones del Modelo Normal**:
  1. *Soporte infinito*: Asigna probabilidad teórica a notas $< 0$ y $> 20$.
  2. *Inflación de ceros (zero-inflation)*: No modela la bimodalidad causada por deserción escolar.
  3. *Discretitud*: Las calificaciones son números enteros, no continuos.

---

## 🚗 Carpeta `variantes_cars/` (Blindaje Preventivo)
Contiene las variantes `MAT_Examen1.py` y `MAT_Examen1_V2.py` con el dataset `mpg.csv` (`acceleration` y `weight`) por si en el aula se divide el salón por filas. Ver el acordeón en [`acordeon_examen_macd.md`](acordeon_examen_macd.md) para los números exactos de esas variantes.
