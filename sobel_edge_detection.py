import cv2
import numpy as np
from PIL import Image
from pylab import *


def sobel_edge_dection(im):
    sobel_x  = cv2.Sobel(im, -1, 1, 0, ksize=5)
    sobel_y  = cv2.Sobel(im, -1, 0, 1, ksize=5)
    return (sobel_x, sobel_y)


if __name__ == '__main__':
    im = cv2.imread('./images/yenn.jpg', 0)
    
    sobel_x, sobel_y = sobel_edge_dection(im)
    
    figure(figsize=(15, 15))
    subplot(221, title='original')
    plt.imshow(Image.open('./images/yenn.jpg'))

    subplot(222, title='sobel_x')
    plt.imshow(sobel_x, cmap ='gray')

    subplot(223, title='sobel_y')
    plt.imshow(sobel_y, cmap ='gray')

    subplot(224, title='sobel_x + sobel_y')
    plt.imshow(sobel_x + sobel_y, cmap ='gray')
    plt.show()