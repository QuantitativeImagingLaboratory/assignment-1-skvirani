class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        #pt1,pt2,unknown hold two pieces of data, first we have the coordinate and second we have the intensity of the pixel
        #returns the intensity of the pixel
        #formula from lecture notes of linear interpolation

        intensity = (pt1[1] * (pt2[0] - unknown[0])) / (pt2[0] - pt1[0]) + (pt2[1] * (unknown[0] - pt1[0])) / ( pt2[0] - pt1[0])

        return intensity

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        #pt1,pt2,pt3,pt4,unknown hold 3 pieces of data, first/second we have the coordinates and last we have the intensity of the pixel
        #returns the intensity of the unknown pixel
        if pt1[0] == pt3[0]:
            R1 = self.linear_interpolation((pt1[1],pt1[2]),(pt3[1],pt3[2]),(unknown[1],unknown[2]))
        elif pt1[1] == pt3[1]:
            R1 = self.linear_interpolation((pt1[0],pt1[2]),(pt3[0],pt3[2]),(unknown[0],unknown[2]))
        if pt2[0] == pt4[0]:
            R2 = self.linear_interpolation((pt2[1],pt2[2]),(pt4[1],pt4[2]),(unknown[1],unknown[2]))
        elif pt2[1] == pt4[1]:
            R2 = self.linear_interpolation((pt2[0],pt2[2]),(pt4[0],pt4[2]),(unknown[0],unknown[2]))
        P = self.linear_interpolation((pt1[1],R1),(pt2[1],R2),(unknown[1],unknown[2]))
        return P
