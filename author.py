import streamlit as st
from streamlit.components.v1 import html
import altair as alt
from streamlit_modal import Modal

def app () :
        
        st.title("Author Profile")
        
        st.image(
            "https://avatars.githubusercontent.com/u/22234154?s=400&u=a9fd78dd9da713ff8dbaca3375e9d9f0079c9155&v=4",
            width=200, # Manually Adjust the width of the image as per requirement
        )
        
        st.write('''
                        Hello world! 
                        Thank you for visiting this website application 🙏. My name is Marsetio Noorprajuda.  
                        I am a machine learning scientist with a fullstack developer background.
                        I graduated from DataCamp, FreeCodeCamp, and DTSense Bootcamps.
                        There I learned data science and machine learning with Python programming language.
                        I also graduated from Hacktiv8 Indonesia Bootcamp. 
                        So I have extensive experiences both in backend and frontend using JavaScript technologies (such as Angular, React, Vue, ionic) too.
                        You can check in my [LinkedIn profile](https://www.linkedin.com/in/marsetio-noorprajuda-5633401b9/).
                        If you are interested in my other projects, you can simply visit my [Github profile](https://github.com/noorprajuda).''')
        st.write('Thank you very much!')
        st.write('''
                created on Sunday, 28th April 2024 © Marsetio Noorprajuda.
                ''')