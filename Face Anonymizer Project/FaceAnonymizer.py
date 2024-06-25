import cv2
import mediapipe as mp


#Initialize MediaPipe face detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()

#Open videocapture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print(("No video"))
        break

    #Get the dimension of frame
    H, W, _ = frame.shape
    print("The height and weight of the frame:",H, W)

    #convert color BGR to RGB as MediaPipe require RGB input
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #process the frame the face detection
    results = face_detection.process(frame_rgb)
    if results.detections:
        for detection in results.detections:
            boxc = detection.location_data.relative_bounding_box

            x = int(boxc.xmin * W)
            y = int(boxc.ymin * H)
            w = int(boxc.width * W)
            h = int(boxc.height * H)


            print(x, y, w, h)

            #check frame dimension
             x = int(boxc.xmin * W)
            y = int(boxc.ymin * H)
            w = int(boxc.width * W)
            h = int(boxc.height * H)


            #specify the region to face anonymizer
            roi = frame[y:y+h, x:x+w]

            #blurring using GaussianBlur
            blurred_region = cv2.GaussianBlur(roi,(35, 35), 15)

            #Back to the original frame
            frame[y:y+h, x:x+w] = blurred_region

            #Draw boundary box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0 , 0), 2)


    #Display the frame
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



