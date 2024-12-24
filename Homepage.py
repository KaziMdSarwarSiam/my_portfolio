import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

st.title("Hello! This is Siam.")
st.subheader("An architecture student from Bangladesh University of Engineering and Technology (BUET).")

img=Image.open('RESUME - Copy-01.png')
st.image(img)