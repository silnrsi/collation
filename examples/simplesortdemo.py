#!/usr/bin/env python
'Simple example of ICU sorting'
__url__ = 'http://github.com/silnrsi/collation'
__copyright__ = 'Copyright (c) 2021 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Rowe'

# Installation of ICU:
# Linux: pip install PyICU
# Windows: From https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyicu download the "wheel" (.whl file) to match
# the version of Python ("cp37" for Python 3.7, for example) and Windows ("amd64" for 64-bit Windows) you have.
# Then: pip install PyICU‑2.5‑cp37‑cp37m‑win_amd64.whl (but using the actual .whl file you downloaded)

import icu
inputdata = ["date", "apple", "cherry", "banana"]
# First example: use default collation by specifying an empty string for the collation
rbc1 = icu.RuleBasedCollator("")
sorteddata1 = sorted(inputdata, key=rbc1.getSortKey)
for line in sorteddata1:
    print(line)
# produces:
# apple
# banana
# cherry
# date

# Second example: use a collation tailoring that sorts "d" directly after "a"
col = """
&a < d
"""
rbc2 = icu.RuleBasedCollator(col)
sorteddata2 = sorted(inputdata, key=rbc2.getSortKey)
for line in sorteddata2:
    print(line)
# produces:
# apple
# date
# banana
# cherry
