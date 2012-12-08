pypcb - Python's Swiss Army Knife for PCB CAD
=============================================

Scott Torborg - `Cart Logic <http://www.cartlogic.com>`_

PyPCB is a Python library intended to provide a single interchange point and an extensible toolchain for working with schematic and PCB layout CAD files.


Foundation
----------

* Python object representation (class hierarchy) for PCB and schematic files.
* Parsers and writers for EAGLE 6 and KiCAD, initially.


Goals / Roadmap
---------------

* SVG (and HTML?) rendering.
* Intelligent merge and diff tools.
* Design rule checking engines / configuration.
* Manufacturing workflow tools. (Gerber export, PnP, etc).
* BOM management tools.


Installation
============

Install with pip::

    $ pip install pypcb


License
=======

PyPCB is licensed under an MIT license. Please see the LICENSE file for more
information.


Code Standards
==============

PyPCB has a comprehensive test suite with 100% line and branch coverage, as
reported by the excellent ``coverage`` module. To run the tests, simply run in
the top level of the repo::

    $ nosetests

There are no `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ or
`Pyflakes <http://pypi.python.org/pypi/pyflakes>`_ warnings in the codebase. To
verify that::

    $ pip install pep8 pyflakes
    $ pep8 .
    $ pyflakes .

Any pull requests must maintain the sanctity of these three pillars.
