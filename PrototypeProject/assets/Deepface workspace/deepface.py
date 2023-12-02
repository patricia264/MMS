from deepface import DeepFace

# Access camera in real time and see emotions
#DeepFace.stream("database")

# Path to the image you want to analyze
img_path = "database/happy.jpg"

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
