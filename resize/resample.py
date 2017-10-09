import numpy as np
import math


class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fy: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        # output_image = cv2.resize(image, (0,0), fx=self.fx, fy=self.fy,interpolation=cv2.INTER_NEAREST)
        (height, width) = image.shape
        newheight = height * float(fy)
        newwidth = width * float(fx)
        heightratio = height/newheight
        widthratio = width/newwidth

        output_image = np.ones((int(newheight),int(newwidth)), np.uint8)*255
        #print(output_image.shape)
        #print(image.shape)

        #use round after applying the ratios
        #get intensity of the old pixels and set to new pixels
        for col in range(output_image.shape[0]):
            for row in range(output_image.shape[1]):
                mappedcol = round(col*heightratio)
                mappedrow = round(row*widthratio)
                if mappedcol == height:
                    mappedcol = height-1
                if mappedrow == width:
                    mappedrow = width-1
                output_image[col,row] = image[mappedcol,mappedrow]


        return output_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """
        from . import interpolation as inter
        bi = inter.interpolation()
        # Write your code for bilinear interpolation here
        (height, width) = image.shape
        newh = height * float(fy)
        neww = width * float(fx)
        hratio = height/newh
        wratio = width/neww

        output = np.ones((int(newh),int(neww)), np.uint8)*255
        for col in range(output.shape[0]):
            for row in range(output .shape[1]):
                mapcol = col * hratio
                maprow = row * wratio
                x1 = math.floor(mapcol)
                x2 = math.ceil(maprow)
                y1 = math.floor(mapcol)
                y2 = math.ceil(maprow)

                if x1 == mapcol:
                    x1 = x1 - 1
                if x2 == mapcol:
                    x2 = x2 - 1
                if y1 == maprow:
                    y1 = y1 - 1
                if y2 == maprow:
                    y2 = y2 - 1

                pt1 = (x1, y1, image[x1, y1])
                pt2 = (x1, y2, image[x1, y2])
                pt3 = (x2, y1, image[x2, y1])
                pt4 = (x2, y2, image[x2, y2])
                unknown = (mapcol, maprow, output[col, row])
                output[row,col] = bi.bilinear_interpolation(pt1,pt2,pt3,pt4,unknown)

        return output



