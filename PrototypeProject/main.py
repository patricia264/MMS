import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk,ttk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
from PIL import Image
import glob

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


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
# ImageList erstellen mit Strings unserer Memes-PFADE, müssen pngs sein
image_list = []
for filename in glob.glob(r"./assets/imagesmemes//*"):
    image_list.append(filename)

# erstellt Dictionary String MemesPfade: Bewertungs-Ints, die jetzt auf 0 gesetzt sind.
# diese Ints können dann durch die Happy Rate der DeepFace Erkennungsschnittstelle überschrieben werden

MemeDictionary = {}
for filename in image_list:
    MemeDictionary[filename] = 0

# globale Variabeln
# StringVar, damit Text Button verändert werden kann
MemePosition = 0
buttonText = tkinter.StringVar()
buttonText.set("Next")


# Erhöht MemePosition um eines und stellt sicher, dass beim letzten Meme der Text auf "Results" ändert
# Setzt Progress Bar wieder auf 0

def button_clicked():
    global MemePosition
    MemePosition += 1
    set_Image()
    progressVarInt.set(0)
    if MemePosition < len(image_list) - 1:
        return
    buttonText.set("Results")


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
button_1 = Button(
    image=button_image_1,
    textvariable=buttonText,
    fg="#FFFFFF",
    font=("Inter", 32 * -1),
    compound=tkinter.CENTER,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked,
    relief="flat"
)
button_1.place(
    x=741.0,
    y=637.0,
    width=206.0,
    height=59.0
)
# white title
canvas.create_text(
    343.0,
    81.0,
    anchor="nw",
    text="Meme Game",
    fill="#FFFFFF",
    font=("Press Start 2P", 40 * -1)
)
# black title
canvas.create_text(
    350.0,
    75.0,
    anchor="nw",
    text="Meme Game",
    fill="#000000",
    font=("Press Start 2P", 40 * -1)
)


progressVarInt = tkinter.IntVar()


# künstliche Zahl als Platzhalter.
# sollte aus unserem Dictionary dann geholt werden

progressVarInt.set(30)


# Prozentanzahl als ProgressBar

progressbar= ttk.Progressbar(
    length=300,
    orient='horizontal',
    variable=progressVarInt)

progressbar.place(
    x = 250,
    y = 655
)

# Prozentanzahl als Text oder au nöd. git kein direkte weg text mit variable z verbinde
#canvas.create_text(
 #   190.0,
#  655.0,
#    anchor="nw",
 #   text= "63%",
  #  fill="#000000",
   # font=("Avenir Next LP Pro", 20 * -1))


set_Image()

window.resizable(False, False)
window.mainloop()
