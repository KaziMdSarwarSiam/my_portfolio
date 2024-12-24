import streamlit as st
from PIL import Image


st.title("Project 2: Design of a Residence")
st.subheader("")


img4=Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-01.png')
img5=Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-02.png')
img6=Image.open('RESIDENCE SHEET FOR PORTFOLIO [Recovered]-03.png')

st.image(img4)
st.image(img5)
st.image(img6)