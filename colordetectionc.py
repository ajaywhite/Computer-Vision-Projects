import cv2
import numpy as np

# Define HSV segments with corresponding BGR colors for bounding boxes
hsv_segments = [
    {'name': 'Red1', 'lower': np.array([0, 100, 100]), 'upper': np.array([10, 255, 255]), 'bgr': (0, 0, 255)},
    {'name': 'Red2', 'lower': np.array([170, 100, 100]), 'upper': np.array([180, 255, 255]), 'bgr': (0, 0, 255)},
    {'name': 'Yellow', 'lower': np.array([25, 100, 100]), 'upper': np.array([30, 255, 255]), 'bgr': (0, 255, 255)},
    {'name': 'Green', 'lower': np.array([35, 100, 100]), 'upper': np.array([85, 255, 255]), 'bgr': (0, 255, 0)},
    {'name': 'Cyan', 'lower': np.array([80, 100, 100]), 'upper': np.array([100, 255, 255]), 'bgr': (255, 255, 0)},
    {'name': 'Blue', 'lower': np.array([94, 100, 100]), 'upper': np.array([126, 255, 255]), 'bgr': (255, 0, 0)},
    {'name': 'Purple', 'lower': np.array([130, 100, 100]), 'upper': np.array([160, 255, 255]), 'bgr': (255, 0, 255)},
    {'name': 'Pink', 'lower': np.array([160, 100, 100]), 'upper': np.array([170, 255, 255]), 'bgr': (255, 0, 255)},
    # Add more segments if needed
]

# Function to draw labels
def draw_label(frame, text, x, y, color):
    # Place the text above the bounding box, slightly offset
    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)

# Capture video from the default camera
cap = cv2.VideoCapture("C:/Users/aajay/Videos/Captures/child.mp4")

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if ret:
        # Convert the frame to HSV color space
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for segment in hsv_segments:
            # Create a mask for the current color segment
            mask = cv2.inRange(hsv_img, segment['lower'], segment['upper'])

            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw contours, bounding boxes, and labels for each detected object
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                contour_area = cv2.contourArea(cnt)
                if contour_area > 200:  # Filter out small contours
                    # Draw the bounding box with the specified BGR color
                    cv2.rectangle(frame, (x, y), (x + w, y + h), segment['bgr'], 2)
                    # Draw the label above the bounding box
                    draw_label(frame, segment['name'], x, y, segment['bgr'])

        # Display the frame with the bounding boxes and labels
        cv2.imshow("Frame", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
