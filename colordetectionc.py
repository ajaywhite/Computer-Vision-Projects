import cv2
import numpy as np

# Define the yellow color range in HSV (adjust as needed)
lower_yellow = np.array([25, 100, 200])
upper_yellow = np.array([35, 255, 255])

# Capture video from the default camera
cap = cv2.VideoCapture(0)

# Video is started to run
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if ret:
        # Convert the frame to HSV color space
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for yellow color
        mask = cv2.inRange(hsv_img, lower_yellow, upper_yellow)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        # Draw contours and bounding boxes around detected yellow objects
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            contour_area = cv2.contourArea(cnt)
            if contour_area > 150:  # Filter out small contours
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        # Display the frame with the bounding box
        cv2.imshow("Frame", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
