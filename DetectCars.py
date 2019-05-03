#Detect a moving car first and chck if whether it has pass the line given the robot signal
import cv2
import os
import datetime

filename = "Videos/_video1.avi"
# filename = "Videos/_downhill.mp4"
# print(filename)

# exit()
camera = cv2.VideoCapture(filename)
# camera = cv2.VideoCapture("Plates_short.mkv")
camera.open(filename)
# camera.open("Plates_short.mkv")
car_cascade = cv2.CascadeClassifier('cars.xml')
while True:
    (grabbed, frame) = camera.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
    # x = 0
    # for car in cars:
    #     carfile = "/car_images/car" + str(x) + ".jpg"
    #     cv2.imwrite(carfile, car)
    for (x,y,w,h) in cars:
     cv2.rectangle(frame, (x, y), (x + w, y + h), (105, 105, 105), 1)
     car = frame[y:y+h, x:x+w] # Getting car only from whole frame

     now = datetime.datetime.now()
     currentDate = str(now.day) + "_" + str(now.month) + "_" + str(now.year) + "_" + str(now.time())

     carfile = "car_images/car" + currentDate + ".jpg"
     cv2.imwrite(carfile, car)

     #### CODE TO CHECK IF RULES VIOLATED GO HERE!!!!!!!!!!!!!!!!!
     # code to delete file after use
     cv2.imshow("video", frame)
    if cv2.waitKey(1)== ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
