import cv2
import numpy as np
import dlib 

# Load pre-trained face detector and facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dlib.shape_predictor('shape_predictor_68_face_landmarks.dat'))

# Load filter image (e.g., glasses)
filter_img = cv2.imread('glasses.png', -1)  # Load with alpha channel

def overlay_filter(frame, filter_img, position):
    x, y, w, h = position
    filter_resized = cv2.resize(filter_img, (w, h))
    
    for i in range(0, filter_resized.shape[0]):
        for j in range(0, filter_resized.shape[1]):
            if filter_resized[i, j][3] != 0:  # Check alpha channel
                frame[y + i, x + j] = filter_resized[i, j][:3]  # Apply filter
    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        frame = overlay_filter(frame, filter_img, (x, y + int(h / 2), w, int(h / 2)))  # Adjust filter position

    cv2.imshow('AR Filter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
