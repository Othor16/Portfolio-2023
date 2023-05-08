import streamlit as st
import pandas as pd

# TiTLE
st.title("Olivia Thor - Portfolio")

#header and subheader
st.header("Welcome!")
st.subheader("merely exist")

#Infor about you
st.text("INFO ABOUT ME.")

#Illustrations
st.header("Illustrations")
st.subheader("Three Portraits 2019")
col1, col2, col3 = st.columns(3)
illustration1 = "Illustration Portraits1.PNG"
illustration2 = "Illustration Portraits2.PNG"
illustration3 = "Illustration Portraits3.PNG" 
with col1:
   st.header("Portait 1")
   st.image(illustration1)

with col2:
   st.header("Portrait 2")
   st.image(illustration2)
with col3:
   st.header("Portrait 3")
   st.image(illustration3)

#Buttons
st.subheader("Earth Day Button Design 2021")
button_design = ("button design.png")
real_button = ("buttons.jpg")
col1, col2 = st.columns(2)
with col1:
   st.image(button_design)
with col2:
   st.image(real_button)


col1, col2, col3, col4 = st.columns(4)
bdp1 = "Button Design Process_1.png"
bpd2 = "Button Design Process_2.png"
bpd3 = "Button Design Process_3.png" 
bpd4 = "Button Design Process_4.png"
with col1:
   st.image(bpd2)

with col2:
   st.image(bdp1)
with col3:
   st.image(bpd3)
with col4:
   st.image(bpd4)

#Halloween Packages
st.header("Halloween Illustrations 2020")
st.subheader("For my little cousins")
   #images
hp1 = "halloween package 2.jpg"
hp2 = "halloween package 3.jpg"
hp3 = "halloween package 4.jpg" 
hp4 ="halloween package 5.jpg" 
hp5 = "halloween package 6.jpg" 
   #columns
pak1, pak2 = st.columns(2)
with pak1:
   st.image(hp1)

with pak2:
   st.image(hp2)
