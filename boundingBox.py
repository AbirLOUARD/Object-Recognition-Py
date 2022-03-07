import cv2
import numpy as np

class BB :
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

def findAndDrawBB(imageWithDifferences, imageOriginal, imageToDraw, imageFloorRegion, valeurPixelFloor):
    listBB = []
    compteurBB = 0
    gray = cv2.cvtColor(imageWithDifferences, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)

        # Check if BB is interesting (big)
        if (w > 20 or h > 20) :
            listBB.append(BB(x,y,w,h))

    #Eliminer les box contenues dans une autre box
    for box1 in listBB :
        for box2 in listBB :
            if (box1 != box2) :
                if ((box1.x > box2.x) and (box1.x < (box2.x + box2.w))) :
                    if ((box1.y > box2.y) and (box1.y < (box2.y + box2.h))) :
                        if (box1 in listBB) :
                            listBB.pop(listBB.index(box1))

    """
    #Chercher box sur le sol
    for box in listBB :
        moyValeurPixel = 0
        nbrPixel = 0
        for yPos in range(box.x, box.x + box.w) :
            for xPos in range(box.y, box.y + box.h) :
                moyValeurPixel += imageFloorRegion.item(xPos, yPos)
                nbrPixel += 1
        moyValeurPixel //= nbrPixel
        if (moyValeurPixel != valeurPixelFloor) :
            listBB.pop(listBB.index(box))
    """


    #Chercher box sur le sol 2
    for box in listBB :
        if (box.y + box.h < thresh.shape[0] // 2 ) :
            listBB.pop(listBB.index(box))
    


    for b in listBB:
        compteurBB += 1
        cv2.rectangle(imageToDraw, (b.x, b.y), (b.x + b.w, b.y + b.h), (0,255,0), 2)
        cv2.rectangle(imageOriginal, (b.x, b.y), (b.x + b.w, b.y + b.h), (0,255,0), 2)

    return compteurBB


"""
def findAndDrawBBGRAY(imageWithDifferences, imageToDraw):
    thresh = cv2.threshold(imageWithDifferences, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        # Check if BB is interesting (big)
        if (w > 20 or h > 20) :
            cv2.rectangle(imageToDraw, (x, y), (x + w, y + h), (0,255,0), 2)

    return imageToDraw
"""
