import streamlit as st
import requests
#import pandas as pd

'''
# WagonCab TaxiFareModel By Conor
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#Taking user inputs and constructing params dictionary

date_input = st.date_input("Enter in a date", value="today")
pickup_time = st.time_input("Enter in a time", value="now")

date_time = f"{date_input} {pickup_time}"

pup_lon_input =st.number_input("Pickup lon", min_value=None, max_value=None, value=73.985, step=None, format=None, key=None, help=None, on_change=None,placeholder=None, disabled=False, label_visibility="visible")
pup_lat_input = st.number_input("Pickup lat", min_value=None, max_value=None, value=40.7484, step=None, format=None, key=None, help=None, on_change=None,placeholder=None, disabled=False, label_visibility="visible")

droff_lon_input =st.number_input("Drop off lon", min_value=None, max_value=None, value=73.9262, step=None, format=None, key=None, help=None, on_change=None,placeholder=None, disabled=False, label_visibility="visible")
droff_lat_input = st.number_input("Drop off lat", min_value=None, max_value=None, value=40.8296, step=None, format=None, key=None, help=None, on_change=None,placeholder=None, disabled=False, label_visibility="visible")

passenger_count = st.number_input("Number of passengers", min_value=None, max_value=None, value=1, step=None, format=None, key=None, help=None, on_change=None,placeholder=None, disabled=False, label_visibility="visible")

input_params = {"pickup_datetime": date_time,
          "pickup_longitude": pup_lon_input,
          "pickup_latitude": pup_lat_input,
          "dropoff_longitude": droff_lon_input,
          "dropoff_latitude": droff_lat_input,
          "passenger_count": passenger_count}

##map_df = pd.DataFrame({"lat": pup_lat_input, "lon": pup_lon_input})

#map = st.map(map_df, color='#ffaa0088')

#Calling API and handling response object
response = requests.get(url, params=input_params)

json_response = response.json()

print(json_response)

fare =json_response['fare']

#retrieving prediction and displaying in frontend
st.metric("Estimated Fare", value=f"${round(fare,2)}")
