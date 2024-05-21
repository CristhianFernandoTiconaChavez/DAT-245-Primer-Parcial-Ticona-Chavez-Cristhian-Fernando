import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTGqtuFpx0oxDbdwe7t3AiXNZQiTaVg4FRTeAHcUfF5cu_HL7dJs_IVViORDz7z-Kc2EzNwduH4xUa5/pub?output=csv'
datos = pd.read_csv(url)

"""
1. OneHotEncoder
  Nos sirve para pasar las variables "categóricas" a variables "binarias".
  Esto ya que algunos algoritmos de aprendizaje automático funcionan mejor con datos numéricos.
"""
ohe = OneHotEncoder(sparse=False)
categoria_codificado = ohe.fit_transform(datos[['Release']])
categoria_codificado_df = pd.DataFrame(categoria_codificado, columns=ohe.get_feature_names_out(['Release']))
datos = datos.join(categoria_codificado_df).drop('Release', axis=1)

"""
2. StandardScaler
  Este preprocesamiento escalar, nos ayuda escalando los datos de una columna para que tengan media de 0 y desviación estándar de 1, es útil cuando los datos se distribuyen normalmente.
  En nuestro caso nos sirve ya que nuestros datos de la columna "% of Total" se asemejan a una distribución Normal, esto nos ayudará después para mejores interpretaciones de los datos.
"""
ss = StandardScaler()
datos['% de Total Estandarizada'] = ss.fit_transform(datos[['% of Total']])

"""
3. SimpleImputer
  Rellena valores faltantes basandose en la media, mediana o la moda, ls valores faltantes pueden introducir sesgos y problemas en los modelos de aprendizaje automático, este preprocesamiento escalar nos ayuda a mantener la integridad del dataset.
  En nuestro dataset por ejemplo, si de una película se desconociera sus Distribuidora, escalarla de esta manera nos daría por ejemplo la Distribuidora que se repite más veces, ese valor sería el que se rellenaría en nuestro dataset.
"""
si = SimpleImputer(strategy='mean')
datos['Total Gross escalado'] = si.fit_transform(datos[['Total Gross']])

from google.colab import drive
drive.mount('/content/drive')
datos.to_csv('/content/drive/My Drive/dataset_preprocesado1.csv', index=False)