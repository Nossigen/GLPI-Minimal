#!/usr/bin/python3

import sys as s
import django as d


print("Python: Version " + str(s.version_info[0]) + "." + str(s.version_info[1]))
print("Django: Version " + d.get_version())