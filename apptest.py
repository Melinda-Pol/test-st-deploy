import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime
import time
from altair import Chart,X, Y, Axis, SortField, OpacityValue

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
        subset_data = df0
        genre_input = st.sidebar.multiselect('Genre',
                                             df0.groupby('Platform').count().reset_index()['Platform'].tolist())
        if len(genre_input) > 0:
            subset_data = df0[df0['Platform'].isin(genre_input)]
        st.subheader('Plataforma según ventas globales')
        totalcases = alt.Chart(subset_data).transform_filter(alt.datum.Global_Sales > 0).mark_line().encode(
            x=alt.X('Year', type='nominal', title='Year'),
            y=alt.Y('sum(Global_Sales):Q', title='Global Sales'),
            color='Genre',
            tooltip='sum(Global_Sales)',
        ).properties(
            width=1500,
            height=600
        ).configure_axis(
            labelFontSize=17,
            titleFontSize=20
        )
        st.altair_chart(totalcases)

    if choice == "Geografía":
        regions = st.selectbox(label="Selecciona una zona geográfica", options=['NA_Sales','PAL_Sales','JP_Sales'])
        fig = go.figure
        if regions == 'NA_Sales':
            fig.add_trace(go.Scatter(x=df0.Year,y=df0.NA_Sales, mode='lines',name='NA_Sales'))
        if regions == 'PAL_Sales':
            fig.add_trace(go.Scatter(x=df0.Year, y=df0.NA_Sales, mode='lines', name='PAL_Sales'))
        if regions == 'JP_Sales':
            fig.add_trace(go.Scatter(x=df0.Year, y=df0.NA_Sales, mode='lines', name='JP_Sales'))
    if choice == "Género":
        pass
    if choice == "ESRB":
        pass
    if choice == "Acuerdo":
        pass

if __name__ == '__main__':
    main()
