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

    Should this be called "footprint"?
    """
    pass


class Pin(object):
    """
    One connection point of a part.

    Has
    - part
    - wire
    """
    pass


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


class Via(Hole):
    """
    A via.

    Has
    - wire
    - all hole properties

    Note: subclasses from Hole.
    """


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
