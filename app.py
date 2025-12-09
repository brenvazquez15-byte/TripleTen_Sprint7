import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos del archivo CSV
df = pd.read_csv('vehicles_us.csv')