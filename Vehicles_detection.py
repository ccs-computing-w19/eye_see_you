# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
cap = cv2.VideoCapture('ccsbuilding-no-span.mp4')
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cas1.xml')

total = 0
frame = 0

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 3, 0, (300,300))
    #print(len(cars))

    # CALCULATE AVERAGE NUMBER OF CARS EVERY 10 FRAMES
    total += len(cars)
    frame += 1
    print(int((total/frame) + 0.5))

    if (frame >= 30):
        frame = 0
        total = 0

    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

   # Display frames in a window
    cv2.imshow('video2', frames)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
