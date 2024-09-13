# import cv2
# import dlib

# Load the pre-trained facial landmarks model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to extract the eyes region using the landmarks
def extract_eye(landmarks, eye_points):
    points = [(landmarks.part(point).x, landmarks.part(point).y) for point in eye_points]
    x = min(point[0] for point in points)
    y = min(point[1] for point in points)
    w = max(point[0] for point in points) - x
    h = max(point[1] for point in points) - y
    return (x, y, w, h)

# Eye landmarks
LEFT_EYE = list(range(36, 42))
RIGHT_EYE = list(range(42, 48))

# Open a webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Get the landmarks for the face
        landmarks = predictor(gray, face)

        # Extract and draw the left and right eyes
        left_eye = extract_eye(landmarks, LEFT_EYE)
        right_eye = extract_eye(landmarks, RIGHT_EYE)

        # Draw rectangles around the eyes
        cv2.rectangle(frame, (left_eye[0], left_eye[1]), (left_eye[0] + left_eye[2], left_eye[1] + left_eye[3]), (0, 255, 0), 2)
        cv2.rectangle(frame, (right_eye[0], right_eye[1]), (right_eye[0] + right_eye[2], right_eye[1] + right_eye[3]), (0, 255, 0), 2)

    # Display the frame with eye rectangles
    cv2.imshow("Eye Tracker", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
