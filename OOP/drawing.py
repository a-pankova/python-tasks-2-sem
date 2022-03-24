class Drawing:

    def __init__(self, columns, rows, symbol):
        self.image = [[symbol] * columns for i in range(rows)]

    def print(self):
        for row in self.image:
            for elem in row:
                print(elem, end=' ')
            print()
        print('\n')

    def setPoint(self, x, y, char):
        self.image[x][y] = char

    def drawHorizontalLine(self, row, char, start=0, end=None):
        if end is None:
            end = len(self.image[row])
        for i in range(start, end):
            self.image[row][i] = char

    def drawVerticalLine(self, col, char, start=0, end=None):
        if end is None:
            end = len(self.image)
        for i in range(start, end):
            self.image[i][col] = char

    def drawRectangle(self, x1, y1, x2, y2, char):
        self.drawHorizontalLine(x1, char, min(y1, y2), max(y1, y2)+1)
        self.drawHorizontalLine(x2, char, min(y1, y2), max(y1, y2)+1)
        self.drawVerticalLine(y1, char, min(x1, x2), max(x1, x2))
        self.drawVerticalLine(y2, char, min(x1, x2), max(x1, x2))

    def draw_line(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, char = '*'):
        dx = x2 - x1
        dy = y2 - y1
        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy
        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        x, y = x1, y1
        error, t = el / 2, 0
        self.setPoint(x, y, char)
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.setPoint(x, y, char)

    def drawCircle(self, r, x1, y1, char):
        x = 0
        y = r
        delta = 1 - 2 * r
        error = 0
        while y >= 0:
            self.setPoint(x1 + x, y1 + y, char)
            self.setPoint(x1 + x , y1 - y, char)
            self.setPoint(x1 - x, y1 + y, char)
            self.setPoint(x1 - x, y1 - y, char)

            error = 2 * (delta + y) - 1
            if (delta < 0) and (error <= 0):
                x += 1
                delta = delta + (2 * x + 1)
                continue
            error = 2 * (delta - x) - 1
            if (delta > 0) and (error > 0):
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1

    def draw(self, x, y, drawing):
        for row in range(len(drawing.image)):
            for elem in range(len(drawing.image[row])):
                self.image[row + x][elem + y] = drawing.image[row][elem]

img = Drawing(20, 20, '.')
img.print()
img.drawVerticalLine(3, '*')
img.print()
img.drawHorizontalLine(2, '#')
img.print()
img.drawRectangle(1, 6, 3, 1, '+')
img.print()
img.drawCircle(3, 5, 5, '+')
img.print()
img.draw_line(2, 4, 5, 5, '@')
img.print()

img2 = Drawing(25, 25, ')')
img2.print()
img2.draw(1, 2, img)
img2.print()
