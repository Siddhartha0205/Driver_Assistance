# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:26:08 2024

@author: sidne
"""

#importing libraries
import cv2
import os

#import the cascade
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_detector = cv2.CascadeClassifier("haarcascade_eye.xml")

def detect(frame, gray):

    #face locations are detected
    faces = face_detector.detectMultiScale(gray, 1.3, 3)
    
    for (x, y, w, h) in faces:

        #creating a rectangle across the human frontal face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

        gray_roi = gray[y:y+h, x:x+w]
        color_roi = frame[y:y+h, x:x+w]

        # detecting location of Human eyes
        eyes = eyes_detector.detectMultiScale(gray_roi, 1.1, 3)

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(color_roi, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
        
    return frame


def main():

    #selecting camera
    cap = cv2.VideoCapture(0)

    while True:

        #reading input data
        ret, frame = cap.read()

        #converting input signal to gray format
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # calling function that detects location of face
        output_img = detect(frame, gray_frame)

        #Display of processed output
        cv2.imshow("Live Feed", output_img)

        #Close the process when key 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
        
    print("Face detection and Eye detection closed !")
    
if __name__ == "__main__":
    
    main()