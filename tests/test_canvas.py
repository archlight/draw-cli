from unittest import TestCase
from canvas import Canvas
from shape import *


class TestCanvas(TestCase):

    def setUp(self):
        self.canvas = Canvas(20, 4)

    def test_blank_canvas(self):

        expected = """
----------------------
|                    |
|                    |
|                    |
|                    |
----------------------
"""
        actual = self.canvas.render()
        self.assertEqual("\n"+actual, expected)

    def test_draw_line(self):
        expected = """
----------------------
|                    |
|xxxxxx              |
|                    |
|                    |
----------------------
"""

        actions = [
            Line(Point(1, 2), Point(6, 2))
        ]
        for t in actions:
            self.canvas.draw(t, 'x')

        actual = self.canvas.render()
        self.assertEqual("\n" + actual, expected)

    def test_line_extra(self):
        expected = """
----------------------
|                    |
|xxxxxx              |
|     x              |
|     x              |
----------------------
"""
        actions = [
            Line(Point(1, 2), Point(6, 2)),
            Line(Point(6, 3), Point(6, 4)),
        ]
        for t in actions:
            self.canvas.draw(t, 'x')

        actual = self.canvas.render()
        self.assertEqual("\n" + actual, expected)

    def test_rect(self):
        expected = """
----------------------
|             xxxxx  |
|xxxxxx       x   x  |
|     x       xxxxx  |
|     x              |
----------------------
"""
        actions = [
            Line(Point(1, 2), Point(6, 2)),
            Line(Point(6, 3), Point(6, 4)),
            Rect(Point(14, 1), Point(18, 3))
        ]
        for t in actions:
            self.canvas.draw(t, 'x')

        actual = self.canvas.render()
        self.assertEqual("\n" + actual, expected)

    def test_fill(self):
        expected = """
----------------------
|oooooooooooooxxxxxoo|
|xxxxxxooooooox   xoo|
|     xoooooooxxxxxoo|
|     xoooooooooooooo|
----------------------
"""
        actions = [
            Line(Point(1, 2), Point(6, 2)),
            Line(Point(6, 3), Point(6, 4)),
            Rect(Point(14, 1), Point(18, 3))
        ]
        for t in actions:
            self.canvas.draw(t, 'x')

        self.canvas.fill(Point(10, 3), 'o')
        actual = self.canvas.render()
        self.assertEqual("\n" + actual, expected)