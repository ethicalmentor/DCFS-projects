import cv2

def face_recog(detect, img, clr: tuple):
    for (x, y, width, length) in detect:
        cv2.rectangle(
            img,
            (x, y),
            (x + width, y + length),
            clr,
            thickness=2
        )
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

while True:
    _, frame = video_capture.read()
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_seen = face_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.4, minNeighbors=2)
    eyes_seen = eye_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.4, minNeighbors=2)
    face_recog(faces_seen, frame, (255, 255, 255))
    face_recog(eyes_seen, frame, (0, 0, 0))
    cv2.imshow('Facial recognition with OpenCV', frame)
    if cv2.waitKey(1) == 27:
        break

video_capture.release()
cv2.destroyAllWindows()
