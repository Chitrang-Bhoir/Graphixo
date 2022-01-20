class Ellipse(object):
    def __init__(self, x:int, y:int, a:int, b:int) -> None:
        super().__init__()
        self._x = x
        self._y = y
        self._a = a
        self._b = b
        self._pixel_set = []

    def getPixels(self) -> list[int, int, int]:
        x = 0
        y = self._b
        p = self._b*self._b - self._a*self._a*self._b + 0.25*self._a*self._a
        dx = 2 * self._b * self._b * x
        dy = 2 * self._a * self._a * y
        while dx < dy:
            self._pixel_set.append((x + self._x, y + self._y, p))
            self._pixel_set.append((-x + self._x, y + self._y, p))
            self._pixel_set.append((x + self._x, -y + self._y, p))
            self._pixel_set.append((-x + self._x, -y + self._y, p))
            if p < 0:
                x = x + 1
                dx = dx + 2*self._b*self._b
                p = p + dx + self._b*self._b
            else:
                x = x + 1
                y = y - 1
                dx = dx + 2*self._b*self._b
                dy = dy - 2*self._a*self._a
                p = p + dx - dy + self._b*self._b
        while y >= 0:
            self._pixel_set.append((x + self._x, y + self._y, p))
            self._pixel_set.append((-x + self._x, y + self._y, p))
            self._pixel_set.append((x + self._x, -y + self._y, p))
            self._pixel_set.append((-x + self._x, -y + self._y, p))
            if p > 0:
                y = y - 1
                dy = dy - 2*self._a*self._a
                p = p + self._a*self._a - dy
            else:
                y = y - 1
                x = x + 1
                dx = dx + 2*self._b*self._b
                dy = dy - 2*self._a*self._a
                p = p + dx - dy + self._a*self._a
        return self._pixel_set


if __name__ == '__main__':
    o = Ellipse(0, 0, 2, 3)
    ellipse = o.getPixels()
    print('x\ty\tp')
    for pixel in ellipse:
        print(f'{pixel[0]}\t{pixel[1]}\t{pixel[2]}')