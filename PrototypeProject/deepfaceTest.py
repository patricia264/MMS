from deepface import DeepFace
import cv2
import time


def takePic(MemePosition, cap):
    time.sleep(2)
    # Warte auf die Initialisierung der Kamera
    while not cap.isOpened():
        pass
    # Liest ein Bild von der Webcam
    ret, frame = cap.read()
    # Überprüfe, ob das Lesen erfolgreich war
    if ret:
        # Speichere das Bild
        cv2.imwrite(f"WebCamShots/{MemePosition}.jpg", frame)


# Access camera in real time and see emotions
#DeepFace.stream("database")

# Path to the image you want to analyze
img_path = "assets/Deepface workspace/database/happy.jpg"

# Analyze the image for facial attributes including emotions
#result = DeepFace.analyze(img_path, actions=['emotion'])

# Access the probability score for happiness
#happiness_score = result['emotion']['happy']
##print("Happiness score:", happiness_score)

#analyse a picture
objs = DeepFace.analyze(img_path,
        actions = ['age', 'gender', 'race', 'emotion']
)
#print absolute values of a certain emotion, why 0 idk
print(objs[0]['emotion']['happy'])
