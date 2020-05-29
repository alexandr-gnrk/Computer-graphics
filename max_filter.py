import scipy.ndimage
import scipy.misc
from PIL import Image
from pylab import *


def max_filter(im):
    b = scipy.ndimage.filters.maximum_filter(
        im, size=5, footprint=None, 
        output=None, mode ='reflect',cval=0.0,origin=0)
    return Image.fromarray(b)


if __name__ == '__main__':
    im = Image.open('./images/watermelon.jpg')
    figure(figsize=(15, 15))
    subplots_adjust(hspace=0.3)

    subplot(121, title='original')
    imshow(im)
    subplot(122, title='max_filter')
    imshow(max_filter(im))

    show()