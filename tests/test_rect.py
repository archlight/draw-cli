from unittest import TestCase
from shape import Point, Rect, Position


class TestRect(TestCase):
    def setUp(self):
        self.rect = Rect(Point(0, 0), Point(10, 10))
        self.small_rect = Rect(Point(2, 2), Point(3, 3))

    def test_within(self):
        self.assertTrue(self.rect.within(Point(5, 5)) == Position.INSIDE)
        self.assertTrue(self.rect.within(Point(15, 5)) == Position.OUTSIDE)
        self.assertTrue(self.rect.within(Point(10, 5)) == Position.ONEDGE)

    def test_iter(self):
        cont_points = tuple([(x, y) for x, y in self.small_rect])
        self.assertEquals(cont_points, ((2, 2), (2, 3), (3, 3), (3, 2)))



