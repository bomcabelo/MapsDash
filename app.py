# Construindo relatórios e dashboard para Data Science em Python

# Importando os módulos:
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import folium
from folium import plugins
from PIL import Image

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

# Adicionando os registros no mapa de calor:
mapa.add_child(plugins.HeatMap(coordenadas))        
mapa

# Fim





