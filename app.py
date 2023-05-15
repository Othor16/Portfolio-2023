import streamlit as st
import pandas as pd
import os



# TiTLE
st.title("Olivia Thor's Portfolio" )

st.header("Welcome!")
st.write("Hello! I'm a 19y/o Illustration Major at Parsons School of Design. Currently I've been interested in photobooks and visual development on projects. I've experimented with painting, graphic design, animation and more! Below you will see some of my past work either from college or high school, commissions or art programs I've tried from the past. Hope you enjoy!")

st.header("Animations 2023")

st.subheader("breathe - 4D Core Studio Final Animation")
final4D = open('animations1.mp4', 'rb')
video_bytes = final4D.read()
st.video(video_bytes)
st.write("A short animation about just taking a moment to sit and relax as life happens. Done with Adobe Photoshop, Illustrator, and Premiere Pro. Sounds pulled from freesounds.org")

st.subheader("Pigeon Talk - 4D Core Studio Sound Animation")
pigeon = open('animations2.mp4', 'rb')
pigeon_bytes = pigeon.read()
st.video(pigeon_bytes)
st.write("A talk about the scandal of pigeons with Kirari T. and I. Drawn with chalk pastel, edit in Adobe Premiere Pro")

st.write("---")

#Illustrations
st.header("Illustrations")

#Halloween Post Cards

st.subheader("Halloween Postcards 2020")
st.write('This project started by free-drawing halloween themed illustrations on packaging boxes using a sharpie. Taking a picture of each illustration through Adobe Capture, I was able to scan the drawings into Adobe Illustrator.  This is where I cleaned up and colored the illustrations.')
    #images
HPFinal1 = ['hp9.png','hp10.png','hp11.png']
HPFinal2 = ['hp12.png','hp13.png','hp14.png']
HPD1 = ['hp3.png','hp4.png','hp5.png']
HPD2 = ['hp6.png','hp7.png','hp8.png']
HPSketch = ['hp1.png','hp2.png']

# Columns
hpfinal = st.columns(len(HPFinal1))
hpfinal2 = st.columns(len(HPFinal2))
digital1 = st.columns(len(HPD1))
digital2 = st.columns(len(HPD2))
sketch = st.columns(len(HPSketch))

for i, col in enumerate(hpfinal):
    col.image(HPFinal1[i], caption=f"Final Iterations {i+1}")
for i, col in enumerate(hpfinal2):
    col.image(HPFinal2[i], caption=f"Final Iterations {i+3}")
for i, col in enumerate(digital1):
    col.image(HPD1[i], caption=f"Digital Iterations {i+1}")
for i, col in enumerate(digital2):
    col.image(HPD2[i], caption=f"Digital Iterations {i+3}")
for i, col in enumerate(sketch):
    col.image(HPSketch[i], caption=f"Drawn with Sharpie {i+1}")

st.write("---")


#Buttons

st.subheader("Weinberg/Newton Gallery Button 2021")
st.write('This button was designed and selected as one of the top designs for the “Collective Communities Exhibition Button Design Challenge” with the Weinberg/Newton Gallery in Chicago IL.  They proceeded to create these buttons for free and sent them to anyone who helped spread the word about the importance of climate and environmental justice.')
    #images
Button_Design = "BD_5.png"
st.image(Button_Design, caption="Button Design")

BDProcess = ["BD_1.png", "BD_2.png", "BD_3.png", "BD_4.png"]

# Columns
bcols = st.columns(len(BDProcess))

for i, col in enumerate(bcols):
    col.image(BDProcess[i], caption=f"Process {i+1}")

st.write("---")

#George Album

st.subheader("Mr. Incredible - Scott Freebass 2021")
st.write('This piece was commissioned for a single released on Spotify called “Mr. Incredible”.  With not a lot of information on the artist and not a lot of guidelines, I started this piece with two images I created in my sketchbook of the artist, King of Dreams. From here, I transferred the images into Adobe Photoshop and fixed it up a bit before playing with the different modes of how these two different iterations affect one another, either with color or adding or subtracting an effect. I created multiple different iterations of the cover art before sending it over to my client and asking which ones he liked or disliked and we discussed what can be added or discarded before settling on one.')
    #images
ACFinal = "GA_2.png"
st.image(ACFinal, caption="Mr.Incredible Album Cover")

GAORANGE = ["GA_3.png", "GA_4.png"]
GABLACK = ["GA_7.png", "GA_8.png", 'GA_9.png']

# Columns
gao = st.columns(len(GAORANGE))
gab = st.columns(len(GABLACK))

for i, col in enumerate(gao):
    col.image(GAORANGE[i], caption=f"iterations {i+1}")
for i, col in enumerate(gab):
    col.image(GABLACK[i], caption=f"iterations {i+3}")

st.write("---")

#AFTER SCHOOL MATTERS (2018-2021)
st.header ("After School Matters")
st.write("After School Matters (ASM) is a non-profit organization that gives students of Chicago the opportunity to be paid while trying new classes and learn new skills. Their programs have helped me grow as an artist a lot and explore new mediums of the art world. I've taken graphic design, painting, to mosaics. ")

st.write("---")
#Space Post Card (2019)

st.subheader("Space Post Card 2021")
st.write("A simple design excercise that started by listing themes and sketching quick thumbnails. I used Adobe Illustrator to create the backgrounds and foregrounds before transferring to ibisPaint X and adding the finishing touches.")
    #images
PCFInal = "ASM_PC_8.png"
st.image(PCFInal, caption="Space Post Card for ASM Gift Shop")

PCProcess1 = ["ASM_PC_2.png", "ASM_PC_3.png", "ASM_PC_4.png",]
PCProcess2 = ["ASM_PC_5.png", "ASM_PC_6.png", "ASM_PC_7.png"]

# Columns
pccols = st.columns(len(PCProcess1))
pccols = st.columns(len(PCProcess2))
for i, col in enumerate(pccols):
    col.image(PCProcess1[i], caption=f"Process {i+1}")    
for i, col in enumerate(pccols):
    col.image(PCProcess2[i], caption=f"Process {i+4}")

st.write("---")

#CARD DESIGN

st.subheader("Elemental Play Cards 2020")
st.write('In my Graphic Design program, we designed and created a deck of playing cards with the theme of the 4 elements: Water, Fire, Earth, and Air. Everyone designed at least one card to each element before at least one card was chosen from each student. Three of mine were selected to be included in the deck: The Water, Earth, and Air cards. All four of my cards were created in Adobe Illustrator. The process for each card was all different. I experimented with lines a lot more in the water and air cards. The fire card represented the heart suite and so I attempted to combine the two in a pattern. While the Earth card was more of an opportunity to explore how to illustrate different plants.')
  
    #images
cards = "CARDS1.png"
st.image(cards, caption="Elementat Play Cards for ASM Gift shop")

air = ["CARDS2.png", "CARDS3.png"]
earth = ["CARDS4.png", "CARDS5.png"]
fire = ['CARDS6.png', 'CARDS7.png']
water =['CARDS8.png', 'CARDS9.png']

# Columns
aircol = st.columns(len(air))
earthcol = st.columns(len(earth))
firecol = st.columns(len(fire))
watercol = st.columns(len(water))

for i, col in enumerate(aircol):
    col.image(air[i], caption=f"Air Iteration {i+1}")    
for i, col in enumerate(earthcol):
    col.image(earth[i], caption=f"Earth Iteration {i+1}")
for i, col in enumerate(firecol):
    col.image(fire[i], caption=f"Fire Iteration {i+1}")    
for i, col in enumerate(watercol):
    col.image(water[i], caption=f"Water Iteration {i+1}")

st.write('---')

st.header("Paintings")
#Painting

st.subheader("Poisoned Mind 2020")
st.write('This painting was a reaction to the Covid-19 Pandemic. During quarantine, a lot was happening in the world that caused anxiety and loneliness. Especially through the media, hearing what’s happening in the world was nerve-wracking.The flowers in this painting are based on real poisonous flowers that I researched during my process. The idea of the flowers growing out of the human head represented how one negative thought can maximize its growth within the mind.')
    #images
PMPainting = "pm3.png"
pmcolor = "pm2.png"
pmsketch = "pm1.png"
st.image(PMPainting, caption="Poisoned Mind")
st.image (pmcolor, caption= "thumbnails and color palettes")
st.image (pmsketch, caption = "sketches & research")
