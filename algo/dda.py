class DDA(object):
    '''For generating any line segment we need intermediate points and
       for calculating them we can use a basic algorithm called DDA
       (Digital differential analyzer) line generating algorithm.
                                            -GEEKSFORGEEKS
    
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

        self._dx = abs(x2 - x1)
        self._dy = abs(y2 - y1)

        self._x_inc_sign = 1 if x2 > x1 else -1
        self._y_inc_sign = 1 if y2 > y1 else -1

        self._pixel_set = []

    def getPixels(self) -> list[int, int, int, int]:
        '''This function finds the pixel locations which approximate
           lines by running through the longest directions step by step
           and calculating the location of each pixel in the other
           direction.

           ⦿ Output:
                1. a list of tuples containing x position, y position
                   as floats precise till 2 digits and their values
                   rounded to nearest integers.  
        '''
        if self._dx >= self._dy:
            step = self._dx
        else:
            step = self._dy
        self._dx /= step
        self._dy /= step
        x = self._x1
        y = self._y1
        for i in range(step + 1):
            self._pixel_set.append((round(x, 2), round(y, 2), 
                                   round(x), round(y)))
            x += self._dx * self._x_inc_sign
            y += self._dy * self._y_inc_sign
        return self._pixel_set


if __name__ == '__main__':
    dda = DDA(0, 7, 7, 0)
    line = dda.getPixels()
    print('x\ty\tx-plot\ty-plot')
    for pixel in line:
        print(f'{pixel[0]}\t{pixel[1]}\t{pixel[2]}\t{pixel[3]}')