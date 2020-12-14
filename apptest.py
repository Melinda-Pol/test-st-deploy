import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import altair as alt
from altair import Chart,X, Y, Axis, SortField, OpacityValue
from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Video Game EDA")
activity = ["Basico EDA", "Multiplataforma","Geografía","Género","ESRB","Acuerdo","Conclusiones"]
choice = st.sidebar.selectbox("Tipo de análisis",activity)
st.markdown("[Fuente: Kaggle video game sales](https://www.kaggle.com/ashaheedq/video-games-sales-2019)")
#Dataset Kaggle
df0 = pd.read_csv("vgsales-12-4-2019.csv")

def main():
    if choice == "Basico EDA":
        st.title('Análisis básico')
        st.text("¿Tamaño del dataset?")
        st.write(df0.shape)
        st.text("5 primeras filas:")
        st.write(df0.head(5))
        st.text("Descripción general:")
        st.write(df0.describe(include='all'))
        st.text("¿Qué tipo de datos tengo?")
        st.write(df0.dtypes)
        st.text("¿Datos nulos?:")
        st.write(df0.isnull().sum())

    if choice == "Multiplataforma":
        
        if st.checkbox("¿Debo desarrollar juegos multiplataforma?¿O enfocarme sólo en una plataforma?"):
            
            st.text("Según ranking de ventas totales")
            df1 = df0[df0['Rank'] <= 20]
            df1 = df1[df1['Year']>=2000]
            df1 = df1[['Year','Name','Platform','Rank']]
            df1['Year'] = df1['Year'].astype('int64')
            df1 = df1.sort_values(by=['Rank'])
            st.write(df1)
        
        if st.checkbox("En ese segundo caso, ¿en qué plataforma me debería enfocar?"):
            st.write("Reparto de ventas globales por plataforma durante los últimos 5 años:")
            img = Image.open("df1p.png")
            st.image(img, width=600, caption="Sum Global_Sales (5 Years) ")
            st.write("Cómo   se observa, las plataformas: XOne, Wii y PS4 son las que han dominado el número de ventas totales en los últimos 5 años.")
        if st.checkbox("Ranking de juegos según plataformas"):
            st.write("En construcción")
    if choice == "Geografía":
        st.write("¿Puedo esperar que mis ventas se repartan por igual entre las distintas geografías?")
        regions = st.selectbox(label="Selecciona una zona geográfica", options=['Global_Sales','NA_Sales','PAL_Sales','JP_Sales','Other_Sales'])
        if regions == 'Global_Sales':
            pass
        if regions == 'NA_Sales':
            st.write("Distribución de videojuegos en Norte América")
        if regions == 'PAL_Sales':
            st.write("Distribución de videojuegos en Europa")
        if regions == 'JP_Sales':
            st.write("Distribución de videojuegos en Japón")
        if regions == 'Other_Sales':
            st.write("Distribución de videojuegos en Otros Países")
        
         
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "ESRB":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Acuerdo":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Conclusiones":
        st.text("Meli está en ello...en unas semanas estará disponible")
if __name__ == '__main__':
    main()
