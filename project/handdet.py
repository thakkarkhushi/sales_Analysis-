import cv2
from cvzone.HandTrackingModule import HandDetector

# Setup
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Open webcam
cap = cv2.VideoCapture(0)

print("✅ Starting... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)

    # Detect hands
    hands, frame = detector.findHands(frame)  # draws landmarks automatically

    if hands:
        cv2.putText(frame, "Hand Detected!", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "No Hand", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()