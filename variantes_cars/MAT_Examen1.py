# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "pandas",
#     "numpy",
#     "matplotlib",
#     "seaborn",
#     "scipy",
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(
    width="medium",
    app_title="Matemáticas Aplicadas a Ciencia de Datos — Examen 1",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <center> <span style="color:indigo">Machine Learning e Inferencia Bayesiana</span> </center>

    <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Centro_Universitario_del_Guadalajara_Logo.png" style="width: 800px;"/>
    </div>

    <center> <span style="color:DarkBlue">  Examen 1. Análisis Exploratorio de Datos y Distribución Gaussiana </span>  </center>
    <center> <span style="color:Blue"> Profesor: Iván A. Toledano Juárez </span>  </center>

    ## Matemáticas Aplicadas a Ciencia de Datos: Examen 1

    Vamos a utilizar el dataset **MPG (Miles Per Gallon)** que contiene información sobre 398 automóviles fabricados entre 1970 y 1982. El dataset incluye características técnicas de los vehículos como consumo de combustible, número de cilindros, potencia, peso, y aceleración.

    **Variables principales:**
    - `acceleration`: Tiempo de aceleración de 0 a 60 mph en segundos (8.0 - 24.8)
    - `mpg`: Millas por galón (consumo de combustible)
    - `cylinders`: Número de cilindros (4, 6, 8)
    - `displacement`: Cilindrada del motor (pulgadas cúbicas)
    - `horsepower`: Caballos de fuerza
    - `weight`: Peso del vehículo (libras)
    - `model_year`: Año del modelo (70-82)
    - `origin`: Origen (usa, europe, japan)
    - `name`: Nombre del vehículo
    """)
    return


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    # Importar librerías necesarias
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

    return mo, np, pd, plt, stats


@app.cell
def _(pd):
    # Cargar el dataset
    url = "https://raw.githubusercontent.com/IvTole/Matematicas_Aplicadas_Ciencia_De_Datos_CUGDL/refs/heads/main/data/cars/mpg.csv"
    df = pd.read_csv(url)
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funciones de apoyo

    Se añaden algunas funciones que los ayudarán a resolver los ejercicios relacionados con distribución gaussiana.

    Recuerda que el z-valor puede ser calculado a partir de los datos originales $x$, y viceversa, a partir de las siguientes ecuaciones,

    \begin{equation}
    z = \frac{x - \mu}{\sigma}; \quad x = z\sigma + \mu
    \end{equation}

    Recuerda que puedes utilizar el método `stats.norm.cdf(z)`de `scipy` para calcular la CDF (Cumulative Distribution Function, área bajo la cuva) a partir de un valor $z$, además de calcular un valor $z$ a partir de una CDF con `stats.norm.ppf(cdf)` (Percent Point Function). El método `stats.norm.pdf(z, loc, scale)` sirve para evaluar un valor z de entrada en la distribución de probabilidad teórica, dada una media(loc) y una desviación estándar(scale) para dicha distribución.
    """)
    return


@app.cell
def _(np, plt, stats):
    ## Grafica una distribucion acumulada hasta cierto punto z
    def area_cdf(z):
        x = np.arange(-10,z,0.001) # se genera una lista con puntos entre dos valores, para el área marcada
        x_full = np.arange(-10,10,0.001) # lista de valores donde se va a graficar toda la curva de Gauss

        # utilizamos z-values, la distribucion estandar, con scipy.stats
        y = stats.norm.pdf(x, 0, 1)
        y_full = stats.norm.pdf(x_full, 0, 1)

        fig, ax = plt.subplots(figsize=(5,3))

        ax.plot(x_full,y_full)
        ax.fill_between(x,y,0, alpha=0.3, color='b')
        ax.fill_between(x_full,y_full,0, alpha=0.1)
        ax.set_xlim([-5,5])
        ax.set_xlabel('z, # de desviaciones estandar con respecto de la media ')
        ax.set_title('Distribución Normal Estándar')

        plt.show()

        area = stats.norm.cdf(z)

        print(f'Area bajo la curva : {area}')

        return area

    return


@app.cell
def _(np, plt, stats):
    ## Grafica el area bajo la curva entre dos puntos z

    def area_between(z1,z2): # z1 min, z2 max
        x = np.arange(z1,z2,0.001) # se genera una lista con puntos entre dos valores, para el área marcada
        x_full = np.arange(-10,10,0.001) # lista de valores donde se va a graficar toda la curva de Gauss

        # utilizamos z-values, la distribucion estandar, con scipy.stats
        y = stats.norm.pdf(x, 0, 1)
        y_full = stats.norm.pdf(x_full, 0, 1)

        fig, ax = plt.subplots(figsize=(5,3))

        ax.plot(x_full,y_full)
        ax.fill_between(x,y,0, alpha=0.3, color='b')
        ax.fill_between(x_full,y_full,0, alpha=0.1)
        ax.set_xlim([-5,5])
        ax.set_xlabel('z, # de desviaciones estandar con respecto de la media ')
        ax.set_title('Distribución Normal Estándar')

        plt.show()

        area = stats.norm.cdf(z2) - stats.norm.cdf(z1)

        print(f'Area bajo la curva : {area}')

        return area

    return


@app.cell
def _(np, plt, stats):
    ## Grafica una distribucion acumulada hasta cierto punto z
    def area_cdf_c(z):
        x = np.arange(z,10,0.001) # se genera una lista con puntos entre dos valores, para el área marcada
        x_full = np.arange(-10,10,0.001) # lista de valores donde se va a graficar toda la curva de Gauss

        # utilizamos z-values, la distribucion estandar, con scipy.stats
        y = stats.norm.pdf(x, 0, 1)
        y_full = stats.norm.pdf(x_full, 0, 1)

        fig, ax = plt.subplots(figsize=(5,3))

        ax.plot(x_full,y_full)
        ax.fill_between(x,y,0, alpha=0.3, color='b')
        ax.fill_between(x_full,y_full,0, alpha=0.1)
        ax.set_xlim([-5,5])
        ax.set_xlabel('z, # de desviaciones estandar con respecto de la media ')
        ax.set_title('Distribución Normal Estándar')

        plt.show()

        area = 1.0 - stats.norm.cdf(z)

        print(f'Area bajo la curva : {area}')

        return area

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Responde a las siguientes preguntas dentro del Notebook. Cuando finalices, guárdalo con forma **\<apellido-nombre\>-Examen1.py** y súbelo a la plataforma correspondiente.

    En marimo, escribe tus soluciones en las celdas de código y edita los textos de *Respuesta:* para añadir tus interpretaciones. Las variables se definen en una sola celda y pueden usarse en las siguientes; para variables auxiliares que quieras reutilizar en distintas celdas, emplea nombres locales como `_fig` y `_ax`. Para mostrar una gráfica, deja `_fig` o `_ax` como última expresión de la celda, o utiliza `plt.show()`.

    ## Análisis Exploratorio de Datos

    ### Medidas de Tendencia Central y Dispersión

    Para la variable **acceleration (tiempo de aceleración 0-60 mph en segundos)**:

    **a) Calcula la media, mediana y moda**. Escribe también sus unidades correspondientes.
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Calcula la desviación estándar, varianza y rango intercuartílico (IQR)**. Escribe también sus unidades correspondientes.
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Interpreta estos resultados: ¿Qué te dicen sobre la aceleración de los automóviles en este dataset?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Visualización

    **a) Crea un histograma de la variable acceleration con al menos 10 bins.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Crea un boxplot de acceleration. Identifica si existen outliers y menciona cuántos hay.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Crea un scatter plot entre weight (eje x) y acceleration (eje y). ¿Qué relación observas?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Análisis de Distribución

    **a) Observando el histograma de acceleration, ¿consideras que la distribución es aproximadamente simétrica, sesgada a la derecha o sesgada a la izquierda? Justifica tu respuesta**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Compara la media y la mediana de acceleration. ¿Qué te indica esta comparación sobre la simetría de los datos?**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Distribución Gaussiana

    ### Ajuste de Distribución Normal

    Considera la variable **acceleration (tiempo de aceleración)**.

    **a) Estima los parámetros μ (media) y σ (desviación estándar) de una distribución normal que se ajuste a los datos de acceleration.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Crea un gráfico que superponga:**
    - **El histograma normalizado (densidad) de acceleration**
    - **La curva de la distribución normal N(μ, σ²) con los parámetros estimados**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Crea un gráfico Q-Q (quantile-quantile plot) para evaluar qué tan bien se ajusta acceleration a una distribución normal. ¿Los datos siguen aproximadamente una distribución normal? Justifica.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Cálculo de Probabilidades

    Asumiendo que acceleration sigue una distribución normal con los parámetros estimados en el punto anterior:

    **a) ¿Cuál es la probabilidad de que un automóvil seleccionado al azar tenga una aceleración mayor a 18 segundos?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) ¿Cuál es la probabilidad de que un automóvil tenga una aceleración entre 14 y 17 segundos?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Si se considera que un automóvil tiene "aceleración rápida" si está por debajo del percentil 25, ¿cuál es el tiempo límite para esta clasificación?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **d) ¿Cuál es la probabilidad de que un automóvil tenga una aceleración menor a 12 segundos?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interpretación y Aplicación

    **a) Basándote en el modelo gaussiano ajustado, si una fábrica produce 1000 automóviles, ¿aproximadamente cuántos automóviles esperarías que tengan una aceleración mayor a 20 segundos?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Una revista de automóviles quiere seleccionar el 15% de autos con mejor aceleración (menor tiempo) para una categoría especial. ¿Cuál debería ser el tiempo máximo de aceleración para calificar?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu solución.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Reflexiona: ¿Consideras que el modelo de distribución normal es apropiado para modelar la aceleración de los automóviles? ¿Qué limitaciones podría tener este modelo?**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Criterios de Evaluación

    - **Justificación matemática y estadística**: 50%
    - **Calidad del código y visualizaciones**: 25%
    - **Interpretación y análisis crítico**: 25%

    **Total: 100 puntos**
    """)
    return


if __name__ == "__main__":
    app.run()
