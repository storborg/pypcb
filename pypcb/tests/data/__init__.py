import os.path


__here__ = os.path.abspath(os.path.dirname(__file__))

fallback = os.path.join(__here__, 'eagle-pypcb-basic.lbr')
eagle_root = '/Applications/EAGLE-6.3.0'

if os.path.exists(eagle_root):
    fname = os.path.join(eagle_root, 'lbr', 'diode.lbr')
else:
    fname = fallback


test_library_filename = fname
