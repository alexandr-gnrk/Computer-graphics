from PIL import Image
from pylab import *


def negative(im_arr):
    return 255 - im_arr

def clamp_to_interval(im_arr, from_, to):
    return ((to - from_) / 255 * im + from_).astype(np.uint8)

def darker(im_arr, degree):
    return (255 * (im / 255)**degree).astype(np.uint8)


if __name__ == '__main__':
    im = array(Image.open('./images/gosha.jpg').convert('L'))
    figure(figsize=(15, 15))
    subplots_adjust(hspace=0.3)

    gray()
    subplot(221, title='original')
    imshow(im)
    subplot(222, title='negative')
    imshow(negative(im))
    
    subplot(223, title='clamp_to_interval')
    imshow(clamp_to_interval(im, 240, 255))
    
    subplot(224, title='darker')
    imshow(darker(im, 3))
    show()
