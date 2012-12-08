import sys

from .dialects import eagle
from . import model


def describe_package(package):
    print repr(package)
    for pad in package.pads:
        if isinstance(pad, model.SMDPad):
            print "   %s - SMD" % pad.name
        else:
            print "   %s - TH" % pad.name


def read_main():
    # for now, just try to read an eagle library file.
    fname = sys.argv[1]
    library = eagle.read(fname)
    print "Library"
    print library.description
    for package in library.packages:
        print "-" * 80
        describe_package(package)
