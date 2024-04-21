import cv2

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

count = 0

# Define a video writer object
out = cv2.VideoWriter('./videos/output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640,480))

recording = False  # Flag for recording status

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    cv2.imshow("Title", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if key == ord('c'):
        cv2.imwrite(f'images//image{count}.jpg', img)
        count += 1
        print("Image Captured")

    if key == ord('v'):  # Start recording
        print("Started recording, Press 'S' to stop recording.")
        recording = True
    elif key == ord('s'):  # Stop recording
        print("Recording stopped")
        recording = False

    if recording:
        out.write(img)  # Write frames to the video file

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()