import cv2


def captureImage():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print('camera is not available!')
        return None
    print(f'press s to shoot photo.\tpress q to quit.')
    while True:
        res, frame = camera.read()

        if not res:
            print('error occur on the camera!')
            break
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            path = "./images/image.jpg"
            cv2.imwrite(path, frame)

        elif key == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    captureImage()
