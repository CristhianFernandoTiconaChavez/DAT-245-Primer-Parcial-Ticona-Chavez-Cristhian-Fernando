import pandas as pd
import numpy as np

base_de_datos = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSHIdebxvXrtk2R2u86LNg6S-5xB5QDPFcCtq2diM3slZGkoSnk9cFp-YMaVZJayhw6cgOU1kywZanU/pub?gid=507241814&single=true&output=csv")
datos = base_de_datos.values

#a)
print("\na)\n\n")

def calcular_cuartil_percentil(datos, numero_cuartil, numero_percentil):
    numero_de_columnas = len(datos[0])
    ultimos_cuartiles = []
    percentiles_80 = []

    for i in range(numero_de_columnas):
        valores_de_columna = [row[i] for row in datos]
        #if (type(valores_de_columna[0]) != str): Si, no quisiéramos los datos no numéricos
        valores_de_columna.sort()
        cuartil = valores_de_columna[int(len(valores_de_columna) * (0.25 * numero_cuartil))]
        percentil_80 = valores_de_columna[int(len(valores_de_columna) * (0.01 * numero_percentil))]
        ultimos_cuartiles.append(cuartil)
        percentiles_80.append(percentil_80)

    return ultimos_cuartiles, percentiles_80

ultimos_cuartiles, percentiles_80 = calcular_cuartil_percentil(datos, 3, 80)
#últimos cuartiles
matriz_ultimos_cuartiles = np.array(ultimos_cuartiles).reshape(1, 8)
df_ultimos_cuartiles = pd.DataFrame(matriz_ultimos_cuartiles, columns=['Película', 'Fin de semana', 'Total', '% de total', 'Cines', 'Promedio', 'Fecha', 'Distribuidor'])
print("ÚLTIMOS CUARTILES POR COLUMNA:\n\n----------------------------------------------------------------------------------------------------------------------------\n", df_ultimos_cuartiles.to_string(index = False), "\n----------------------------------------------------------------------------------------------------------------------------\n")
print("-Película:\n  Ordenadas alfabéticamente, en el puesto 750 se encuentra \"The Chronicles of Riddick\", esto significa que el 75% de las películas más taquilleras tiene un nombre que empieza o está por debajo de la letra \"T\"")
print("-Fin de semana:\n  El 75% de las películas más taquilleras, en su primer fin de semana tienen una recaudación por debajo de 54,471,475$")
print("-Total:\n  El 75% de las películas más taquilleras tiene una recaudación total por debajo de 182,618,434$")
print("-% del total:\n  El 75% de las películas más taquilleras, tiene un porcentaje de los ingresos brutos totales representado por los ingresos del primer fin de semana de apertura por debajo de 37.9%")
print("-Cines:\n  El 75% de las películas más taquilleras se estrenó en menos de 3,876 cines")
print("-Promedio:\n  El 75% de las películas más taquilleras tiene un promedio de recaudación en cada cine por debajo de 14,900$")
print("-Fecha:\n  Ordenadas alfabéticamente, el 75% de las películas más taquilleras se estrenó antes de la fecha 22-11-1995")
print("-Distribuidor:\n  Ordenadas alfabéticamente, en el puesto 750 se encuentra \"Walt Disney Studios Motion Pictures\", esto quiere decir que el 75% de las distribuidoras, tiene un nombre que empieza o está por debajo de la letra \"W\"")

#Percentiles 80
matriz_percentiles_80 = np.array(percentiles_80).reshape(1, 8)
df_percentiles_80 = pd.DataFrame(matriz_percentiles_80, columns=['Película', 'Fin de semana', 'Total', '% de total', 'Cines', 'Promedio', 'Fecha', 'Distribuidor'])
print("\nPERCENTILES 80 POR COLUMNA:\n\n----------------------------------------------------------------------------------------------------------------------------\n", df_percentiles_80.to_string(index = False), "\n----------------------------------------------------------------------------------------------------------------------------\n")
print("-Película:\n  Ordenadas alfabéticamente, en el puesto 800 se encuentra \"The Haunting in Connecticut\", esto significa que el 80% de las películas más taquilleras tiene un nombre que empieza o está por debajo de la letra \"T\"")
print("-Fin de semana:\n  El 80% de las películas más taquilleras, el primer fin de semana tienen una recaudación que está por debajo de 60,316,738$")
print("-Total:\n  El 80% de las películas más taquilleras tiene una recaudación total por debajo de 206,459,076$")
print("-% del total:\n  El 80% de las películas más taquilleras, tiene un porcentaje de los ingresos brutos totales representado por los ingresos del primer fin de semana de apertura por debajo de 39.6%")
print("-Cines:\n  El 80% de las películas más taquilleras se estrenó en menos de 3,987 cines")
print("-Promedio:\n  El 80% de las películas más taquilleras tiene un promedio de recaudación en cada cine por debajo de 16,601$")
print("-Fecha:\n  Ordenadas alfabéticamente, el 80% de las películas más taquilleras se estreno en una fecha anterior a la fecha 24-06-2009")
print("-Distribuidor:\n  Ordenadas alfabéticamente, en el puesto 800 se encuentra \"Walt Disney Studios Motion Pictures\", esto quiere decir que el 80% de las distribuidoras, tiene un nombre que empieza o está por debajo de la letra \"W\"")

#b)
print("\nb)\n\n")

numero_de_columnas = len(datos[0])
cuartiles_con_librerias = []
percentiles_con_librerias = []
for i in range(numero_de_columnas):
  valores_de_columna = [row[i] for row in datos]
  if (type(valores_de_columna[0]) != str):
    cuartil = np.quantile(valores_de_columna, 0.75)
    percentil = np.percentile(valores_de_columna, 80)
    cuartiles_con_librerias.append(cuartil)
    percentiles_con_librerias.append(percentil)

#Últimos cuartiles
matriz_ultimos_cuartiles = np.array(cuartiles_con_librerias).reshape(1, 5)
df_ultimos_cuartiles_con_librerias = pd.DataFrame(matriz_ultimos_cuartiles, columns=['Fin de semana', 'Total', '% de total', 'Cines', 'Promedio'])
print("Últimos cuartiles con librerías\n\n------------------------------------------------------------\n", df_ultimos_cuartiles_con_librerias.to_string(index = False), "\n------------------------------------------------------------\n")

#Últimos percentiles
matriz_ultimos_percentiles = np.array(percentiles_con_librerias).reshape(1, 5)
df_ultimos_percentiles_con_librerias = pd.DataFrame(matriz_ultimos_percentiles, columns=['Fin de semana', 'Total', '% de total', 'Cines', 'Promedio'])
print("Percentiles 80 con librerías\n\n------------------------------------------------------------\n", df_ultimos_percentiles_con_librerias.to_string(index = False), "\n------------------------------------------------------------\n")

#c), d)
print("\nc), d)\n\n")

import matplotlib.pyplot as plt

base_de_datos = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSHIdebxvXrtk2R2u86LNg6S-5xB5QDPFcCtq2diM3slZGkoSnk9cFp-YMaVZJayhw6cgOU1kywZanU/pub?gid=507241814&single=true&output=csv")
datos = base_de_datos.values
explicaciones = ["Media: Nos indica que dentro del top de 1000 de películas más taquilleras de la historia, la mayoría en su primer fin de semana tuvo esa recaudación.\nMediana: Nos indica que, ordenados las recaudaciones del primer fin de semana de las 1000 películas más taquilleras, ese el monto de recaudación que está en el centro de esta lista.\nModa: Nos indica el monto exacto de recaudación del primer fin de semana que se repite más veces.\nGeométrica: Nos indica la tasa de crecimiento de las recaudaciones del primer fin de semana de todas las películas.\n","Media: La mayoria de las 1000 películas más taquilleras de la historia tiene esa recaudación.\nMediana: Ordenada la lista del total de recaudaciones de las películas má taquilleras, nos indica el valor que está justo en medio de la lista.\nModa: Nos indica el valor de recaudación total que más veces se repitió.\nGeométrica: Nos indica la tasa de crecimiento en las ganancias totales que se observan en la lista.\n", "Media: Nos indica que para la mayoría de películas, ese porcentaje del primer fin de semana fue el que influyó su éxito.\nMediana: Ordenados los porcentajes, nos indica que en la lista de las películas más taquilleras, en el centro está el porcentaje que indica qué tanto le ayuda a su éxito el primer fin de semana.\nModa: El porcentaje que más veces se repite.\nGeométrica: Como suben los porcentajes en esta lista de lo que influyó el primer fin de semana en su ingreso total.\n", "Media: La mayoría de películas más taquilleras se estreno en esa cantidad de cines.\nMediana: En la lista ordenada de los cines en las que fueron estrenadas las películas, en el centro está ese valor.\Moda: Nos indica cuántas veces se repite la misma cantidad de estrenos de cine en las películas más taquilleras.\nGeométrica: Nos indica la tasa de incremento del número de cines en los que se fueron estrenando las películas más taquilleras.\n", "Media: Nos indica que dentro del promedio que cada película recaudó por cine, la mayoría recaudó esa cantidad por cine.\nMediana: Ordenada la lista del promedio de ganancias por cine de las películas, nos indica el valor que se encuentra en el centro.\nModa: Nos indica el promedio que cada película recaudó por cine, el que más se repitió fue ese valor.\nGeométrica: Nos indica la tasa de crecimiento de los promedios que recaudó cada película.\n"]

numero_de_columnas = len(datos[0])
titulos = ['Primer fin de semana', 'Total de recaudación', '% de total de recaudación', 'Cines en los que se estreno', 'Promedio de ganancias por cine']

for i in range(numero_de_columnas):
  valores_de_columna = [row[i] for row in datos]
  if (type(valores_de_columna[0]) != str):
    valores_de_columna.sort()
    media = np.mean(valores_de_columna, axis = 0)
    mediana = np.median(valores_de_columna, axis = 0)
    moda = pd.Series(np.ravel(valores_de_columna)).mode()[0]
    geometrica = np.exp(np.mean(np.log(valores_de_columna), axis = 0))
    print("---------- ", titulos[i - 1], " ----------")
    print("Media:", media)
    print("Mediana:", mediana)
    print("Moda:", moda)
    print("Geométrica:", geometrica,"\n")
    print(explicaciones[i - 1])

    #d) graficando la distribución de los datos
    plt.hist(valores_de_columna, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de los datos')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
    print("\n")

print("\n\tPrimer fin de semana:\n\t\tPara este caso, la media nos puede servir para un artículo científico, ya que nos dirá cuánto de recaudación tiene que tener une película para considerar el que está sea un éxito en taquilla y entre en el top.")
print("\n\tTotal de recaudación:\n\t\tPara este caso, la media también nos interesaria más, nos daría más información sobre las películas más taquilleras, cuál es el estándar para que una película se considere exitosa.")
print("\n\t% de total de recaudación:\n\t\tNos podría interesar la moda, cuántas veces se repitió una cantidad de recaudación en el primer fin de semana, así podríamos pronosticar qué otras películas según su primer fin de semana se postularían a ser un éxito.")
print("\n\tCines en los que se estreno:\n\t\tTambién nos interesaría más la media, en cuántos cines se debería estrenar una película para que sea un éxito (teniendo en cuenta que también existen otros factores que afectarán).")
print("\n\tPromedio de ganancias por cine:\n\t\tIgualmente nos interesaría más la media, cuánto debería generar una película por cine para que sea un éxito.")
