import numpy as np
import cv2 as cv

image = cv.imread('result.jpg' , 0)
template1 = cv.imread('tom.jpg' , 0)
template2 = cv.imread('tom2.jpg' , 0)
template3 = cv.imread('tom3.jpg' , 0)
all = [template1,template2,template3]
for template in all:
    width , height = template.shape
    
    final = cv.matchTemplate(image , template ,cv.TM_CCOEFF_NORMED) 
    
    thresh  =  0.4
    loc = np.where(final >= thresh)
    
    for point in zip(*loc[::-1]):
        cv.rectangle(image , point , (point[0]+height ,point[1]+width) , (0 , 0 , 255) ,3)
    cv.imshow("sag",image)
    cv.waitKey(0)
    cv.destroyAllWindows()