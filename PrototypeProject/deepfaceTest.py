from deepface import DeepFace
import cv2
import time
import threading

highestScore = 0.01
bestMeme = 0

def takePic(MemePosition, cap, MemeDictionary):

    def delayed_capture():
        global highestScore
        global bestMeme
        time.sleep(2)  # 2 seconds delay
        # Write the rest of the capture logic here
        while not cap.isOpened():
            pass
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f"WebCamShots/{MemePosition}.jpg", frame)

        analyzRes = DeepFace.analyze(f"WebCamShots/{MemePosition}.jpg", actions=['emotion'])
        happyPercent = analyzRes[0]['emotion']['happy']
        MemeDictionary[MemePosition] = happyPercent

        if happyPercent > highestScore:
            highestScore = happyPercent
            bestMeme = MemePosition

    # Start a thread to capture the image after a delay
    threading.Thread(target=delayed_capture).start()
