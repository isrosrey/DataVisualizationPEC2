# Ejemplo de código original obtenido en: https://python-graph-gallery.com/390-basic-radar-chart

# Librerías necesarias
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Se leen los datos del CSV obtenido del INE: https://www.ine.es/up/kBpWj4DtiD
temp = pd.read_csv('https://raw.githubusercontent.com/isrosrey/DataVisualizationPEC2/main/data/Poblacion6Municipios.csv',
                    sep=';', encoding='ansi', thousands='.')

# Se elimina el código postal
temp["Municipios"] = temp["Municipios"].str.extract('\s(.*)')

# Se eliminan datos de Sexo y Periodo que no se usarán
temp = temp.drop(['Sexo', 'Periodo'], axis=1)
# Se transponen los datos para tener una columna con cada municipio
temp = temp.T
# Se asignan los municipios como cabecera de la tabla
temp.columns = temp.iloc[0]
# Se elimina la fila con los nombres de los municipios que sería redundante
temp = temp.drop(temp.index[0])

# cantidad de variables
categories=list(temp)[0:]
N = len(categories)

values = temp.iloc[0].to_list()
values.append(values[0])
values
 
# Se calcula el ángulo de cada eje en el gráfico (Se divide el gráfico entre el número de variables)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Se inicializa el gráfico de radar
ax = plt.subplot(111, polar=True)
 
# Dibuja un eje por cada variable y se añaden las etiquetas
plt.xticks(angles[:-1], categories, color='blue', size=10)
 
# Se añaden las etiquetas del eje Y
ax.set_rlabel_position(0)
plt.yticks([5000,15000,25000],
           ["5000","15000","25000"],
           color="grey", size=7)
plt.ylim(0,35000)
 
# Se pintan los datos
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
# Se rellena el área
ax.fill(angles, values, 'b', alpha=0.1)

# Se muestra el gráfico
plt.show()