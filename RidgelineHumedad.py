# Se importan las librerías necesarias
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Estilo para poder solapar subplots
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Se leen los datos del CSV obtenido del Kaggle: https://www.kaggle.com/datasets/sumandey/temperature-and-humidity-of-kolkata-from-20152020?select=weather_data_kolkata_2015_2020.csv
temp = pd.read_csv('https://raw.githubusercontent.com/isrosrey/DataVisualizationPEC2/main/data/weather_data_kolkata_2015_2020.csv', sep=',')

# Se crea una columna separada para el mes
temp['mes'] = pd.to_datetime(temp['DATETIME']).dt.month

# Se define un diccionario con los meses que se mostrarán en el gráfico
dict_meses = {1: 'enero',
              2: 'febrero',
              3: 'marzo',
              4: 'abril',
              5: 'mayo',
              6: 'junio',
              7: 'julio',
              8: 'agosto',
              9: 'septiembre',
              10: 'octubre',
              11: 'noviembre',
              12: 'diciembre'}

# Se mapea la columna para el mes con los nombres del diccionario
temp['mes']= temp['mes'].map(dict_meses)

# Se crea una columna con la media de humedad de cada mes
# Esta información se usa para los colores del gráfico
serie_media_humedad = temp.groupby('mes')['HUMIDITY'].mean()
temp['humedad_media'] = temp['mes'].map(serie_media_humedad)

# Se genera una paleta de color con Seaborn.color_palette()
pal = sns.color_palette(palette='coolwarm', n_colors=12)

# En la clase sns.FacetGrid, el argumento 'hue' es el que representará los colores de la paleta indicada en 'palette'
g = sns.FacetGrid(temp, row='mes', hue='humedad_media', aspect=15, height=0.75, palette=pal)

# Se añaden las densidades para cada año
g.map(sns.kdeplot, 'HUMIDITY',
      bw_adjust=0.5, clip_on=False,
      fill=True, alpha=0.7, linewidth=0.5)

# Se añade una línea blanca que muestra el contorno de cada kdeplot
g.map(sns.kdeplot, 'HUMIDITY', 
      bw_adjust=0.5, clip_on=False, 
      color="w", lw=1)

# Se añade la línea horizontal de cada plot
g.map(plt.axhline, y=0,
      lw=2, clip_on=False)

# we loop over the FacetGrid figure axes (g.axes.flat) and add the month as text with the right color
# notice how ax.lines[-1].get_color() enables you to access the last line's color in each matplotlib.Axes
for i, ax in enumerate(g.axes.flat):
    ax.text(-5, 0.01, dict_meses[i+1],
            fontweight='bold', fontsize=15,
            color=ax.lines[-1].get_color())
    ax.set_ylabel("")

# we use matplotlib.Figure.subplots_adjust() function to get the subplots to overlap
g.figure.subplots_adjust(hspace=-0.5)

# eventually we remove axes titles, yticks and spines
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)

plt.setp(ax.get_xticklabels(), fontsize=15, fontweight='bold')
plt.xlabel('Humedad (%)', fontweight='bold', fontsize=15)
g.fig.suptitle('Humedad media mensual en Kolkata',
               ha='center',
               fontsize=20,
               fontweight=20)

plt.savefig('./output/RidgelineChart.png')
plt.show()