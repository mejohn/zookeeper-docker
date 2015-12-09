import re
import os
import time
import unittest
from subprocess import call

class TestCommekaze(unittest.TestCase):

  FNULL = open(os.devnull, 'w')

  slash_comment = """int main() {
                     printf("Hello World");
                     /*~ int x = 10;
                     x *= 3;
                     printf("%d", x); ~*/
                  }"""

  pound_comment = """def test():
                        print "hello world"
                        
                        #~ x = 10
                        x *= 3
                        print x ~#"""

  def setUp(self):
    # Create directory and cd in there
    print('Creating directory...')
    dir_name = str(time.time())
    call(["mkdir", dir_name])
    os.chdir(dir_name)

    # Init the git directory, copy the hook in there, create initial files, and initial commit
    print('Init\'ing git, copying pre-commit, create initial files, and initial commit...')
    call(["git", "init"], stdout=self.FNULL)
    call(["cp", "../commekaze.py", ".git/hooks/pre-commit"])

    hello_world_c = open('hello_world.c', 'w+')
    hello_world_c.write(self.slash_comment)
    hello_world_c.close()

    hello_world_py = open('hello_world.py', 'w+')
    hello_world_py.write(self.pound_comment)
    hello_world_py.close()

    call(["git", "add", "."])
    call(["git", "commit", "-am", "Initial commit"], stdout=self.FNULL)

  def test_equals(self):
    self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()