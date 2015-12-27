#!/usr/bin/env python

import sys
import re
import subprocess
import os

# TODO
# right now, the script checks for all files in the repo, we can do git diff instead to make this that much more efficient

# Call git in a nice way
def git(args):
  args    = ['git'] + args
  try:
    git = subprocess.check_output(args).decode("utf-8").strip()
    return git
  except Exception, e:
    return None
exit(1)
regex      = "((?:(?:\\/\\*)|\\#)\\~(?:.*?|[\\r\\n])*?\\~(?:(?:\\*\\/)|\\#))" # NOTE: every forward slash in the pattern had to be escaped here - to test out, remove every other forward slash
files      = git(['ls-tree', '-r', 'HEAD', '--name-only']).split('\n') # Get all the files in our working tree
commekazed = []

# Iterate through each file that our git repo is tracking
for file in files:
  if len(file):
    # Check to see if we can find a commekaze code comment
    f          = open(file, 'a+')
    f.seek(0)
    content    = f.read()
    orig_file  = content
    matches    = re.findall(regex, content, re.M)

    if len(matches):
      try:
        # If we did find a commekaze comment, let's check that against the same file from 5 commits ago
        history = git(['show', 'HEAD~4:' + file]) # TODO change to ~5

        for match in matches:
          # Check our old file for matches...

          if match in history:
            # import pdb; pdb.set_trace()
            # ...if we found a match, log it and replace it with an empty string

            # Let's find the line number of our match
            line_num = orig_file.count(os.linesep, 0, orig_file.find(match)) + 1

            content = content.replace(match, '')
            f.seek(0)    # Start at the beginning of the file again

            # f.truncate() # Trancate the file
            # TODO ***********************
            # uncomment line below and above
            # f.write(content) # Write the new string we created after switching out the commekaze comment

            # TODO add this to the git commit message
            msg = "Removed commekaze block from {0}, line {1}\n".format(unicode(file), unicode(line_num))
            commekazed.append(msg) 
          pass
        pass
      except Exception, e:
        pass

    f.close()

print(''.join(commekazed))
# commit_file = open(os.path.join(os.path.dirname(__file__), "..", "COMMIT_EDITMSG"), "r+")
# import pdb; pdb.set_trace()
# commit_file.seek(0)
# commit_file.write(''.join(commekazed))
# commit_file.seek(0)

print("in commit msg, {0}".format(unicode(sys.argv[1])))
# print(commit_file.read())
commit_file.seek(0)
commit_file.close()
# print ''.join(commekazed)
















