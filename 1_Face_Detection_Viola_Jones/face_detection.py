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

def detect(frame, gray):

    #face locations are detected
    faces = face_detector.detectMultiScale(gray, 1.3, 3)
    
    for (x, y, w, h) in faces:

        #creating a rectangle across the human frontal face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        
    return frame


def main():

    #reading the images from the folder
    base_path = os.path.dirname(os.path.abspath(__file__))

    #location of dataset
    img_path = os.path.join(base_path, "Dataset")

    #location to create output images
    output_path = os.path.join(base_path, "Output")
    
    for file in os.listdir(os.path.join(base_path, "Dataset")):

        #Take an image
        img = cv2.imread(os.path.join(img_path, file))

        #Creating gray image for processing with viola jones algorithm
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #calling function that detects location of face
        output_img = detect(img, gray_img)

        #saving the output image
        cv2.imwrite(os.path.join(output_path, file), output_img)
        
    print("Face detection finished !")
    
if __name__ == "__main__":
    
    main()