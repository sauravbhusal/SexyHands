import cv2
import mediapipe as mp
capture = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumbCoordinates = (4, 2)
gesturestr= str(0)


while True:
    ret, frame = capture.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        for handLm in multiLandMarks:
            handPoints = []
            mpDraw.draw_landmarks(frame, handLm, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLm.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handPoints.append((cx, cy))


        for point in handPoints:
            print(point)
            cv2.circle(frame, point, 5, (0, 255, 255), -1)


        for coordinates in fingerCoordinates:
            if handPoints[6][1] > handPoints[8][1]:
                gesture = 1
            elif (handPoints[10][1] > handPoints[12][1]):
                gesture = 2
            else:
                gesture = 0




        cv2.putText(frame, str(gesture), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 250))

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

