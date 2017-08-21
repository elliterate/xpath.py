import sys


PY2 = sys.version_info[0] == 2

if PY2:
    bytes_ = str
    str_ = unicode
else:
    bytes_ = bytes
    str_ = str
