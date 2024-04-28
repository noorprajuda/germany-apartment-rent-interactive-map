import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import home, predict, data, author, project

st.set_page_config(
        page_title="German Apartment Rent", layout="wide"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
            
        # Sidebar
        with st.sidebar:
            st.title('Germany apartments rent')
            app = option_menu(
                menu_title=None,
                menu_icon=None,
                options=["Main Dashboard", "Predict", "About the data", "About this project", "Author"],
                icons=["speedometer", "currency-euro", "clipboard-data", "info-circle", "person-lines-fill"],        
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "darkgreen"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                    }
            )

        
        if app == "Main Dashboard":
            home.app()            
        if app == "Predict":
            predict.app()   
        if app == "About the data":
            data.app()  
        if app == "About this project":
            project.app()  
        if app == "Author":
            author.app()   
      
             
          
             
    run()            
         