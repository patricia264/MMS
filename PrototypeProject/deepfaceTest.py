from deepface import DeepFace
import cv2
import time

highestScore = 0.01
bestMeme = 0

def takePic(MemePosition, cap, MemeDictionary):

    global highestScore
    global bestMeme

    # Verzögerung von 2 sekunden bis Bild aufgenommen wird ACHTUNG BLOCKT ALLES? NOCH KEINE GUTE ASYNCHRONE LÖSUNG GEFUNDEN
    #time.sleep(2)
    # Warte auf die Initialisierung der Kamera
    while not cap.isOpened():
        pass
    # Lese ein Bild von der Webcam
    ret, frame = cap.read()
    # Überprüfe, ob das Lesen erfolgreich war
    if ret:
        # Speichere das Bild
        cv2.imwrite(f"WebCamShots/{MemePosition}.jpg", frame)

    # Analyziere Bild
    analyzRes = DeepFace.analyze(f"WebCamShots/{MemePosition}.jpg",
                            actions=['emotion'])

    # save absolute values of a certain emotion, why 0 idk
    happyPercent = (analyzRes[0]['emotion']['happy'])
    MemeDictionary[MemePosition] = happyPercent

    if happyPercent > highestScore:
        highestScore = happyPercent
        bestMeme = MemePosition