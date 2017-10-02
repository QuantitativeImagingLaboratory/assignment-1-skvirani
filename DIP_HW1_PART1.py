__author__ = "Samad Virani"
__email__ = "skvirani2@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
from resize import resample as rs
from datetime import datetime

def display_image(window_name, image):
    """This function will display an image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def main():
    #parses input arguments
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-fx", "--resize_x", dest="resize_x",
                        help="specify scale size (fx)", metavar="RESAMPLE SIZE")
    parser.add_argument("-fy", "--resize_y", dest="resize_y",
                        help="specify scale size (fy)", metavar="RESAMPLE SIZE")
    parser.add_argument("-m", "--interpolation", dest="interpolate",
                        help="specify the interpolation method (nearest_neighbor or bilinear)", metavar="INTERPOLATION METHOD")

    args = parser.parse_args()

    if args.image is None:
        print("Please specify the name of the image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    if args.resize_x is None:
        print("Resize scale fx not specified using default (1.5)")
        print ("use the -h option to see usage information")
        fx = 1.5
    else:
        fx = args.resize_x

    if args.resize_y is None:
        print("Resize scale fy not specified using default (1.5)")
        print("use the -h option to see usage information")
        fy = 1.5
    else:
        fx = args.resize_y


    if args.interpolate is None:
        print("Interpolation method not specified, using default=nearest_neighbor")
        print("use the -h option to see usage information")
        interpolation = "nearest_neighbor"

    else:
        if args.interpolate not in ["nearest_neighbor", "bilinear"]:
            print("Invalid interpolation method, using default=nearest_neighbor")
            print("use the -h option to see usage information")
            interpolation = "nearest_neighbor"
        else:
            interpolation = args.interpolate

    outputDir = 'output/resize/'

    output_image_name = outputDir+image_name+interpolation+datetime.now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(output_image_name, resampled_image)
