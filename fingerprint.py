import cv2 as cv
import numpy as np
def finger(image_name):
    im = cv.imread(f'fingerprint/{image_name}' , cv.IMREAD_COLOR)
    image = cv.cvtColor(im , cv.COLOR_BGR2GRAY)
    #image_gray = cv.cvtColor(image , cv.COLOR_BGR2GRAY)
    tresh = cv.adaptiveThreshold(image , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY ,15 ,0.5)
    T = cv.resize(tresh , (500 , 600))
    
    #image2 = cv.imread('photo_2024-12-16_15-18-18.jpg' , cv.IMREAD_UNCHANGED)
    #cv.line(image , (0,0) ,(1000,1000) , (55,255,0) , thickness=5)
    #cv.putText(image ,"BCD" ,(200 , 200) , cv.FONT_HERSHEY_TRIPLEX,3 ,(0 , 250 ,250))
    
    
    cv.imwrite(f"res-{image_name}")