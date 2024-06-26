import cv2
import numpy as np

# Load the face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to extract face from image
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
        return cropped_face

# Start video capture
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = face_extractor(frame)
    if face is not None:
        count += 1
        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = 'faces/user' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
        print("Face detected and saved:", file_name_path)
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 100:  # Press 'Enter' to exit
        break

cap.release()
cv2.destroyAllWindows()
print('Collecting Samples Complete!!!')
