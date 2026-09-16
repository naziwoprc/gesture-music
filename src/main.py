import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from gesture_recognizer import is_index_up, is_middle_up, is_ring_up, is_pinky_up

# -----------------------------
# Configuration
# -----------------------------

MODEL_PATH = "models/hand_landmarker.task"


# -----------------------------
# Create Hand Landmarker
# -----------------------------

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)

detector = vision.HandLandmarker.create_from_options(options)


# -----------------------------
# Open webcam
# -----------------------------

camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Could not open webcam.")
    exit()


# -----------------------------
# Main loop
# -----------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("Could not read frame.")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Convert OpenCV BGR → RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect hand
    result = detector.detect(mp_image)

    # Draw landmarks
    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        index = is_index_up(hand)
        middle = is_middle_up(hand)
        ring = is_ring_up(hand)
        pinky = is_pinky_up(hand)

        print(f"Index: {index}, Middle: {middle}, Ring: {ring}, Pinky: {pinky}")

        for hand in result.hand_landmarks:

            # Draw the 21 landmark points
            for landmark in hand:

                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # Draw connections between landmarks
            connections = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (0, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (5, 9),
                (9, 10),
                (10, 11),
                (11, 12),
                (9, 13),
                (13, 14),
                (14, 15),
                (15, 16),
                (13, 17),
                (17, 18),
                (18, 19),
                (19, 20),
                (0, 17),
            ]

            for start, end in connections:

                x1 = int(hand[start].x * frame.shape[1])
                y1 = int(hand[start].y * frame.shape[0])

                x2 = int(hand[end].x * frame.shape[1])
                y2 = int(hand[end].y * frame.shape[0])

                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display
    cv2.imshow("Gesture Music", frame)

    # Q → quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------

camera.release()
cv2.destroyAllWindows()
detector.close()
