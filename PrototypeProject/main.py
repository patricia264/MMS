import tkinter
from pathlib import Path
import sys
import tkinter as tk
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk,ttk, Canvas, Label, Entry, Text, Button, PhotoImage
from tkinter.font import Font
import glob
import deepfaceTest
import cv2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

#Initalisierung webcam
cap = cv2.VideoCapture(0)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Erstellt neues Fenster,in Doks meistens als root angegeben
window = Tk()

# SuperCooleFont importieren
font_path = r"./assets/PressStart2P-Regular.ttf"
custom_font = Font(
    family="PressStart2P",
    size=40 * -1
)

# Font Import
window.option_add("*Font", custom_font)

window.geometry("1024x768")
window.configure(bg="#FFFFFF")

# Versuch, hier alle Funktionalitäten einzubauen (lmao was e catastrophe die gliederig)
# ImageList erstellen mit Strings unserer Memes-PFADE, müssen pngs sein und schon zurechtgeschnitten (400x400px glaub)
image_list = []
for filename in glob.glob(r"./assets/imagesmemes//*"):
    image_list.append(filename)

# globale Variabeln
# StringVar, damit Text Button verändert werden kann
MemePosition = 0
buttonText = tkinter.StringVar()
buttonText.set("Next")

# erstellt Dictionary Int MemePosition: Bewertungs-Ints, die jetzt auf 0 gesetzt sind.
# diese Ints können dann durch die Happy Rate der DeepFace Erkennungsschnittstelle überschrieben werden
#dies geschieht bei Funktion deepfaceTest.takePic()

MemeDictionary = {}
for count,filename in enumerate(image_list):
    MemeDictionary[count] = 0


# Erhöht MemePosition um eines und stellt sicher, dass beim letzten Meme der Text auf "Results" ändert
# Setzt Progress Bar wieder auf 0
#Yanis: addded if condition depending on button value, now button has 2 functions
#sorry for confusing naming, buttonText is the Button, while button_text is the string which is
#saved within the button and displayed
def button_clicked():

    button_text = buttonText.get()
    if button_text == "Next":
        global MemePosition
        MemePosition += 1
        set_Image()
        progressVarInt.set(0)
        # Ändert Text von Button von Next zu Result
        if MemePosition < len(image_list) - 1:
            return
        buttonText.set("Results")
        print(MemeDictionary)

    #goes to the results page
    elif button_text == "Results" :
        displayResultsPage()
        buttonText.set("finish")

    #terminates program
    elif button_text == "finish":
        sys.exit(0)

#Results page, shows the best meme and what happiness value it made you.
#add finish button to end the game

def displayResultsPage():

    #call these functions to make a ''semi-blank'' canvas whitout completely building a new one and
    #retaining button logic
    remove_Image()
    canvas.delete(white_title_id)
    canvas.delete(black_title_id)

    # Top text label
    top_text = Label(window, text="Your top meme was:", font=("Arial", 20))
    top_text.pack(pady=50)  # Add padding to the top

    # Display an image (change 'path_to_your_image.png' to the actual image path)
    img = PhotoImage(file=image_list[deepfaceTest.bestMeme])
    image_label = Label(window, image=img)
    image_label.image = img  # Keep a reference to the image to prevent garbage collection
    image_label.pack(pady=50)  # Add padding below the image

    # Smaller text under the image
    bottom_text = Label(window, text="It raised your happiness levels to: " + str(deepfaceTest.highestScore) + " %", font=("Arial", 12))
    bottom_text.pack(pady=20)  # Add padding above the text

    # Center align widgets vertically and horizontally
    top_text.pack(anchor='center')
    image_label.pack(anchor='center')
    bottom_text.pack(anchor='center')


# Bilderquelle verändert sich mit der MemePosition. Auch erstmalige Initalisierung vom Bild durch diese Methode
def set_Image():
    global canvas
    global memeImage
    if MemePosition < len(image_list):

        memeImage = PhotoImage(
        file=image_list[MemePosition])
        image_2 = canvas.create_image(
        512.0,
        384.0,
        image=memeImage)

#helper function to remove the image as to make space for results
def remove_Image():
    global canvas
    global memeImage
    global progressbar

    # Check if 'image_2' has been set previously
    if 'memeImage' in globals():
        canvas.delete(memeImage)  # Delete the image object from the canvas
        del memeImage  # Remove the reference to the image object
    progressbar.destroy()


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))


image_1 = canvas.create_image(
    512.0,
    384.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

#Button GUI Variabeln
button_1 = Button(
    image=button_image_1,
    textvariable=buttonText,
    fg="#FFFFFF",
    font=("Inter", 32 * -1),
    compound=tkinter.CENTER,
    borderwidth=0,
    highlightthickness=0,
    #bei Klick führt zuerst Hauptfunktion aus, dann take pic (Hoffnung das delay klappt, tuts ned)
    command=lambda: [button_clicked(), deepfaceTest.takePic(MemePosition, cap, MemeDictionary, progressVarInt)],
    relief="flat"
)

button_1.place(
    x=741.0,
    y=637.0,
    width=206.0,
    height=59.0
)

#added title_ids, which makes the deletion process much easier :)
# white title
white_title_id = canvas.create_text(
    343.0,
    81.0,
    anchor="nw",
    text="Meme Game",
    fill="#FFFFFF",
    font=("Press Start 2P", 40 * -1)
)
# black title
black_title_id = canvas.create_text(
    350.0,
    75.0,
    anchor="nw",
    text="Meme Game",
    fill="#000000",
    font=("Press Start 2P", 40 * -1)
)


# Var erstellt um Progressbarwert dann zu verändern, damit dynamischer Wert
progressVarInt = tkinter.IntVar()
progressVarInt.set(0)





# Prozentanzahl als ProgressBar
progressbar= ttk.Progressbar(
    length=300,
    orient='horizontal',
    variable=progressVarInt)

progressbar.place(
    x = 250,
    y = 655
)



# erstmaliges Initialisieren von Bild
set_Image()

#erstes Mal take Pic da sonst mit Next Funktion verbunden
deepfaceTest.takePic(MemePosition, cap, MemeDictionary, progressVarInt)

window.resizable(False, False)
window.mainloop()

# Gib die Kameraressourcen frei
cap.release()
# Schließe alle OpenCV-Fenster
cv2.destroyAllWindows()
