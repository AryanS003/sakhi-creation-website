import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Page Title
st.title("Sakhi Creation - Women's Fashion Store")
st.write("Welcome to Sakhi Creation, your go-to shop for elegant and trendy women's fashion!")

# Product Showcase with Horizontal Scrolling
st.header("Our Featured Products")
products = [
    {"name": "Elegant Kurti", "price": "₹1200", "image": "https://via.placeholder.com/200", "desc": "Beautiful cotton kurti with embroidery."},
    {"name": "Designer Saree", "price": "₹2500", "image": "https://via.placeholder.com/200", "desc": "Silk saree with intricate zari work."},
    {"name": "Anarkali Dress", "price": "₹3000", "image": "https://via.placeholder.com/200", "desc": "Floor-length anarkali with dupatta."},
    {"name": "Casual Palazzo Set", "price": "₹1500", "image": "https://via.placeholder.com/200", "desc": "Comfortable and stylish palazzo suit."},
    {"name": "Western Dress", "price": "₹1800", "image": "https://via.placeholder.com/200", "desc": "Chic western dress for every occasion."},
]

carousel_html = """
<div style="overflow-x: auto; white-space: nowrap; width: 100%;">
"""
for product in products:
    carousel_html += f"""
    <div style="display: inline-block; text-align: center; margin: 10px;">
        <img src="{product['image']}" width="70%"><br>
        <strong>{product['name']}</strong><br>
        {product['desc']}<br>
        <strong>{product['price']}</strong>
    </div>
    """
carousel_html += "</div>"

components.html(carousel_html, height=250)

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
    st.map(pd.DataFrame({"lat": [expo["lat"]], "lon": [expo["lon"]]}))
    st.markdown("---")

# Google Drive Link for Full Catalog
st.header("View Our Full Collection")
drive_link = "https://drive.google.com/drive/folders/YOUR_DRIVE_LINK_HERE"
st.markdown(f"[Click here to view our full catalog]({drive_link})")

st.write("Follow us for the latest trends and collections!")
