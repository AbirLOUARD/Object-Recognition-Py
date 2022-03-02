import cv2

def findFloor(image) :
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    copyImage = imageGray.copy()
    x1 = imageGray.shape[0]
    y1 = imageGray.shape[1]

    for i in range(x1) :
        for j in range(y1) :
            pixel = imageGray.item(i, j)
            if (pixel < 50) :
                imageGray.itemset((i,j), 0)
            elif (pixel >= 50 and pixel < 100) :
                imageGray.itemset((i,j), 50)
            elif (pixel >= 100 and pixel < 150) :
                imageGray.itemset((i,j), 100)
            elif (pixel >= 150 and pixel < 200) :
                imageGray.itemset((i,j), 150)
            elif (pixel >= 200 and pixel <= 255) :
                imageGray.itemset((i,j), 200)

    valeurPixelFloor = imageGray.item(x1//2, y1-1)
    return imageGray, valeurPixelFloor
