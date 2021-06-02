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

df_sus = pd.read_csv('https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-19-10-2020.csv',
                     sep=';',
                     encoding='iso-8859-1',
                     error_bad_lines=False
                    )

# importando conjunto de dados
#contratos = df = pd.read_csv("data-1619262085828.csv")

# Visualizando os dados
st.markdown('### __Base de dados:  Contratos em Andamento__ ')
st.dataframe(df_sus)
st.markdown('---')

mapa = folium.Map(location=[-15.788497,-47.879873])
st.plotly_chart(mapa)

# Fim
