import glob

def setUpVariables():

    # Ungebrauchte Methode, das alles könnte man theoretisch extrahieren

    # ImageList erstellen mit Strings unserer Memes-PFADE, müssen pngs sein
    image_list = []
    for filename in glob.glob(r"C:\Users\Gioia\Desktop\Uni Bern\MMS\Draft2\build\assets\imagesmemes\\*"):
        image_list.append(filename)

    # erstellt Dictionary String MemesPfade: Bewertungs-Ints, die jetzt auf 0 gesetzt sind.
    # diese Ints können dann durch die Happy Rate der DeepFace Erkennungsschnittstelle überschrieben werden

    memeDictionary = {}
    for filename in image_list:
        memeDictionary[filename] = 0

    memePosition = 0