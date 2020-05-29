from PIL import Image
from PIL import ImageFilter
from pylab import *


def contour(im):
    return im.filter(ImageFilter.CONTOUR)

def detail(im):
    return im.filter(ImageFilter.DETAIL)

def edge_enhance(im):
    return im.filter(ImageFilter.EDGE_ENHANCE)

def edge_enhance_more(im):
    return im.filter(ImageFilter.EDGE_ENHANCE_MORE)

def embosse(im):
    return im.filter(ImageFilter.EMBOSS)

def find_edges(im):
    return im.filter(ImageFilter.FIND_EDGES)

def smooth(im):
    return im.filter(ImageFilter.SMOOTH)

def smooth_more(im):
    return im.filter(ImageFilter.SMOOTH_MORE)

def sharpen(im):
    return im.filter(ImageFilter.SHARPEN)

def custom_filter(im, size, kernel):
    ker = ImageFilter.Kernel(size, kernel, scale=None, offset=0)
    return im.filter(ker)


if __name__ == '__main__':
    im = Image.open('./images/flowers.jpg')
    figure(figsize=(15, 15))
    subplots_adjust(hspace=0.3)
    
    subplot(431, title='original')
    imshow(im)
    
    funcs = [
        contour, detail, edge_enhance, 
        edge_enhance_more, embosse, find_edges,
        smooth, smooth_more, sharpen,
    ]
    for i, func in enumerate(funcs, 2):
        subplot(4, 3, i, title=func.__name__)
        imshow(func(im))
        
    subplot(4, 3, 11, title='custom_filter')
    imshow(custom_filter(im, size=(3, 3), kernel=[1,1,1,1,-1,1,-1,-1,-1]))

    show()