import sys

from unittest import TestCase

from pypcb.cmd import read_main

from . import data


class TestEagleRead(TestCase):
    def test_sample(self):
        sys.argv = ['', data.test_library_filename]
        read_main()
