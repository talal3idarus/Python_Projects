import cv2
import numpy as np

def rgb_to_name(rgb):
    # Define some basic color ranges
    colors = {
        "red": [np.array([100, 0, 0]), np.array([255, 100, 100])],
        "green": [np.array([0, 100, 0]), np.array([100, 255, 100])],
        "blue": [np.array([0, 0, 100]), np.array([100, 100, 255])],
        "yellow": [np.array([100, 100, 0]), np.array([255, 255, 100])],
        "cyan": [np.array([0, 100, 100]), np.array([100, 255, 255])],
        "magenta": [np.array([100, 0, 100]), np.array([255, 100, 255])]
    }
    
    for color_name, (lower, upper) in colors.items():
        if np.all(lower <= rgb) and np.all(rgb <= upper):
            return color_name
    
    return "unknown"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2
    region_size = 50

    # Define the region of interest (ROI) centered around the center of the frame
    x1, y1 = max(center_x - region_size // 2, 0), max(center_y - region_size // 2, 0)
    x2, y2 = min(center_x + region_size // 2, width), min(center_y + region_size // 2, height)
    
    roi = frame[y1:y2, x1:x2]
    
    # Calculate the average color in the ROI
    avg_color = np.mean(roi, axis=(0, 1))
    avg_color_bgr = (int(avg_color[0]), int(avg_color[1]), int(avg_color[2]))
    avg_color_rgb = (avg_color_bgr[2], avg_color_bgr[1], avg_color_bgr[0])
    
    # Convert the average color to a color name
    color_name = rgb_to_name(avg_color_rgb)
    
    # Display the average color and its name on the frame
    cv2.putText(frame, f'Color: {color_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    cv2.imshow('Color Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
