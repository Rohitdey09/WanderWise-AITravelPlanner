import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import time

def get_coordinates(location_name):
    """Get latitude and longitude for a location name"""
    try:
        
        geolocator = Nominatim(user_agent="ai_travel_planner", timeout=10)
        
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                location = geolocator.geocode(location_name)
                if location:
                    return location.latitude, location.longitude
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(1)  
                    continue
                else:
                    st.error(f"Failed to get coordinates after {max_retries} attempts: {e}")
                    raise
                    
        return None
    except Exception as e:
        st.error(f"Error getting location coordinates: {e}")
        return None

def create_trip_map(origin, destination):
    """Create a map showing the trip route"""
    
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)
    
    if not origin_coords or not destination_coords:
        st.warning("Could not find locations on map. Please check spelling or try again later.")
        return None
    
    
    center_lat = (origin_coords[0] + destination_coords[0]) / 2
    center_lon = (origin_coords[1] + destination_coords[1]) / 2
    
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=4)
    
    # Add markers
    folium.Marker(
        location=origin_coords,
        popup=origin,
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(m)
    
    folium.Marker(
        location=destination_coords,
        popup=destination,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)
    
    
    folium.PolyLine(
        locations=[origin_coords, destination_coords],
        color="blue",
        weight=3,
        opacity=0.7
    ).add_to(m)
    
    return m

def display_trip_map(origin, destination):
    """Display the trip map in Streamlit"""
    if origin and destination:
        with st.spinner("Generating map..."):
            map = create_trip_map(origin, destination)
            if map:
                st.subheader("🗺️ Trip Route")
                folium_static(map)
    else:
        st.info("Enter origin and destination to see the route on a map")