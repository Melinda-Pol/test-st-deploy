import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

st.title("Video Game EDA")
activity = ["Basico EDA", "Multiplataforma","Geografía","Género","ESRB","Acuerdo"]
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
        fig1 = px.pie(df0, values=df0.Global_Sales,names=df0.Platform,color=df0.Platform)
        fig1.update_layout(title="<b>Sales pecentage between platforms</b>")
        st.plotly_chart(fig1)
    if choice == "Geografía":
        pass
    if choice == "Género":
        pass
    if choice == "ESRB":
        pass
    if choice == "Acuerdo":
        pass

if __name__ == '__main__':
    main()
