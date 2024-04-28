import csv
import streamlit as st
from streamlit.components.v1 import html
import altair as alt
from streamlit_modal import Modal
import requests
import json
from types import SimpleNamespace

my_list = []

with open('output.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        my_list.append(row)
locations = my_list[0]


def app () :
    st.title("Price prediction")
    st.write("Please fill all of the fields below in order to predict the apartment price in Germany:")
    estimated_price = 0
    
    alt.themes.enable("dark")
    
    # Form
    
    area = st.text_input("Area (m"+'\u00B2'+")")
    room = st.text_input("Number of rooms (include kitchen, living room, toilet, etc)")
    extra_cost = st.text_input("Additional cost (Warmiete und Kaltmiete)")
    flat_type = st.selectbox("Apartment type", ('ground_floor', 'apartment', 'roof_storey', 'raised_ground_floor', 'terraced_flat', 'half_basement', 'maisonette', 'other', 'loft','penthouse'))
    heating_type = st.selectbox("Heating type", ('central_heating', 'self_contained_central_heating', 'oil_heating', 'district_heating', 'floor_heating', 'gas_heating', 'electric_heating', 'combined_heat_and_power_plant', 'heat_pump', 'wood_pellet_heating', 'night_storage_heater', 'stove_heating', 'solar_heating'))
    condition = st.selectbox("Room condition", ('well_kept', 'refurbished', 'fully_renovated', 'Other', 'mint_condition', 'first_time_use_after_refurbishment', 'first_time_use', 'modernized'))
    location = st.selectbox("Location", options=locations)
    
    # Send data to fastApi URL
    # Define the URL of your FastAPI endpoint
    url = 'https://noorprajuda-german-apartment-rent-server.hf.space/predict'

    # Define the JSON data to send in the request body
    data = {
        "livingSpace": f"{area}",
        "noRooms": f"{room}",
        "additionCost" : f"{extra_cost}",
        "heating_type" : f"{heating_type}",
        "condition" : f"{condition}",
        "typeOfFlat" : f"{flat_type}",
        "regio2" : f"{location}"
    }

    
    # Modal
    modal = Modal(
        "Result",
        key="modal",
    )
    
    open_modal = st.button("Predict price")
    
    if open_modal:

        # Convert the data to JSON format
        json_data = json.dumps(data)

        # Set the headers to indicate that the request body is JSON
        headers = {'Content-Type': 'application/json'}

        # Send the POST request with the JSON data
        response = requests.post(url, data=json_data, headers=headers)
        
        response = str(response.json()).replace("\'", "\"")

        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))

        estimated_price = response.estimated_price
        
        with modal.container():
            st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 40px; color: lightgreen;'>€ {estimated_price}</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: white;'>The price prediction is based on dataset with machine learning using XGBoost model</p>", unsafe_allow_html=True)
        