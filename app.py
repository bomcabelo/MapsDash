# Construindo relatórios e dashboard para Data Science em Python

# Importando os módulos:
import streamlit as st
import matplotlib
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image
import folium
from folium import plugins

# Adicionando um titulo
st.title('Construindo Relatórios para Data Science com Streamlit')

# importando conjunto de dados
contratos = df = pd.read_csv("data-1619262085828.csv")

# Visualizando os dados
st.markdown('### __Base de dados:  Contratos em Andamento__ ')
st.dataframe(contratos)
st.markdown('---')

# Extraindo as coordenadas de 18000 registros:
coordenadas=[]
for lat,lng in zip(df.lat_documento.values[:18000],df.long_documento.values[:18000]):
  coordenadas.append([lat,lng])

# Renderizando o mapa com algumas personalizações:
mapa = folium.Map(location=[-15.788497,-47.879873],zoom_start=11)

# Visualização Gráfica
st.title('Visualização Gráfica')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Adicionando os registros no mapa de calor:
#fig = mapa.add_child(plugins.HeatMap(coordenadas))        
#st.plotly_chart(fig)

# Fim





