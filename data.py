import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app () :
    st.title("**Dataframe**")
    
    df = pd.read_excel("./immo_data_clean.xlsx")
    st.dataframe(df)
    st.write('''**Source**: [Kaggle dataset](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany)''')
    
    st.write('''**Data distributions**''')
    
    col = st.columns(2)

    with col[0]:
    
        fig_totalRent_distribution,ax = plt.subplots(figsize=(10,6))
        sns.histplot(
            df['totalRent'], kde=True,
            stat="density", kde_kws=dict(cut=3),
            color="red", ec="darkred"
        )
        ax.set_xlabel("Rent per month (include base rent, service charge, heating cost) in Euro", color="white")
        ax.set_ylabel(f"Density",  color="white")
        plt.title('Data distribution of monthly rent',  color="white", loc="center")
        st.plotly_chart(fig_totalRent_distribution, use_container_width=True)
        
        
    with col[1]:
        fig_price_per_m2_distribution,ax = plt.subplots(figsize=(10,6))
        sns.histplot(
            df['livingSpace'], kde=True,
            stat="density", kde_kws=dict(cut=3),
            color="green", ec="darkgreen"
        )
        ax.set_xlabel(f"Living space area in m" + '\u00B2',  color="white")
        ax.set_ylabel(f"Density",  color="white")
        plt.title('Data distribution of living space area',  color="white", loc="center")
        st.plotly_chart(fig_price_per_m2_distribution, use_container_width=True)
        
    st.write('''**Data cleaning**''')
    st.write('Regio2 selected from 16 capital cities of the 16 Germany Federal States (Bundesland) to represent all of region in Germany plus big cities (Köln, Frankfurt am Main, Freiburg im Breisgau, Dortmund, Essen, Leipzig, Bonn, Nürnbergm Mannheim) to minimize totalRent bias in "Other" region')
    st.write('Further data cleaning processes can be found [here](https://github.com/noorprajuda/german-apartment-rent)')
        
