import streamlit as st
import requests
from datetime import datetime

st.title("Taxi Fare Prediction")


st.header("Input Ride parameters")

#input parameter
pickup_date = st.date_input(
    "Pickup Date",
    value=datetime.today())

pickup_time = st.time_input(
    "Pickup Time",
    value=datetime.now().time())

pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input(
    "Pickup Longitude", value=-73.950655)

pickup_latitude = st.number_input(
    "Pickup latitude", value=40.783282)

dropoff_longitude = st.number_input(
    "Dropoff Longitude", value=-73.984365)

dropoff_latitude = st.number_input(
    "Dropoff Latitude", value=40.769802)

passenger_count = st.number_input(
    "Number of passenger", min_value=1, max_value=8, value=1)


#API paraemter dictionary

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

#API Call
url = 'https://taxifare.lewagon.ai/predict'
if st.button("Get Fare Prediction"):
    respond = requests.get(url, params=params)
    if respond.status_code == 200:
        prediction = respond.json()["fare"]
        st.success(f"Predicted Fare: ${prediction:.2f}")
    else:
        st.error("Failed to retrive prediction from API")
