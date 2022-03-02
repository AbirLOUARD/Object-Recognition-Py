import argparse
import cv2
import utils
import histogram
import boundingBox
import threshold
import os

def processing(pathFolder, ref, cmp) :
    image1 = cv2.imread(pathFolder + "/" + ref)
    image2 = cv2.imread(pathFolder + "/" + cmp)

    image1, image2 = utils.resizeImages(image1, image2)

    #Rechercher le sol de la photo
    imageFloorRegion, valeurPixelFloor = threshold.findFloor(image1)


    image1Equalized = histogram.equalizeHistogramColor(image1)
    image2Equalized = histogram.equalizeHistogramColor(image2)

    image2Equalized = utils.filterBright(image2Equalized)
    image1Equalized = utils.filterBright(image1Equalized)


    """
    image1Equalized = histogram.equalizeHistogramColorHSV(image1)
    image2Equalized = histogram.equalizeHistogramColorHSV(image2)
    """


    """
    image1Gray = cv2.cvtColor(image1Equalized, cv2.COLOR_BGR2GRAY)
    image2Gray = cv2.cvtColor(image2Equalized, cv2.COLOR_BGR2GRAY)
    image2WithDifferencesGRAY = utils.foundDifferencesBetweenImagesGRAY(image1Gray, image2Gray, 75)
    imageDifferencesThreshGRAY = utils.threshDifferencesGRAY(image2WithDifferencesGRAY)
    imageBB = boundingBox.findAndDrawBBGRAY(imageDifferencesThreshGRAY, image2)
    """


    image2WithDifferences = utils.foundDifferencesBetweenImagesHSV(image1Equalized, image2Equalized, 75)
    imageDifferencesThresh = utils.threshDifferences(image2WithDifferences)
    nombreBB = boundingBox.findAndDrawBB(imageDifferencesThresh, image1, image2, imageFloorRegion, valeurPixelFloor)

    utils.displayBothImages(image1, image2, nombreBB)
    cv2.waitKey(0)
    cv2.destroyAllWindows


def main():
    args = utils.parserInitialisation()

    pathFolder = args["pathFolder"]
    directory = os.fsencode(pathFolder)

    listImageToCompare = []

    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         if (filename.startswith("Reference") and (filename.endswith(".JPG") or filename.endswith(".jpg"))) :
             reference = file.decode("utf-8")
         elif filename.endswith(".JPG") or filename.endswith(".jpg"):
             listImageToCompare.append(file.decode("utf-8"))
             continue
         else:
             continue

    for image in listImageToCompare :
        processing(pathFolder, reference, image)


if __name__ == "__main__":
    main()
