#!/usr/bin/env python3

import os
import re

with os.popen('who', 'r') as f:
    for line in f:
        print(re.split(r'\s\s+|\t', line.strip()))
