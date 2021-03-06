from PIL import Image
from numpy import *
from scipy.misc import imsave

from PCV.tools import rof

"""
Simple example of Chan-Vese segmentation.
Load an image, segment in two classes and save result.
"""

im = array(Image.open('fisherman_tiny.jpg').convert('L')) 
U,T = rof.denoise(im,im,tolerance=0.001)
t = 0.4

imsave('result.pdf',U < t*U.max())