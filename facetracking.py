# By_SciCraft
import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np

cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

port = "COM3"
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s')  # Pin 9 Arduino
servo_pinY = board.get_pin('d:10:s')  # Pin 10 Arduino

detector = FaceDetector()
servoPos = [90, 90]  # Initial servo position

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        # Get the coordinates
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]

        # Convert coordinates to servo degrees
        servoX = np.interp(fx, [0, ws], [180, 0])
        servoY = np.interp(fy, [0, hs], [180, 0])
        servoX = max(0, min(180, servoX))  # Clamp servoX to 0-180
        servoY = max(0, min(180, servoY))  # Clamp servoY to 0-180

        servoPos[0] = servoX
        servoPos[1] = servoY

        # Draw target information
        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)  # Red circle
        cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # Blue text
        cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # Black x-line
        cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # Black y-line
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)  # Filled red circle
        cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)  # Red text

    else:
        # No face detected
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)  # Red text
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)  # Red circle
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)  # Filled red circle
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)  # Black x-line
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)  # Black y-line

    # Display servo angles
    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # Blue text
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # Blue text

    # Send angles to servos
    servo_pinX.write(servoPos[0])
    servo_pinY.write(servoPos[1])

    # Display the frame
    cv2.imshow("Face Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
