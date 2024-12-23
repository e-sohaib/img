import numpy as np
import cv2 as cv

def noiser():
    image = cv.imread('fingerprint/result.jpg' , 0)
    #res , tresh = cv.threshold(image ,25 ,255 , cv.THRESH_OTSU)
    
    ker = np.ones((1,1) , dtype= 'uint8')
    
    #result = cv.morphologyEx(tresh , cv.MORPH_RECT, ker )
    eroded = cv.erode(image , ker , iterations=2)
    
