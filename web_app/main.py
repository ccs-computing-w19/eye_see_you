import cv2

class VehicleDetect:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640) #WIDTH
        self.cap.set(4, 480) #HEIGHT

        self.face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
        self.car_cascade = cv2.CascadeClassifier('cas1.xml')
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS):" + format(self.fps))


    def dataCapture(self):
        data = 0
        for _ in range(10):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cars = self.face_cascade.detectMultiScale(gray, 1.1, 3, 0, (300,300))
            data += len(cars)
        return data/10


