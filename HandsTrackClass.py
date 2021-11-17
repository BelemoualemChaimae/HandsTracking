# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 00:00:19 2021

@author:  Computer Vision Seniorita Chama
"""

# Framework MediaPipe is a Framwork which is developped By Google 

# Hand Track is uses two main module in the backend 
         # -- Palm detection (is used to crop the image from original image )
         # --Hand landmarks is a model used to find the 20 landmark within a hand 
        
        
import cv2 as cv
import mediapipe as mp 
import time

from datetime import datetime





class HandDetector():
    
    def __init__(self,mode=False,nbr_hands=10,model=1,detection_confidence=0.5,tracking_confidence=0.5):
        self.mode=mode
        self.nbr_hands=nbr_hands
        self.model=model
        self.detection_confidence=detection_confidence
        self.tracking_confidence=tracking_confidence
        
        
        self.mpHand=mp.solutions.hands
        self.hands=self.mpHand.Hands(self.mode,self.nbr_hands,self.model,self.detection_confidence,self.tracking_confidence)
        self.mpDraw=mp.solutions.drawing_utils
    
    
    def findHandz(self,img):
        
        #date 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cv.putText(img,str(current_time),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
        imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        result=self.hands.process(imgRGB)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img,hand_landmarks,self.mpHand.HAND_CONNECTIONS)
                #Getting the information of landmarks from 0- 20 
                
                for id , lm in enumerate(hand_landmarks.landmark) :
                    h,w,b=img.shape
                    x,y=int(lm.x*w),int(lm.y*h)
                    print(id,x,y)
                    if id ==12: 
                        cv.circle(img,(x,y),5,(255,255,255),cv.FILLED) 
                        
     
        
        return img
        
    
    
       

if __name__=='__main__' : 
    cap=cv.VideoCapture(0) 
    Handz=HandDetector()
    Ctime=0
    Ptime=0
    fps =0
    while True : 
        success,img=cap.read()
        img=Handz.findHandz(img)
        Ctime=time.time()
        fps=1/(Ctime-Ptime)
        Ptime=Ctime
        
        #cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv.imshow('Image',img)
        if cv.waitKey(1) & 0xFF == ord('q'):
          break
            
        
        