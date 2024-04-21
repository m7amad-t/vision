import cv2


def captureVideo():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print('camera is not available!')
        return None
    print(f'press r to start recording.\npress s to stop recording.\npress q to quit.\n')

    ext = cv2.VideoWriter_fourcc(*'XVID')
    path = './videos/video.avi'

    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))

    fps = 20

    videoWriter = cv2.VideoWriter(path, ext, fps, (width, height))

    isRecording = False

    while True:
        res, frame = camera.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('r'):
            print('start recording')
            isRecording = True
        elif key == ord('s'):
            isRecording = False
            print('recording is stopped')
        elif key == ord('q'):
            break

        if isRecording:
            videoWriter.write(frame)

    camera.release()
    videoWriter.release()
    cv2.destroyAllWindows()


captureVideo()
