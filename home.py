import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import altair as alt
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image 
import seaborn as sns
import plotly.express as px
from streamlit_folium import folium_static

def app () :
    df = pd.read_excel("./immo_data_clean.xlsx")
    df["price/m2"] = round(df["price/m2"], 2)
    main_variable = ['totalRent', 'price/m2']
    selected_variable = "totalRent"
    maps_data_final = gpd.read_file("./maps/immo_data_merge_geopandas.shp")
    color_theme_list = ['default','cividis', 'inferno', 'magma', 'plasma', 'rainbow', 'turbo']
    
    geo_json_data = r'maps_data_final.geojson'
    
    column_name = "Total rent"
    
    alt.themes.enable("dark")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # CSS styling
    st.markdown("""
    <style>

    .tooltip {
    position: relative;
    display: inline-block;
    cursor: pointer;
    }

    .tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: white;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    top: 100%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
    cursor: pointer;
    }

    .element-class:hover {
    cursor: pointer;
    }

    [data-testid="block-container"] {
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin-bottom: -7rem;
    }

    [data-testid="stVerticalBlock"] {
        padding-left: 0rem;
        padding-right: 0rem;
    }

    [data-testid="stMetric"] {
        background-color: #393939;
        text-align: center;
        padding: 15px 0;
    }

    [data-testid="stMetricLabel"] {
    display: flex;
    justify-content: center;
    align-items: center;
    }

    [data-testid="stMetricDeltaIcon-Up"] {
        position: relative;
        left: 38%;
        -webkit-transform: translateX(-50%);
        -ms-transform: translateX(-50%);
        transform: translateX(-50%);
    }

    [data-testid="stMetricDeltaIcon-Down"] {
        position: relative;
        left: 38%;
        -webkit-transform: translateX(-50%);
        -ms-transform: translateX(-50%);
        transform: translateX(-50%);
    }

    </style>
    """, unsafe_allow_html=True)
    
    def color_selector(input_color_theme):
        if input_color_theme == "default" :
            input_color_theme = None
            return input_color_theme
        elif input_color_theme not in color_theme_list :
            input_color_theme = None
            return input_color_theme
    

    def make_choropleth(input_color_theme, selected_variable) :        
        if input_color_theme == "default" :
            input_color_theme = None    
        elif input_color_theme not in color_theme_list :
            input_color_theme = None
            
        missing_value_color = '#cccccc' # Light grey
        
        if selected_variable == "price/m2":
            display_map = maps_data_final.explore(column="price/m2", 
                tooltip=["note", "price/m2"], 
                popup=True, 
                tiles="CartoDB positron",
                legend=True,
                legend_kwds=dict(textColor="white"), 
                cmap=input_color_theme,
                scheme="naturalbreaks",
                k=20,
                edgecolor = "0",
                zoom_start=5,
                missing_kwds={"color": missing_value_color, "label": "Missing values"})
          
        
            return display_map  
        else :
                display_map = maps_data_final.explore(column="avg_rent", 
                    tooltip=["note", "avg_rent"],  
                    popup=True, 
                    tiles="CartoDB positron",
                    legend=True,
                    legend_kwds=dict(textColor="white"), 
                    cmap=input_color_theme,
                    scheme="naturalbreaks",
                    k=20,
                    edgecolor = "0",
                    zoom_start=5,
                    missing_kwds={"color": missing_value_color, "label": "Missing values"})
            
                return display_map  

            
    # Main Dashboard 
    col_select_1, col_select_2 = st.columns((5, 5), gap='small')
    col1, col2 = st.columns((5, 5), gap='small')
    col3, col4 = st.columns((6, 4), gap='small')
    
    with col_select_1:
        # Select box
        selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    
    with col_select_2:
        # Select box
        selected_variable = st.selectbox('Select a variable', main_variable)

    with col1:
        column_title = "Total Rent"
        
        if selected_variable == "price/m2":
            column_title = "Price/m" + '\u00B2' 
        else :
            column_title = "Total Rent"
        
        # Top banner
        st.markdown(f'#### {column_title} Median Price GeoData')
        
        # Map
        st.markdown(f"""
                    <style>
                    iframe {{
                        width: inherit;
                    }}
                    </style>
                    """, unsafe_allow_html=True)
        germany_map = make_choropleth(selected_color_theme, selected_variable)
        
        folium_static(germany_map)

    with col2:        
        column_title = "Total Rent"
        
        if selected_variable == "price/m2":
            column_title = "Price/m" + '\u00B2' 
        else :
            column_title = "Total Rent"
                
        st.markdown(f'#### {column_title} boxplot')
        
        # totalRent or price/m2
        selected_dtick = 100
        
        if selected_variable == "price/m2":
            selected_dtick = 1
            
        median_marker = df[selected_variable].mean()
        fig_box = px.box(df.sort_values(by=selected_variable+"Median", ascending=False), x=selected_variable, y="regio2", color='regio2', height=510)
        fig_box.add_vline(x=median_marker, line_width=2, line_dash="dash", line_color="red")
        fig_box.update_xaxes(tickangle=-90, dtick=selected_dtick)
        st.plotly_chart(fig_box, use_container_width=True)
        
    with col3:
        column_title = "Total Rent"
        
        if selected_variable == "price/m2":
            column_title = "Price/m" + '\u00B2' 
        else :
            column_title = "Total Rent"
                
        st.markdown(f'#### {column_title} & Living space correlation')
        
        # Scaterplot
        fig_scatter = px.scatter(df, x=selected_variable, y="livingSpace", color="regio2")
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col4:        
        # Rank Top Cities
        st.markdown('#### Top Cities')
        
        if selected_variable == "price/m2":
            column_name = "Price/m" + '\u00B2' + " Median"
        else :
            column_name = "Total Rent" + " Median"
        
        df_sorted = df.sort_values(by=selected_variable+"Median", ascending=False)
        df_top_cities = []
        df_top_cities = pd.DataFrame(df_top_cities)
        df_top_cities["regio2"] = df_sorted["regio2"]
        df_top_cities["totalRentMedian"] = df_sorted["totalRentMedian"]
        df_top_cities["price/m2Median"] = df_sorted["price/m2Median"]
        df_top_cities["price/m2Median"] = df_top_cities["price/m2Median"].apply(lambda x: round(x, 2))
        df_top_cities = df_top_cities.drop_duplicates()
        
        st.dataframe(df_top_cities,
                    column_order=("regio2", selected_variable+"Median"),
                    hide_index=True,
                    width=None,
                    column_config={
                        "regio2": st.column_config.TextColumn(
                            "Region",
                        ),
                        selected_variable+"Median": st.column_config.ProgressColumn(
                            column_name,
                            format="%f",
                            min_value=0,
                            max_value=max(df_sorted[selected_variable+"Median"]),
                        )}
                    )
        