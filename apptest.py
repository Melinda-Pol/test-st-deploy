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
            st.image(img, width=700, caption="Sum Global_Sales (5 Years) ")
            st.write("Cómo   se observa, las plataformas: XOne, Wii y PS4 son las que han dominado el número de ventas totales en los últimos 5 años.")

    if choice == "Geografía":
        #Ventas según geografía
        st.write("¿Puedo esperar que mis ventas se repartan por igual entre las distintas geografías?")
        
        dfNA = df0[[ 'Year','NA_Sales',]]
        dfNA['label'] = 'NA'
        dfNA=dfNA.rename(columns = {'NA_Sales':'Sales'})
        
        dfPAL= df0[[ 'Year','PAL_Sales',]]
        dfPAL['label'] = 'PAL'
        dfPAL = dfPAL.rename(columns = {'PAL_Sales':'Sales'})
        
        dfJP = df0[[ 'Year','JP_Sales',]]
        dfJP['label'] = 'JP'
        dfJP = dfJP.rename(columns = {'JP_Sales':'Sales'})
        
        dfOT = df0[[ 'Year','Other_Sales',]]
        dfOT['label'] = 'OT'
        dfOT= dfOT.rename(columns = {'Other_Sales':'Sales'})
        
        dftot = pd.concat([dfNA,dfPAL,dfJP,dfOT])
        dftot = dftot[dftot['Year']> 1995]
        source = dftot.rename(columns = {'Year':'x','label':'category','Sales':'y'})
        subset_data = source
        genre_input = st.sidebar.multiselect('category',
                                             source.groupby('category').count().reset_index()['category'].tolist())
        if len(genre_input) > 0:
            subset_data = source[source['category'].isin(genre_input)]
            
        st.subheader('Ventas globales según geografía')
        totalcases = alt.Chart(subset_data).transform_filter(alt.datum.y > 0).mark_line().encode(
            x=alt.X('x', type='nominal', title='Year'),
            y=alt.Y('sum(y):Q', title='Total Sales'),
            color='category',
            tooltip = 'sum(y)',
        ).properties(
            width=800,
            height=400
        ).configure_axis(
            labelFontSize=17,
            titleFontSize=20
        )
        st.altair_chart(totalcases)
        
        st.write("Si hacemos una comparativa a lo largo de los años por zonas geográficas, podemos observar que las ventas en Norte América son las que han predominado a lo largo del tiempo, seguido de Europa. Para indagar un poco más, incluyo un análisis de los videojuegos más vendidos por cada zona geográfica")
    
        if st.checkbox("Análisis videojuegos por zonas geográficas:"):

            dfNA = df0[[ 'Year','NA_Sales','Name']]
            dfNA['label'] = 'NA'
            dfNA=dfNA.rename(columns = {'NA_Sales':'Sales'})

            dfPAL= df0[[ 'Year','PAL_Sales','Name']]
            dfPAL['label'] = 'PAL'
            dfPAL = dfPAL.rename(columns = {'PAL_Sales':'Sales'})

            dfJP = df0[[ 'Year','JP_Sales','Name']]
            dfJP['label'] = 'JP'
            dfJP = dfJP.rename(columns = {'JP_Sales':'Sales'})

            dfOT = df0[[ 'Year','Other_Sales','Name']]
            dfOT['label'] = 'OT'
            dfOT= dfOT.rename(columns = {'Other_Sales':'Sales'})

            dftot = pd.concat([dfNA,dfPAL,dfJP,dfOT])
            dftot = dftot[dftot['Year']>=2018]
            dftot = dftot[dftot['Sales']>0.30]
            source = dftot.rename(columns = {'Year':'x','label':'category','Sales':'y'})

            chartfacet = alt.Chart(source).mark_point().encode(
            alt.X('x:Q', scale=alt.Scale(zero=False)),
            y='Name:O',
            color='x:N',
            facet=alt.Facet('category:O', columns=2),
            ).properties(
            width=600,
            height=300,
            )

            st.altair_chart(chartfacet)
    if choice == "ESRB":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Acuerdo":
        st.text("Meli está en ello...en unas semanas estará disponible")
    if choice == "Conclusiones":
        st.text("Meli está en ello...en unas semanas estará disponible")
if __name__ == '__main__':
    main()
