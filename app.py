# Construindo relatórios e dashboard para Data Science em Python

# Importando os módulos:
import streamlit_gchart as gchart
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
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

cat_data = [
    ['Phrases'],
    ['cats are better than dogs'],
    ['cats eat kibble'],
    ['cats are better than hamsters'],
    ['cats are awesome'],
    ['cats are people too'],
    ['cats eat mice'],
    ['cats meowing'],
    ['cats in the cradle'],
    ['cats eat mice'],
    ['cats in the cradle lyrics'],
    ['cats eat kibble'],
    ['cats for adoption'],
    ['cats are family'],
    ['cats eat mice'],
    ['cats are better than kittens'],
    ['cats are evil'],
    ['cats are weird'],
    ['cats eat mice']
]
    
gchart.gchart(key="cat_chart", data=cat_data, chartType="WordTree", 
    width=600, height=400, wordtree={"format": "implicit", "word": "cats"}


# Adicionando os registros no mapa de calor:
# fig = mapa.add_child(plugins.HeatMap(coordenadas))        
# st.plotly_chart(fig)

# Fim