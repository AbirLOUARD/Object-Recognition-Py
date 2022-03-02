import argparse
import cv2
import matplotlib.pyplot as plt

def parserInitialisation() :
    parser = argparse.ArgumentParser()
    parser.add_argument("pathFolder", help = "path to the images folder")
    #parser.add_argument("pathImageToCompare", help = "path to reference image")
    args = vars(parser.parse_args())
    return args

def resizeImages(image1, image2) :
    resizedImage1 =  cv2.resize(image1, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
    resizedImage2 =  cv2.resize(image2, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
    return resizedImage1, resizedImage2

def displayBothImages(image1, image2, nombreBB) :
    b1, g1, r1 = cv2.split(image1)
    b2, g2, r2 = cv2.split(image2)
    image1PLT = cv2.merge([r1, g1, b1])
    image2PLT = cv2.merge([r2, g2, b2])
    plt.subplot(121)
    plt.imshow(image1PLT)
    plt.title("Pièce rangée")
    plt.subplot(122)
    plt.imshow(image2PLT)
    plt.title("Niveau d'encombrement : " + str(nombreBB))
    plt.show()

def filterBright(image) :
    alpha = 1
    beta = 0
    res = cv2.multiply(image, alpha)
    res = cv2.add(res, beta)
    return res

def foundDifferencesBetweenImages(image1, image2, thresh) :
    x1 = image1.shape[0]
    y1 = image1.shape[1]
    x2 = image2.shape[0]
    y2 = image2.shape[1]

    if ((x1 != x2) or (y1 != y2)) :
        print("ERROR : def foundDifferencesBetweenImages(image1, image2)")

    for i in range(x1) :
        for j in range(y1) :
            compareOnB = abs(image1.item(i, j, 0) - image2.item(i, j, 0))
            compareOnG = abs(image1.item(i, j, 1) - image2.item(i, j, 1))
            compareOnR = abs(image1.item(i, j, 2) - image2.item(i, j, 2))
            if (compareOnB > thresh or compareOnG > thresh or compareOnR > thresh) :
                image2[i, j] = [255, 0, 255]

    return image2

def foundDifferencesBetweenImagesHSV(image1, image2, thresh) :
    x1 = image1.shape[0]
    y1 = image1.shape[1]
    x2 = image2.shape[0]
    y2 = image2.shape[1]

    if ((x1 != x2) or (y1 != y2)) :
        print("ERROR : def foundDifferencesBetweenImages(image1, image2)")

    image1HSV = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    image2HSV = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    for i in range(x1) :
        for j in range(y1) :
            compareOnH = abs(image1.item(i, j, 0) - image2.item(i, j, 0))
            compareOnS = abs(image1.item(i, j, 1) - image2.item(i, j, 1))
            if (compareOnH > thresh or compareOnS > thresh) :
                image2[i, j] = [255, 0, 255]

    return image2

def threshDifferences(image) :
    x1 = image.shape[0]
    y1 = image.shape[1]

    for i in range(x1) :
        for j in range(y1) :
            B = image.item(i, j, 0)
            G = image.item(i, j, 1)
            R = image.item(i, j, 2)
            if (B == 255 and G == 0 and R == 255) :
                image[i, j] = [0, 0, 0]
            else :
                image[i, j] = [255, 255, 255]

    return image

"""
def foundDifferencesBetweenImagesGRAY(image1, image2, thresh) :
    x1 = image1.shape[0]
    y1 = image1.shape[1]
    x2 = image2.shape[0]
    y2 = image2.shape[1]

    if ((x1 != x2) or (y1 != y2)) :
        print("ERROR : def foundDifferencesBetweenImages(image1, image2)")

    for i in range(x1) :
        for j in range(y1) :
            compare = abs(image1.item(i, j) - image2.item(i, j))
            if (compare > thresh) :
                image2[i, j] = 0

    return image2

def threshDifferencesGRAY(image) :
    x1 = image.shape[0]
    y1 = image.shape[1]

    for i in range(x1) :
        for j in range(y1) :
            pixel = image.item(i, j)
            if (pixel == 0) :
                image[i, j] = 0
            else :
                image[i, j] = 255

    return image
"""
