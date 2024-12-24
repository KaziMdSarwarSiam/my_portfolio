import streamlit as st
from PIL import Image


st.title("Project 1: Design of a Pedestrian Bridge")
st.subheader("A pedestrian bridge that illustrates the beauty in tensigrity structures.")


img2=Image.open('BRIDGE SHEET FOR PORTFOLIO-01.png')
img3=Image.open('BRIDGE SHEET FOR PORTFOLIO-02.png')

st.image(img2)
st.image(img3)
