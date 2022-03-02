import numpy as np
import cv2
from matplotlib import pyplot as plt

def getHistogramColor(image) :
    hist = []
    hist.append(cv2.calcHist([image], [0], None, [256], [0, 256]))
    hist.append(cv2.calcHist([image], [1], None, [256], [0, 256]))
    hist.append(cv2.calcHist([image], [2], None, [256], [0, 256]))
    return hist

def equalizeHistogramColor(image) :
    channels = cv2.split(image)
    equalizeChannels = []

    for channel in channels:
        equalizeChannels.append(cv2.equalizeHist(channel))

    equalizeImage = cv2.merge(equalizeChannels)
    return equalizeImage

def equalizeHistogramColorHSV(image):
    H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    equalizeV = cv2.equalizeHist(V)
    equalizeImage = cv2.cvtColor(cv2.merge([H, S, equalizeV]), cv2.COLOR_HSV2BGR)
    return equalizeImage
