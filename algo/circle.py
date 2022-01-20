class Circle(object):
    def __init__(self, x:int, y:int, r:int) -> None:
        super().__init__()
        self._x = x
        self._y = y
        self._r = r
        self._pixel_set = []

    def getPixels(self) -> list[int, int, int]:
        x = 0
        y = self._r
        p = 5/4 - self._r
        while x < y:
            self._pixel_set.append((self._x + x, self._y + y, p))
            self._pixel_set.append((self._x - x, self._y + y, p))
            self._pixel_set.append((self._x + x, self._y - y, p))
            self._pixel_set.append((self._x - x, self._y - y, p))
            self._pixel_set.append((self._x + y, self._y + x, p))
            self._pixel_set.append((self._x - y, self._y + x, p))
            self._pixel_set.append((self._x + y, self._y - x, p))
            self._pixel_set.append((self._x - y, self._y - x, p))
            if p < 0:
                x = x + 1
                p = p + 2*x + 1
            else:
                x = x + 1
                y = y - 1
                p = p + 2*(x - y) + 1
        return self._pixel_set


if __name__ == '__main__':
    o = Circle(0, 0, 2)
    circle = o.getPixels()
    print('x\ty\tp')
    for pixel in circle:
        print(f'{pixel[0]}\t{pixel[1]}\t{pixel[2]}')