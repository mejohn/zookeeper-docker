#!/usr/bin/env python

import os

temp_file = open(os.path.join(os.path.dirname(__file__), "..", "commekaze_temp"), "r+")

commekazed = []

for line in temp_file:
    commekazed.append(line)

temp_file.close()

commit_file = open(os.path.join(os.path.dirname(__file__), "..", "COMMIT_EDITMSG"), "r+")

for line in commekazed:
    commit_file.write(line)

commit_file.close()
