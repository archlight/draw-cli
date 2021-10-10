from enum import Enum


class Position(Enum):
    OUTSIDE = 0
    ONEDGE = 1
    INSIDE = 2


class Orientation(Enum):
    INVALID = 0
    HORIZONTAL = 1
    VERTICAL = 2

