import numpy as np
import cv2 as cv

def noise():
    image = cv.imread('2.jpg' , 0)
    res , tresh = cv.threshold(image ,50 ,255 , cv.THRESH_OTSU)
    
    ker = np.ones((2,2) , dtype= 'uint8')
    result = cv.morphologyEx(tresh , cv.MORPH_RECT, ker )
    
    
    cv.imwrite('result.jpg',tresh)
    
    