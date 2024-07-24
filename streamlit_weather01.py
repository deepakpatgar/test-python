import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from meteostat import Point, Daily, Hourly
from geopy.geocoders import Nominatim

# Streamlit app title
st.title("Weather Data Analysis and Forecast")

# Input for location name
location_name = st.text_input("Enter Location (e.g., Bangalore, Kolkata)")

# Input for date range
start_date = st.date_input("Start Date", value=datetime(2023, 1, 1))
end_date = st.date_input("End Date", value=datetime(2023, 1, 31))

# Forecast duration (in days)
forecast_days = st.slider("Forecast Days", min_value=1, max_value=7, value=3)

# Fetching the weather data
if st.button("Fetch Weather Data"):
    # Get latitude and longitude from location name
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location_name)
    
    if location:
        latitude, longitude = location.latitude, location.longitude
        st.write(f"Location: {location_name} (Lat: {latitude}, Lon: {longitude})")
        
        # Define the location for Meteostat
        weather_location = Point(latitude, longitude)
        
        # Get historical daily data
        start = datetime.combine(start_date, datetime.min.time())
        end = datetime.combine(end_date, datetime.min.time())
        historical_data = Daily(weather_location, start, end)
        historical_data = historical_data.fetch()

        # Get forecast hourly data
        forecast_start = datetime.now()
        forecast_end = forecast_start + timedelta(days=forecast_days)
        forecast_data = Hourly(weather_location, forecast_start, forecast_end)
        forecast_data = forecast_data.fetch()

        # Display the historical data table
        st.write("Historical Weather Data")
        st.dataframe(historical_data)

        # Display the forecast data table
        st.write("Forecast Weather Data")
        st.dataframe(forecast_data)

        # Plot temperature for historical data
        st.write("Historical Temperature Analysis")
        plt.figure(figsize=(10, 5))
        plt.plot(historical_data.index, historical_data['tavg'], label='Avg Temp (°C)')
        plt.plot(historical_data.index, historical_data['tmin'], label='Min Temp (°C)')
        plt.plot(historical_data.index, historical_data['tmax'], label='Max Temp (°C)')
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Historical Temperature Over Time')
        st.pyplot(plt)

        # Plot precipitation for historical data
        st.write("Historical Precipitation Analysis")
        plt.figure(figsize=(10, 5))
        plt.plot(historical_data.index, historical_data['prcp'], label='Precipitation (mm)', color='blue')
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Precipitation (mm)')
        plt.title('Historical Precipitation Over Time')
        st.pyplot(plt)

        # Plot humidity for historical data (if available)
        if 'rhum' in historical_data.columns:
            st.write("Historical Humidity Analysis")
            plt.figure(figsize=(10, 5))
            plt.plot(historical_data.index, historical_data['rhum'], label='Humidity (%)', color='green')
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel('Humidity (%)')
            plt.title('Historical Humidity Over Time')
            st.pyplot(plt)
        else:
            st.write("Humidity data not available for this location and date range.")

        # Plot wind speed for historical data (if available)
        if 'wspd' in historical_data.columns:
            st.write("Historical Wind Speed Analysis")
            plt.figure(figsize=(10, 5))
            plt.plot(historical_data.index, historical_data['wspd'], label='Wind Speed (km/h)', color='orange')
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel('Wind Speed (km/h)')
            plt.title('Historical Wind Speed Over Time')
            st.pyplot(plt)
        else:
            st.write("Wind speed data not available for this location and date range.")

        # Plot temperature for forecast data
        st.write("Forecast Temperature Analysis")
        plt.figure(figsize=(10, 5))
        plt.plot(forecast_data.index, forecast_data['temp'], label='Temp (°C)')
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Forecast Temperature Over Time')
        st.pyplot(plt)

        # Plot precipitation for forecast data
        st.write("Forecast Precipitation Analysis")
        plt.figure(figsize=(10, 5))
        plt.plot(forecast_data.index, forecast_data['prcp'], label='Precipitation (mm)', color='blue')
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Precipitation (mm)')
        plt.title('Forecast Precipitation Over Time')
        st.pyplot(plt)

        # Plot humidity for forecast data (if available)
        if 'rhum' in forecast_data.columns:
            st.write("Forecast Humidity Analysis")
            plt.figure(figsize=(10, 5))
            plt.plot(forecast_data.index, forecast_data['rhum'], label='Humidity (%)', color='green')
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel('Humidity (%)')
            plt.title('Forecast Humidity Over Time')
            st.pyplot(plt)
        else:
            st.write("Humidity forecast data not available for this location and date range.")

        # Plot wind speed for forecast data (if available)
        if 'wspd' in forecast_data.columns:
            st.write("Forecast Wind Speed Analysis")
            plt.figure(figsize=(10, 5))
            plt.plot(forecast_data.index, forecast_data['wspd'], label='Wind Speed (km/h)', color='orange')
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel('Wind Speed (km/h)')
            plt.title('Forecast Wind Speed Over Time')
            st.pyplot(plt)
        else:
            st.write("Wind speed forecast data not available for this location and date range.")

        # Additional visualizations using Plotly for interactive charts
        st.write("Interactive Historical Temperature Analysis")
        fig = px.line(historical_data.reset_index(), x='time', y=['tavg', 'tmin', 'tmax'],
                      labels={'value': 'Temperature (°C)', 'time': 'Date'},
                      title='Historical Temperature Over Time')
        st.plotly_chart(fig)

        st.write("Interactive Forecast Temperature Analysis")
        fig = px.line(forecast_data.reset_index(), x='time', y='temp',
                      labels={'temp': 'Temperature (°C)', 'time': 'Date'},
                      title='Forecast Temperature Over Time')
        st.plotly_chart(fig)

        st.write("Interactive Historical Precipitation Analysis")
        fig = px.bar(historical_data.reset_index(), x='time', y='prcp',
                      labels={'prcp': 'Precipitation (mm)', 'time': 'Date'},
                      title='Historical Precipitation Over Time')
        st.plotly_chart(fig)

        st.write("Interactive Forecast Precipitation Analysis")
        fig = px.bar(forecast_data.reset_index(), x='time', y='prcp',
                      labels={'prcp': 'Precipitation (mm)', 'time': 'Date'},
                      title='Forecast Precipitation Over Time')
        st.plotly_chart(fig)

        # Comparison of historical and forecast temperature
        st.write("Comparison of Historical and Forecast Temperature")
        combined_temp = pd.concat([
            historical_data[['tavg', 'tmin', 'tmax']].rename(columns={'tavg': 'Average Temp', 'tmin': 'Min Temp', 'tmax': 'Max Temp'}),
            forecast_data[['temp']].rename(columns={'temp': 'Forecast Temp'})
        ])
        fig = px.line(combined_temp.reset_index(), x='time', y=combined_temp.columns,
                      labels={'value': 'Temperature (°C)', 'time': 'Date'},
                      title='Comparison of Historical and Forecast Temperature Over Time')
        st.plotly_chart(fig)
    else:
        st.write("Location not found. Please enter a valid location name.")




