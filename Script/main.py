#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
import sys
import runpy
from six.moves import input

try:
    raw_input
except NameError:
    raw_input = input

savethemblobs = sys.argv[1] if sys.argv[1:] else 'savethemblobs.py'
ecid = input("Enter ECID ").strip() or '1050808663311'
device = input("Enter model (eg. iPhone3,1 or n90ap) ").strip() or 'iPhone3,1'
opt = input("Optional arg (eg. --help) ").strip() or '--overwrite-apple'
fmt = "%s: savethemblobs %s %s %s"
print((fmt % (sys.argv[0].split('/')[-1], ecid, device, opt)))
sys.argv = ['savethemblobs.py', ecid, device, opt]
with open(sys.argv[0]) as in_file:
    exec(in_file.read())

