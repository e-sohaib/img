import numpy as np
import cv2 as cv

def featchemach():
    template = cv.imread('tom.jpg' , 0)
    image = cv.imread('result.jpg' , 0)
    
    orb = cv.ORB.create(nfeatures=1000)
    
    
    X , Y = orb.detectAndCompute(template , None)
    A , B = orb.detectAndCompute(image , None)
    
    bf = cv.BFMatcher(cv.NORM_HAMMING , crossCheck=None)
    
    maches = bf.match(Y , B , None)
    
    maches = sorted(maches , key = lambda x : x.distance )
    
    new_image = cv.drawMatches(template , X ,image , A ,maches[:102] ,None ,flags=2)
    