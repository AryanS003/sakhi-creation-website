import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Page Title
st.title("Sakhi Creation - Women's Fashion Store")
st.write("Welcome to Sakhi Creation, your go-to shop for elegant and trendy women's fashion!")

# Product Showcase
st.header("Our Featured Products")
products = [
    {"name": "Elegant Kurti", "price": "₹1200", "image": "https://via.placeholder.com/200", "desc": "Beautiful cotton kurti with embroidery."},
    {"name": "Designer Saree", "price": "₹2500", "image": "https://via.placeholder.com/200", "desc": "Silk saree with intricate zari work."},
    {"name": "Anarkali Dress", "price": "₹3000", "image": "https://via.placeholder.com/200", "desc": "Floor-length anarkali with dupatta."},
    {"name": "Casual Palazzo Set", "price": "₹1500", "image": "https://via.placeholder.com/200", "desc": "Comfortable and stylish palazzo suit."},
    {"name": "Western Dress", "price": "₹1800", "image": "https://via.placeholder.com/200", "desc": "Chic western dress for every occasion."},
]

for product in products:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(product["image"], width=150)
    with col2:
        st.subheader(product["name"])
        st.write(product["desc"])
        st.write(f"**Price:** {product['price']}")
    st.markdown("---")

# Exhibition Locations
st.header("Upcoming Exhibitions")
exhibitions = [
    {"name": "Fashion Expo 2025", "location": "Mumbai", "lat": 19.0760, "lon": 72.8777},
    {"name": "Ethnic Wear Fair", "location": "Delhi", "lat": 28.6139, "lon": 77.2090},
    {"name": "Handloom Showcase", "location": "Bangalore", "lat": 12.9716, "lon": 77.5946},
]

for expo in exhibitions:
    st.subheader(expo["name"])
    st.write(f"**Location:** {expo['location']}")
    map_obj = folium.Map(location=[expo["lat"], expo["lon"]], zoom_start=12)
    folium.Marker([expo["lat"], expo["lon"]], popup=expo["name"]).add_to(map_obj)
    folium_static(map_obj)
    st.markdown("---")

# Google Drive Link for Full Catalog
st.header("View Our Full Collection")
drive_link = "https://drive.google.com/drive/folders/YOUR_DRIVE_LINK_HERE"
st.markdown(f"[Click here to view our full catalog]({drive_link})")

st.write("Follow us for the latest trends and collections!")
