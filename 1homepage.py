import streamlit as st
from pathlib import Path
from modules import *


st.image(f"{Path("assets/BINF_Club_Logo_slim.png")}")
st.title("Welcome to the U of C Bioinformatics Club")


st.header("Who Are We?")
st.markdown("We are something something something asuhdakushdukasd")


st.header("Our Mission")
st.markdown("OMG we love biology and like computerscience and like omg so many things it's so aweasomew and we want to share it with everyone....")

st.header("Past Events")
st.subheader("Biohack 2025")
st.markdown("BioHack was our club-run hackathon on super cool bioinformatics stuff!!!")
st.image(applyEXIF(Path("assets/biohack_example.jpg")), caption = "Eat food at bioahack yummmy")
