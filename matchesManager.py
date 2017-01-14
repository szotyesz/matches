#!/usr/bin/env python

import os
import os.path

from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir(os.path.dirname(os.path.realpath(__file__))) if isfile(join(os.path.dirname(os.path.realpath(__file__)), f)) and 'matches' in f]

print onlyfiles

res = [k for k in onlyfiles if 'matches' in k]

print res
