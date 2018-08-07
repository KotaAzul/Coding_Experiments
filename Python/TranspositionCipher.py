import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour


def main(message, key):
    message = message.upper()
    message = message.replace(" ", "")
    cipherText = transpositionCipher(message, key)

    print(cipherText)


def transpositionCipher(message, key):
    cipherText = [""] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key

    print(cipherText)
    return "".join(cipherText)


main("helpmepleasewearealloutofmilk!", 8)
