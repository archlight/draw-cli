from canvas import Canvas
from shape import *

drawcanvas = None
SUPPORTED_CMD = ['C', 'L', 'R', 'B', 'Q']


def is_number_list(d):
    return len(d) == len([c.isdigit() for c in d])


if __name__ == "__main__":
    print('welcome to drawapp')
    cmd = ''
    while cmd != 'Q':
        cmdline = input('')
        cmd, *args = cmdline.split(' ')
        if cmd not in SUPPORTED_CMD:
            print('{} not supported'.format(cmd))
        else:
            if cmd == 'C':
                if len(args) == 2 and is_number_list(args):
                    width, height = int(args[0]), int(args[1])
                    drawcanvas = Canvas(width, height)
                    print(drawcanvas.render())
                else:
                    print('canvas [C] requires two integers')
            elif cmd in ['L', 'R']:
                if len(args) == 4 and is_number_list(args):
                    start, finish = Point(int(args[0]), int(args[1])), Point(int(args[2]), int(args[3]))
                    element = Line(start, finish) if cmd == 'L' else Rect(start, finish)
                    if drawcanvas:
                        drawcanvas.draw(element, 'x')
                        print(drawcanvas.render())
                    else:
                        print('canvas required in order to draw shape')
                else:
                    print('line/rect [L/R] requires four integers')
            elif cmd == 'B':
                if len(args) == 3 and is_number_list(args[:-1]):
                    pt = Point(int(args[0]),int(args[1]))
                    color = args[2]
                    if drawcanvas:
                        drawcanvas.fill(pt, color)
                        print(drawcanvas.render())
                    else:
                        print('canvas required in order to draw shape')
                else:
                    print('fill [B] requires two integers follower by color')


