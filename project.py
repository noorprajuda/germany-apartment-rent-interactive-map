import streamlit as st
from streamlit.components.v1 import html
import altair as alt
from streamlit_modal import Modal

def app () :
        
        st.title("About this project")
        st.write('**What is this project for?**')
        st.write('''
                        This project was created as a mandatory final project to fulfill the graduation requirement from DTSENSE. 
                        In this application, the user can get the estimated price of Apartment based on the dataset using machine learning 
                        XGBoost.''')
        
        st.write('**For whom this project?**')
        st.write('''This project is for:
                    1. The lecturer in DTSENSE
                    2. Those who is living in Germany
                    3. The people who will fly to Germany
                    4. Those who is curious with apartment rental price in germany
                    5. Machine learning scientist or data scientist who want to study this project
                    
                 ''')
        
        st.write('**Why I choose this dataset?**')
        st.write('''I hope this project can be useful for one who is looking for an apartment in Germany. 
                    There are many peple who will go to Germany, wether they want to study, work, or just living in Germany.
                    Finding a good place to be lived is important to them''')
        
        
        st.write('**When I collected the data?**')
        st.write('I accessed the dataset in April 2024.')
        