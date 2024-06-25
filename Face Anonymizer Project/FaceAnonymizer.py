import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print(("No video"))
        break

    H, W, _ = frame.shape
    print("The height and weight of the frame:",H, W)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(frame_rgb)
    if results.detections:
        for detection in results.detections:
            boxc = detection.location_data.relative_bounding_box

            x = int(boxc.xmin * W)
            y = int(boxc.ymin * H)
            w = int(boxc.width * W)
            h = int(boxc.height * H)


            print(x, y, w, h)

            #specify the region to face anonymizer
            roi = frame[y:y+h, x:x+w]

            blurred_region = cv2.GaussianBlur(roi,(35, 35), 15)

            frame[y:y+h, x:x+w] = blurred_region

            #Draw boundary box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0 , 0), 2)



    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



