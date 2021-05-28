# Construindo relatórios e dashboard para Data Science em Python

# importando as bibliotecas
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image

# Adicionando um titulo
st.title('Construindo Relatórios para Data Science com Streamlit')

# importando conjunto de dados
contratos = pd.read_csv('/dados/data-1622225673337.csv')

contratos.head()


# Fim





