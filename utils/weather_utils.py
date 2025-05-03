import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.express as px

def get_weather(location, days=5):
    """Get weather forecast for a location"""
    try:
        
        api_key = "YOUR_API_KEY"  
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no"
        
        response = requests.get(url, timeout=10)  
        if response.status_code != 200:
            st.error(f"Weather API error: {response.status_code} - {response.text}")
            return None
            
        data = response.json()
        
        
        if 'error' in data:
            st.error(f"Weather API error: {data['error']['message']}")
            return None
            
        
        required_keys = ['current', 'forecast', 'location']
        for key in required_keys:
            if key not in data:
                st.error(f"Weather data missing '{key}' information")
                return None
                
        return data
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def display_weather_widget(location, days=5):
    """Display weather forecast widget"""
    if not location:
        st.info("Enter a destination to see weather forecast")
        return
        
    with st.spinner(f"Fetching weather data for {location}..."):
        weather_data = get_weather(location, days)
        
    if weather_data:
        try:
            
            if 'current' not in weather_data or 'forecast' not in weather_data or 'location' not in weather_data:
                st.error("Weather data is incomplete")
                return
                
            
            current = weather_data['current']
            forecast = weather_data['forecast']['forecastday']
            location_data = weather_data['location']
            
            st.subheader(f"🌤️ Weather in {location_data['name']}, {location_data['country']}")
            
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if 'condition' in current and 'icon' in current['condition']:
                    st.image(f"https:{current['condition']['icon']}", width=100)
                    st.markdown(f"**{current['condition']['text']}**")
                else:
                    st.write("Weather condition information unavailable")
            
            with col2:
                st.markdown(f"**Temperature:** {current.get('temp_c', 'N/A')}°C / {current.get('temp_f', 'N/A')}°F")
                st.markdown(f"**Feels like:** {current.get('feelslike_c', 'N/A')}°C / {current.get('feelslike_f', 'N/A')}°F")
                st.markdown(f"**Humidity:** {current.get('humidity', 'N/A')}%")
                st.markdown(f"**Wind:** {current.get('wind_kph', 'N/A')} km/h")
            
            
            if forecast and len(forecast) > 0:
                
                st.subheader("📅 Forecast")
                
                
                forecast_data = []
                for day in forecast:
                    try:
                        date = datetime.strptime(day['date'], '%Y-%m-%d').strftime('%a, %b %d')
                        forecast_data.append({
                            "Date": date,
                            "Max": day['day']['maxtemp_c'],
                            "Min": day['day']['mintemp_c'],
                            "Condition": day['day']['condition']['text'],
                            "Icon": day['day']['condition']['icon']
                        })
                    except KeyError as e:
                        st.warning(f"Missing data for forecast day: {e}")
                        continue
                
                if forecast_data:
                    
                    df = pd.DataFrame(forecast_data)
                    
                    
                    fig = px.line(df, x="Date", y=["Max", "Min"], 
                                title="Temperature Forecast",
                                labels={"value": "Temperature (°C)", "variable": ""},
                                color_discrete_map={"Max": "#FF9800", "Min": "#2196F3"})
                    st.plotly_chart(fig)
                    
                    
                    for i, day in enumerate(forecast_data):
                        if i < len(forecast):  
                            with st.container():
                                cols = st.columns([1, 3, 2])
                                with cols[0]:
                                    st.image(f"https:{forecast[i]['day']['condition']['icon']}", width=50)
                                with cols[1]:
                                    st.write(f"**{day['Date']}:** {forecast[i]['day']['condition']['text']}")
                                with cols[2]:
                                    st.write(f"**{forecast[i]['day']['maxtemp_c']}°C** / {forecast[i]['day']['mintemp_c']}°C")
                
                # Weather tips
                if 'condition' in current:
                    st.info(f"💡 **Travel Tip:** {get_weather_tip(current['condition'].get('text', ''), current.get('temp_c', 20))}")
            else:
                st.info("Forecast data unavailable")
            
        except Exception as e:
            st.error(f"Error processing weather data: {e}")
            import traceback
            st.error(traceback.format_exc())
    else:
        st.warning(f"Could not find weather data for {location}")

def get_weather_tip(condition, temp):
    """Generate a travel tip based on weather condition"""
    condition = str(condition).lower()
    temp = float(temp) if isinstance(temp, (int, float)) or (isinstance(temp, str) and temp.replace('.', '', 1).isdigit()) else 20
    
    if "rain" in condition or "shower" in condition:
        return "Pack an umbrella or raincoat for your trip!"
    elif "snow" in condition:
        return "Pack warm clothing and waterproof footwear."
    elif "sunny" in condition or "clear" in condition:
        return "Don't forget sunscreen and sunglasses!"
    elif "cloud" in condition:
        return "Weather may change quickly, dress in layers."
    elif temp > 30:
        return "It's very hot! Stay hydrated and seek shade during peak hours."
    elif temp < 10:
        return "It's quite cold. Pack warm clothing and dress in layers."
    else:
        return "Check the local forecast regularly as weather conditions may change."
