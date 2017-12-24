#!/usr/bin/env python3

import fontforge
import os.path
import sys

if len(sys.argv) < 2:
    print('No input file profided!')
    sys.exit(0)

filename = sys.argv[1]
basename, ext = os.path.splitext(filename)

if len(sys.argv) > 2:
    basename = sys.argv[2]

desired_formats = ['eot', 'ttf', 'woff', 'woff2']
font = fontforge.open(filename)

for desired_format in desired_formats:
    font.generate('%s.%s' % (basename, desired_format))
