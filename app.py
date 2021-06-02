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
