import re
import os
import time
import uuid
import shutil
import unittest
from shutil import copyfile
from subprocess import call, Popen
import subprocess

class TestCommekaze(unittest.TestCase):

  FNULL = open(os.devnull, 'w')

  dir_name = str(time.time()) #str(uuid.uuid4()) TODO

  @classmethod
  def setUpClass(cls):
    super(TestCommekaze, cls).setUpClass()

    # Create directory and cd in there
    print('Creating directory...')
    call(["mkdir", cls.dir_name])
    os.chdir(cls.dir_name)

    # Init the git directory, copy the hook in there, create initial files, and initial commit
    print('Init\'ing git, copying git hooks, and creating initial files')
    call(["git", "init"], stdout=cls.FNULL)
    call(["cp", "../pre-commit_commekaze.py", ".git/hooks/pre-commit"])
    call(["cp", "../prepare-commit-msg_commekaze.py", ".git/hooks/prepare-commit-msg"])

    # Iterate through each template test file we have and copy it into our current test directory
    test_file_dir = "../test_files/"
    files_to_test = os.listdir(test_file_dir)
    cur_dir = os.getcwd()

    for test_file in files_to_test:
      copyfile(test_file_dir + test_file, cur_dir + "/" + test_file)

  def test_equals(self):
    self.assertEquals(1, 1)

  def test_initial_commit(self):
    initial_commit_msg = 'Initial commit'

    call(["git", "add", "-A"])
    initial_commit = call('git commit -am "{}"'.format(initial_commit_msg), shell=True, stdout=self.FNULL)
    self.assertEquals(0, initial_commit)

    num_of_commits_call = subprocess.Popen(["git", "rev-list", "--all", "--count"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    num_of_commits, error = num_of_commits_call.communicate()
    self.assertEquals(1, int(num_of_commits.strip()))

    last_commit_msg_call = subprocess.Popen(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    last_commit_msg, error = last_commit_msg_call.communicate()
    self.assertEquals(initial_commit_msg, last_commit_msg.strip())

  def test_second_commit(self):
    commit_msg = "Second commit - added regular comments"
    c_comment  = "\n/* This is a regular comment */"
    py_comment = "\n# This is a regular comment"
    test_files = os.listdir(os.getcwd())
    
    for test_file in test_files:
      if os.path.isdir(test_file) == False:
        f = open(test_file, 'a+')
        ext = os.path.splitext(test_file)[1]
        if ext == '.c':
          f.write(c_comment)
        elif ext == '.py':
          f.write(py_comment)

    second_commit = call('git commit -am "{}"'.format(commit_msg), shell=True, stdout=self.FNULL)
    self.assertEquals(0, second_commit)

    num_of_commits_call = subprocess.Popen(["git", "rev-list", "--all", "--count"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    num_of_commits, error = num_of_commits_call.communicate()
    self.assertEquals(2, int(num_of_commits.strip()))

    last_commit_msg_call = subprocess.Popen(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    last_commit_msg, error = last_commit_msg_call.communicate()
    self.assertEquals(commit_msg, last_commit_msg.strip())

  def test_third_commit(self):
    commit_msg = "Third commit - added commekaze comments"
    c_comment  = "\n/*~ This is a commekaze comment and will disappear after 5 commits ~*/"
    py_comment = "\n#~ This is a commekaze comment and will disappear after 5 commits ~#"
    test_files = os.listdir(os.getcwd())
    
    for test_file in test_files:
      if os.path.isdir(test_file) == False:
        f = open(test_file, 'a+')
        ext = os.path.splitext(test_file)[1]
        if ext == '.c':
          f.write(c_comment)
        elif ext == '.py':
          f.write(py_comment)

    third_commit = call('git commit -am "{}"'.format(commit_msg), shell=True, stdout=self.FNULL)
    self.assertEquals(0, third_commit)

    num_of_commits_call = subprocess.Popen(["git", "rev-list", "--all", "--count"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    num_of_commits, error = num_of_commits_call.communicate()
    self.assertEquals(3, int(num_of_commits.strip()))

    last_commit_msg_call = subprocess.Popen(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    last_commit_msg, error = last_commit_msg_call.communicate()
    self.assertEquals(commit_msg, last_commit_msg.strip())

  def test_fourth_commit(self):
    commit_msg = "Fourth commit - added regular comments"
    c_comment  = "\n/* This is a regular comment */"
    py_comment = "\n# This is a regular comment"
    test_files = os.listdir(os.getcwd())
    
    for test_file in test_files:
      if os.path.isdir(test_file) == False:
        f = open(test_file, 'a+')
        ext = os.path.splitext(test_file)[1]
        if ext == '.c':
          f.write(c_comment)
        elif ext == '.py':
          f.write(py_comment)

    fourth_commit_call = subprocess.Popen('git commit -am "{}"'.format(commit_msg), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fourth_commit, error = fourth_commit_call.communicate()
    # import pdb; pdb.set_trace()
    self.assertEquals(0, fourth_commit)

    num_of_commits_call = subprocess.Popen(["git", "rev-list", "--all", "--count"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    num_of_commits, error = num_of_commits_call.communicate()
    self.assertEquals(4, int(num_of_commits.strip()))

    last_commit_msg_call = subprocess.Popen(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    last_commit_msg, error = last_commit_msg_call.communicate()
    self.assertEquals(commit_msg, last_commit_msg.strip())

  @classmethod
  def tearDownClass(cls):
    # Remove the test directory
    print("tear down")
    # shutil.rmtree(os.path.abspath("./"))




if __name__ == '__main__':
  unittest.main()
