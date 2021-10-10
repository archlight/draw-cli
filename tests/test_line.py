from unittest import TestCase
from shape import Line, Point, Position


class TestLine(TestCase):
    def setUp(self):
        self.line = Line(Point(2, 2), Point(2, 5))

    def test_contains(self):
        self.assertTrue(self.line.contains(Point(2, 4)) == Position.ONEDGE)
        self.assertTrue(self.line.contains(Point(3, 4)) == Position.OUTSIDE)

    def test_iter(self):
        self.assertEquals(tuple([(x, y) for x, y in self.line]), ((2, 2), (2, 3), (2, 4), (2, 5)))
