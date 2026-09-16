import cv2

for index in [0, 1]:

    print(f"\nOpening camera {index}...")

    camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)

    if not camera.isOpened():
        print(f"Could not open camera {index}")
        continue

    while True:
        success, frame = camera.read()

        if not success:
            print("Could not read frame.")
            break

        cv2.imshow(f"Camera {index}", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()
