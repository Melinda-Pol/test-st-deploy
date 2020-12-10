import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import altair as alt
from altair import Chart,X, Y, Axis, SortField, OpacityValue
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
            dfselect = df0[df0['Rank'] <= 20]
            dfselect = dfselect[dfselect['Year']>=2000]
            dfselect = dfselect[['Year','Name','Platform','Rank']]
            dfselect['Year'] = dfselect['Year'].astype('int64')
            dfselect = dfselect.sort_values(by=['Rank'])
            st.write(dfselect)
        
        if st.checkbox("En ese segundo caso, ¿en qué plataforma me debería enfocar?"):
            st.text("Reparto de ventas globales por plataforma durante los últimos 5 años:")
            img = Image.open("df1p.png")
            st.image(img, width=400, caption="Sum Global_Sales (5 Years) ")
            st.write("Cómo se observa, las plataformas: XOne, Wii y PS4 son las que han dominado el número de ventas totales en los últimos 5 años.")
        
    if choice == "Geografía":
        regions = st.selectbox(label="Selecciona una zona geográfica", options=['NA_Sales','PAL_Sales','JP_Sales'])
        if regions == 'NA_Sales':
            pass
        if regions == 'PAL_Sales':
            pass
        if regions == 'JP_Sales':
            pass
    if choice == "Género":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "ESRB":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Acuerdo":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Conclusiones":
        st.text("Meli está en ello...en unas semanas estará disponible")
if __name__ == '__main__':
    main()
