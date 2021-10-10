from .constant import Position, Orientation
from .point import Point


class Line:
    def __init__(self, _start: Point, _finish: Point):
        self.start = _start
        self.finish = _finish
        if self.start.x == self.finish.x:
            self.orient = Orientation.VERTICAL
        elif self.start.y == self.finish.y:
            self.orient = Orientation.HORIZONTAL
        else:
            self.orient = Orientation.INVALID

    def contains(self, pt: Point):
        if self.orient:
            if min(self.start.x, self.finish.x) <= pt.x <= max(self.start.x, self.finish.x) and \
                    min(self.start.y, self.finish.y) <= pt.y <= max(self.start.y, self.finish.y):
                return Position.ONEDGE
            else:
                return Position.OUTSIDE

    def asc_range(self, a, b):
        if a > b:
            a, b = b, a
        return range(a, b+1)

    def __iter__(self):
        if self.orient == Orientation.VERTICAL:
            for i in self.asc_range(self.start.y, self.finish.y):
                yield self.start.x, i
        else:
            for i in self.asc_range(self.start.x, self.finish.x):
                yield i, self.start.y
