import streamlit as st
import pandas as pd

# TiTLE
st.title("Olivia Thor - Portfolio")

st.header("Welcome!")
st.subheader("merely exist")
st.text("INFO ABOUT ME.")

#Illustrations
st.header("Illustrations")

#3 Portraits

st.subheader("Three Portraits 2019")
st.text('Descriptions of Project and Progress')
   #Image Archive
illustration1 = "Illustration Portraits1.PNG"
illustration2 = "Illustration Portraits2.PNG"
illustration3 = "Illustration Portraits3.PNG" 

   #Columns
col1, col2, col3 = st.columns(3)
with col1:
   st.image(illustration1, caption = 'Portrait 1')
with col2:
   st.image(illustration2,caption = 'Portrait 2')
with col3:
   st.image(illustration3,caption = 'Portrait 3')

#Buttons

st.subheader("Earth Day Button Design 2021")

   #Image Archive
button_design = ("button design.png")
real_button = ("buttons.jpg")
bdp1 = "Button Design Process_1.png"
bpd2 = "Button Design Process_2.png"
bpd3 = "Button Design Process_3.png" 
bpd4 = "Button Design Process_4.png"

   #Columns - Final Product
col1, col2 = st.columns(2)
with col1:
   st.image(button_design)
with col2:
   st.image(real_button)

   #Columns - Process
col1, col2, col3, col4 = st.columns(4)
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
   #image Archive
hp1 = "halloween package 2.jpg"
hp2 = "halloween package 3.jpg"
hp3 = "halloween package 4.jpg" 
hp4 ="halloween package 5.jpg" 
hp5 = "halloween package 6.jpg" 
hp6 = "halloween package 7.jpg"
hp7 = "halloween package 8.jpg"
hp8 = "halloween package 9.jpg"
hp9 = "halloween package 10.png"
hp10 = "halloween package 11.png"
hp11 = "halloween package 12.png"
hp12 = "halloween package 13.png"
hp13 = "halloween package 14.png"
hp14 = "halloween package 15.png"

   #column: Drawings
st.subheader("Drawn on Packages with Sharpie & Gold Pen")
pak1, pak2 = st.columns(2)
with pak1:
   st.image(hp1)
with pak2:
   st.image(hp2)
   #column: Digital
st.subheader("Digitalized")
ink1, ink2, ink3 = st.columns (3)
with ink1:
   st.image(hp4)
with ink2:
   st.image(hp5)
with ink3:
   st.image(hp6)
ink4, ink5, ink6 = st.columns(3)
with ink4:
   st.image(hp7)
with ink5:
   st.image(hp8)
with ink6:
   st.image(hp8)
   #column: Final
st.subheader("Colorized")
fhp1, fph2, fph3 = st.columns(3)
with fhp1:
   st.image(hp9)
with fph2:
   st.image(hp10)
with fph3:
   st.image(hp11)
fhp4, fph5, fph6 = st.columns(3)
with fhp4:
   st.image(hp12)
with fph5:
   st.image(hp13)
with fph6:
   st.image(hp14)