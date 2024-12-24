import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

# Helper function to route based on query parameters
def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Get the current page from query parameters
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["Homepage"])[0]

# Header with navigation links
st.markdown(
    """
    <style>
    .nav-buttons {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
    }
    .nav-buttons a {
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 5px;
        color: white;
        background-color: #4CAF50;
    }
    .nav-buttons a:hover {
        background-color: #45a049;
    }
    </style>
    <div class="nav-buttons">
        <a href="?page=Homepage">Homepage</a>
        <a href="?page=Project1">Project 1</a>
        <a href="?page=Project2">Project 2</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Page Content
if page == "Homepage":
    st.title("Hello! This is Siam.")
    st.subheader("An architecture student from Bangladesh University of Engineering and Technology (BUET).")
    img = Image.open('RESUME - Copy-01.png')
    st.image(img)

elif page == "Project1":
    st.title("Project 1: Design of a Pedestrian Bridge")
    st.subheader("A pedestrian bridge that illustrates the beauty in tensigrity structures.")
    img2 = Image.open('BRIDGE SHEET FOR PORTFOLIO-01.png')
    img3 = Image.open('BRIDGE SHEET FOR PORTFOLIO-02.png')
    st.image(img2)
    st.image(img3)

elif page == "Project2":
    st.title("Project 2: Design of a Residence")
    img4 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-01.png')
    img5 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-02.png')
    img6 = Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-03.png')
    st.image(img4)
    st.image(img5)
    st.image(img6)
