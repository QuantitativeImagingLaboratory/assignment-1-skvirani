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
        newheight = int(image.shape[0]*fy)
        newwidth = int(image.shape[1]*fx)
        height = int(image.shape[0])
        width = int(image.shape[1])
        heightratio = height/newheight
        widthratio = width/newwidth

        output_image = np.ones((newheight,newwidth), np.uint8)*255

        #output_image = cv2.resize(image, (0,0), fx=self.fx, fy=self.fy,interpolation=cv2.INTER_NEAREST)

        #use round after applying the ratios
        #get intensity of the old pixels and set to new pixels
        for col in range(output_image.shape[0]):
            for row in range(output_image.shape[1]):
                output_image = np.ones((col*fy,row*fx), npuint8)*255
                if output_image

        return output_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        output_image = image.copy()
        output_image = cv2.resize(image, (0,0), fx=self.fx, fy=self.fy, interpolation=cv2.INTER_LINEAR)
        return image
