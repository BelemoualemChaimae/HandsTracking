# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:34:24 2021

@author: Computer Vision Seniorita Chama
"""

# Framework MediaPipe is a Framwork which is developped By Google 

# Hand Track is uses two main module in the backend 
         # -- Palm detection (is used to crop the image from original image )
         # --Hand landmarks is a model used to find the 20 landmark within a hand 
        
        
import cv2 as cv
import mediapipe as mp 
import time

cap=cv.VideoCapture(0) 
mpHand=mp.solutions.hands
hands=mpHand.Hands()
mpDraw=mp.solutions.drawing_utils
Ctime=0
Ptime=0
fps =0
while True : 
    success,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result=hands.process(imgRGB)
    #print(result.multi_hand_landmarks) # To test if hand is tracked or nCafé New York BudapestotYet
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,hand_landmarks,mpHand.HAND_CONNECTIONS)
            #Getting the information of landmarks from 0- 20 
            
            for id , lm in enumerate(hand_landmarks.landmark) :
                h,w,b=img.shape
                x,y=int(lm.x*w),int(lm.y*h)
                print(id,x,y)
                if id ==12: 
                    cv.circle(img,(x,y),25,(255,255,255),cv.FILLED) 
    
    
    
    Ctime=time.time()
    fps=1/(Ctime-Ptime)
    Ptime=Ctime
    
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
    cv.imshow('Image',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
          break
   

