class BLA(object):
    '''Bresenham's line algorithm is a line drawing algorithm that
       determines the points of an n-dimensional raster that should be
       selected in order to form a close approximation to a straight
       line between two points.                 -WIKIPEDIA

       ⦿ Input:
            1. x1 = x co-ordinate of first point
            2. y1 = y co-ordinate of first point
            3. x2 = x co-ordinate of second point
            4. y2 = y co-ordinate of second point
    '''
    def __init__(self, x1:int, y1:int, x2:int, y2:int) -> None:
        super().__init__()
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._dx = x2 - x1
        self._dy = y2 - y1

        self._x_inc_sign = 1 if x2 > x1 else -1
        self._y_inc_sign = 1 if y2 > y1 else -1

        self._pixel_set = []

    def _getPixLow(self) -> list[int, int, int]:
        '''This function finds the pixel locations which approximate
           the line having slope between -1 and 1.

           ⦿ Output:
                1. a list of tuples containing x position, y position
                   and decider variable p for each pixel.          
        '''
        self._dy = self._dy * self._y_inc_sign
        p = 2*self._dy - self._dx
        y = self._y1
        for x in range(self._x1, self._x2 + 1):
            self._pixel_set.append((x, y, p))
            if p > 0:
                y += self._y_inc_sign
                p += 2 * (self._dy - self._dx)
            else:
                p += 2*self._dy
        return self._pixel_set

    def _getPixHigh(self) -> list[int, int, int]:
        '''This function finds the pixel locations which approximate
           the line having slope either less than equal to -1 or
           greater than equal to 1.

           ⦿ Output:
                1. a list of tuples containing x position, y position
                   and decider variable p for each pixel.          
        '''
        self._dx = self._dx * self._x_inc_sign
        p = 2*self._dx - self._dy
        x = self._x1
        for y in range(self._y1, self._y2 + 1):
            self._pixel_set.append((x, y, p))
            if p > 0:
                x += self._x_inc_sign
                p += 2 * (self._dx - self._dy)
            else:
                p += 2*self._dx
        return self._pixel_set

    def getPixels(self) -> list[int, int, int]:
        '''This function finds the pixel locations which approximate
           lines of all the slopes using the functions
           _getPixHigh() and _getPixLow().

           ⦿ Output:
                1. a list of tuples containing x position, y position
                   and decider variable p for each pixel.  
        '''
        if abs(self._dy) < abs(self._dx):
            if self._x1 > self._x2:
                bla = BLA(self._x2, self._y2, self._x1, self._y1)
                return bla._getPixLow()
            else:
                bla = BLA(self._x1, self._y1, self._x2, self._y2)
                return bla._getPixLow()
        else:
            if self._y1 > self._y2:
                bla = BLA(self._x2, self._y2, self._x1, self._y1)
                return bla._getPixHigh()
            else:
                bla = BLA(self._x1, self._y1, self._x2, self._y2)
                return bla._getPixHigh()


if __name__ == '__main__':
    bla = BLA(6, 16, 7, 5)
    line = bla.getPixels()
    print('x\ty\tp')
    for pixel in line:
        print(f'{pixel[0]}\t{pixel[1]}\t{pixel[2]}')