class Line(object):
    def __init__(self, start, end, width, layer):
        self.start = start
        self.end = end
        self.width = width
        self.layer = layer


class Rectangle(object):
    def __init__(self, topleft, bottomright, layer):
        self.topleft = topleft
        self.bottomright = bottomright
        self.layer = layer


class Polygon(object):
    def __init__(self, vertices, width, layer):
        self.vertices = vertices
        self.width = width
        self.layer = layer


class Circle(object):
    def __init__(self, position, radius, width, layer):
        self.position = position
        self.radius = radius
        self.width = width
        self.layer = layer


class Text(object):
    def __init__(self, s, position, size, ratio, layer):
        self.s = s
        self.position = position
        self.size = size
        self.ratio = ratio
        self.layer = layer
