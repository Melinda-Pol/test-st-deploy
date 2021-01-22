import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import altair as alt
from altair import Chart,X, Y, Axis, SortField, OpacityValue
from PIL import Image
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
#Title
st.title("Video Game EDA")
#Options for a selectbox
section  = ["Basic EDA", "Analysis","Recommendations"]
choice = st.sidebar.selectbox("Type of analysis",section)
#Datasource
st.markdown("[Dataset: Kaggle video game sales](https://www.kaggle.com/ashaheedq/video-games-sales-2019)")
#Load dataset
df0 = pd.read_csv("vgsales-12-4-2019.csv")

def main():
    if choice == "Basic EDA":
        #Shape of df
        st.text("Shape of the dataset:")
        st.write(df0.shape)
        #Stats and general description
        st.text("General description:")
        st.write(df0.describe(include='all'))
        #Type of data
        st.text("Data types:")
        st.write(df0.dtypes)
        #Sum of nulls
        st.text("Do I have null data?")
        st.write(df0.isnull().sum())
        
        if st.button('Correlation map'):
            
            df1 = df0.drop(['VGChartz_Score', 'status','Total_Shipped'],axis=1)
            c_plot = sns.heatmap(df1.corr(),annot=True, cmap="YlGnBu")
            st.write(c_plot)
            st.pyplot()

    if choice == "Analysis":
        #Platforms on demand by year of release
        st.subheader("Top platforms based on year of release game?")
        x = st.number_input('Select ranking',min_value=1,max_value=55792)
        x1 = st.slider('Year of release of the game',1970,2020,(1970,2020))
        
        if st.button('Filter data'):
            df1 = df0[['Year','Name','Rank','Platform']]
            df1 = df1[df1['Rank']<= x]
            df1 = df1[df1['Year']>= x1[0]]
            df1 = df1[df1['Year']<= x1[1]]
            df1['Year'] = df1['Year'].astype('int64')
            df1 = df1.sort_values(by=['Rank'])
            st.write(df1)
            barplot = sns.barplot(x ="Rank",y="Platform", hue="Name",data=df1,palette="mako")
            barplot.plot(kind='bar')
            st.pyplot()
            
        #Platform analysis
        st.subheader("In wich platform should I focus on?")
        if st.button('Barchart'):
            st.write("Market global sales for the last 5 years (:")
            img = Image.open("df1p.png")
            st.image(img, width=700, caption="Sum Global_Sales (5 Years)")
            st.write("Platforms on demand: XOne, Wii and PS4.")

        #Ventas según geografía
        st.subheader("Geographie distribution")
        if st.button('Sales distribution chart'):
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
            genre_input = st.multiselect('category',
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
    
        st.subheader("Análisis videojuegos por zonas geográficas:")
        if st.button("Geo zones"):
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
            dftot = dftot[dftot['Year']>=2019]
            dftot = dftot[dftot['Sales']>0.03]
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

    if choice == "Recommendations":
        st.text("Under construction")
if __name__ == '__main__':
    main()
