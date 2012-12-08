class Schematic(object):
    """
    Has
    - board
    """
    pass


class Part(object):
    """
    Has
    - symbol
    - package
    - pins
    """
    pass


class Symbol(object):
    """
    Schematic representation of a part.
    """
    pass


class Package(object):
    """
    Layout representation of a part.

    Has
    - part
    - name
    - description
    - pads

    Should this be called "footprint"?
    """
    def __init__(self, name=u'', description=u'', drawing=None, pads=None):
        self.name = name
        self.description = description
        self.drawing = drawing or []
        self.pads = pads or []

    def __repr__(self):
        if len(self.description) > 30:
            desc = self.description[:27] + '...'
        else:
            desc = self.description
        return '<Package(name=%r, description=%r)>' % (self.name, desc)


class Pin(object):
    """
    One connection point of a part.

    Has
    - part
    - name
    - wire
    - pad
    """
    pass


class Pad(object):
    """
    Has
    - pin
    - package
    - name
    - position
    - shape
    - rotation
    """
    pass


class ThroughHolePad(Pad):
    """
    Has
    - drill diameter
    """
    def __init__(self, name, position, diameter, shape, rotation):
        self.name = name
        self.position = position
        self.diameter = diameter
        self.shape = shape
        self.rotation = rotation


class SMDPad(Pad):
    """
    - width
    - height
    - layer
    """
    def __init__(self, name, position, dimensions, layer):
        self.name = name
        self.position = position
        self.dimensions = dimensions
        self.layer = layer


class Segment(object):
    """
    One line segment of a wire.

    Has
    - wire
    - width
    - start
    - end

    Arcs??
    """
    pass


class Wire(object):
    """
    Connection between one or more parts.

    Has
    - pins
    - segments
    - vias

    Should this be called 'net' instead?
    """
    pass


class Board(object):
    """
    Has
    - schematic

    - layers
    - holes
    - dimensions (not necessarily rectangular)
    - schematics
    - parts
    - wires between parts
    """
    pass


class Layer(object):
    """
    Layer within a board.
    """
    pass


class Hole(object):
    """
    Hole on a board.

    Has
    - diameter
    - position
    - plating?
    - annulus?
    """
    pass


class Via(Hole):
    """
    A via.

    Has
    - wire
    - all hole properties

    Note: subclasses from Hole.
    """


class Library(object):
    """
    Has
    - description
    - packages
    - symbols
    - devices
    """
    def __init__(self, description=u'', packages=None, symbols=None,
                 devices=None):
        self.description = description
        self.packages = packages or []
        self.symbols = symbols or []
        self.devices = devices or []
