from collections import Counter, defaultdict
from shape import *


class Pixel:

    NON_ERASABLE = ['x', '-', '|']

    def __init__(self, x, y, char=' '):
        self.char = char
        self.fillable = True if char not in self.NON_ERASABLE else False
        self.regionidx = ()
        self.coordinate = (x, y)
        self.label = 1 if char == ' ' else 0

    def __eq__(self, other):
        return self.char == other.char

    def __ne__(self, other):
        return self.char != other.char

    def empty(self):
        return self.char == ' '

    def fill(self, char):
        if self.fillable:
            self.char = char
            self.label = 1 if char == ' ' else 0
            self.fillable = True if char not in self.NON_ERASABLE else False


class Canvas:
    def __init__(self, width, height):
        self.width = width+2
        self.height = height+2
        self.canvas = self.allocate_pixels()
        self.rect = Rect(Point(0, 0), Point(self.width-1, self.height-1))
        self.history = []
        self.regions = dict()
        self.draw_borders()

    def allocate_pixels(self):
        return [[Pixel(x, y) for x in range(self.width)] for y in range(self.height)]

    def draw_borders(self):
        borders = self.rect.borders
        for line in [borders[1], borders[3],borders[0], borders[2]]:
            self.draw(line, '-' if line.orient == Orientation.HORIZONTAL else '|')
        self.canvas[-1][-1].fill('-')

    def draw(self, shape, char):
        if self.rect.within(shape.start)!=Position.OUTSIDE and self.rect.within(shape.finish) != Position.OUTSIDE:
            for x, y in shape:
                self.canvas[y][x].fill(char)
            self.add_shape(shape)
        else:
            print('it is not within canvas')

    def add_shape(self, shape):
        if not isinstance(shape, Line):
            self.history.append(shape)

    def join_regions(self):
        d = defaultdict(list)
        for t in sum(self.canvas, []):
            d[t.regionidx].append(t)
        self.regions = d

    def reindex(self):
        # this approach only works drawing rects only
        for y in range(self.height):
            for x in range(self.width):
                if self.canvas[y][x].fillable:
                    self.canvas[y][x].regionidx = \
                        tuple([1 if s.within(Point(x, y)) == Position.INSIDE else 0 for s in self.history])

        self.join_regions()

    # def fill(self, pt: Point, color='c'):
    #     self.reindex()
    #     self.join_regions()
    #
    #     for k, v in self.regions.items():
    #         if tuple(pt) in [t.coordinate for t in v]:
    #             for t in v:
    #                 t.fill(color)
    #             break

    def connected_area(self):
        labeldict = defaultdict(set)
        regions = defaultdict(list)

        label = 0
        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                if self.canvas[y][x].empty():
                    if self.canvas[y][x] != self.canvas[y-1][x] and \
                            self.canvas[y][x] != self.canvas[y][x-1]:
                        label += 1
                        self.canvas[y][x].label = label
                    elif self.canvas[y][x] == self.canvas[y-1][x] or \
                            self.canvas[y][x] == self.canvas[y][x-1]:
                        label_choices = [self.canvas[y][x-1].label, self.canvas[y-1][x].label]
                        self.canvas[y][x].label = min([t for t in label_choices if t])
                        if self.canvas[y][x-1].label:
                            labeldict[self.canvas[y][x].label].add(self.canvas[y][x-1].label)
                            labeldict[self.canvas[y][x-1].label].add(self.canvas[y][x].label)
                        if self.canvas[y-1][x].label:
                            labeldict[self.canvas[y][x].label].add(self.canvas[y-1][x].label)
                            labeldict[self.canvas[y-1][x].label].add(self.canvas[y][x].label)

        for y in range(self.height):
            for x in range(self.width):
                if self.canvas[y][x].label:
                    self.canvas[y][x].label = min(labeldict[self.canvas[y][x].label])
                    regions[self.canvas[y][x].label].append(self.canvas[y][x])

        return regions

    def fill(self, pt: Point, color='o'):
        regions = self.connected_area()
        label = self.canvas[pt.y][pt.x].label
        for p in regions[label]:
            p.fill(color)

    def debug(self):
        import pprint
        d = []
        for row in self.canvas:
            d.append([t.label for t in row])
        pprint.pprint(d)

    def render(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self.canvas[y][x].char
            s += "\n"
        return s
