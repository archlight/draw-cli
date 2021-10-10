from .constant import Position
from .point import Point
from .line import Line


class Rect:
    def __init__(self, start: Point, finish: Point):
        """
        :param start:
        :param finish:
        """
        self.start = start
        self.start_next = Point(start.x, finish.y)
        self.finish = finish
        self.finish_next = Point(finish.x, start.y)

        self.borders = [Line(start, self.start_next),
                        Line(self.start_next, self.finish),
                        Line(self.finish, self.finish_next),
                        Line(self.finish_next, self.start)]

    def within(self, pt: Point):
        if (pt.x-self.start.x)*(pt.x-self.finish.x) < 0 and (pt.y-self.start.y)*(pt.y-self.finish.y)<0:
            return Position.INSIDE
        elif (pt.x-self.start.x)*(pt.x-self.finish.x) > 0 or (pt.y-self.start.y)*(pt.y-self.finish.y) > 0:
            return Position.OUTSIDE
        else:
            return Position.ONEDGE

    def __iter__(self):
        cont_points = []
        for line in self.borders:
            for pt in line:
                if pt not in cont_points:
                    cont_points.append(pt)
                    yield pt
