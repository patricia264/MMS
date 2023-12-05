from deepface import DeepFace
import cv2
import time



def takePic(MemePosition, cap, MemeDictionary):

    #Verzögerung von 2 sekunden bis Bild aufgenommen wird ACHTUNG BLOCKT ALLES NOCH KEINE GUTE ASYNCHRONE LÖSUNG GEFUNDEN
    time.sleep(2)
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
                            actions=['age', 'gender', 'race', 'emotion'])

    # save absolute values of a certain emotion, why 0 idk
    happyPercent = (analyzRes[0]['emotion']['happy'])
    MemeDictionary[MemePosition] = happyPercent




# Path to the image you want to analyze
# img_path = "assets/Deepface workspace/database/happy.jpg"

# Analyze the image for facial attributes including emotions
#result = DeepFace.analyze(img_path, actions=['emotion'])

# Access the probability score for happiness
#happiness_score = result['emotion']['happy']
##print("Happiness score:", happiness_score)

#analyse a picture
# objs = DeepFace.analyze(img_path,
       # actions = ['age', 'gender', 'race', 'emotion'])

#print absolute values of a certain emotion, why 0 idk
# print(objs[0]['emotion']['happy'])
