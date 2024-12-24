# import streamlit as st
# from PIL import Image

# st.set_page_config(layout='wide')

# st.title("Hello! This is Siam.")
# st.subheader("An architecture student from Bangladesh University of Engineering and Technology (BUET).")

# img=Image.open('RESUME - Copy-01.png')
# st.image(img)

import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Project 1", "Project 2"])

# Home page content
if page == "Home":
    st.title("Hello! This is Siam.")
    st.subheader("An architecture student from Bangladesh University of Engineering and Technology (BUET).")
    img = Image.open('RESUME - Copy-01.png')
    st.image(img)

# Project 1 content
elif page == "Project 1":
    st.title("Project 1: Design of a Pedestrian Bridge")
    st.subheader("A pedestrian bridge that illustrates the beauty in tensigrity structures.")
    img2 = Image.open('BRIDGE SHEET FOR PORTFOLIO-01.png')
    img3 = Image.open('BRIDGE SHEET FOR PORTFOLIO-02.png')
    st.image(img2)
    st.image(img3)

# Project 2 content
elif page == "Project 2":
    st.title("Project 2: Design of a Residence")
    img4 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-01.png')
    img5 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-02.png')
    img6 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-03.png')
    st.image(img4)
    st.image(img5)
    st.image(img6)

