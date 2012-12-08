import sys

from .dialects import eagle


def read_main():
    # for now, just try to read an eagle library file.
    fname = sys.argv[1]
    library = eagle.read(fname)
    print "Library"
    print library.description
    for package in library.packages:
        print package
