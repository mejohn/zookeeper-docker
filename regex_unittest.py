import unittest
import re

class TestRegex(unittest.TestCase):

  regex = "((?:(?:\\/\\*)|\\#)\\~(?:.*?|[\\r\\n])*?\\~(?:(?:\\*\\/)|\\#))"

  slash_comment = """int main() {
                     printf("Hello World");
                     /*~ int x = 10;
                     x *= 3;
                     printf("%d", x); ~*/
                  }"""

  slash_comment_multiple = """int main() {
                               printf("Hello World");
                               /*~ int x = 10;
                               x *= 3;
                               printf("%d", x); ~*/
                            }

                            int not_main() {
                               printf("Hello World");
                               /*~ int x = 10;
                               x *= 4;
                               printf("%d", x); ~*/
                            }"""

  slash_comment_inline = """int main() {
                             printf("Hello World");
                             /*~ int x = 10;
                             /*~ x *= 3;
                             /*~ printf("%d", x); ~*/
                          }"""

  slash_comment_multiple_inline = """int main() {
                                       printf("Hello World");
                                       /*~ int x = 10;
                                       /*~ x *= 3;
                                       /*~ printf("%d", x); ~*/
                                    }

                                    int not_main() {
                                       printf("Hello World");
                                       /*~ int x = 10;
                                       /*~ x *= 4;
                                       /*~ printf("%d", x); ~*/
                                    }"""

  pound_comment = """def test():
                        print "hello world"
                        
                        #~ x = 10
                        x *= 3
                        print x ~#"""

  pound_comment_inline = """def test():
                              print "hello world"
                              
                              #~ x = 10
                              #~ x *= 3
                              #~ print x ~#"""

  pound_comment_multiple = """def test():
                              print "hello world"
                              
                              #~ x = 10
                              x *= 3
                              print x ~#

                          def another_test():
                            #~ x = 11
                              x *= 3
                              print x ~#
                              print "hey" """

  pound_comment_multiple_inline = """def test():
                                      print "hello world"
                                      
                                      #~ x = 10
                                      #~ x *= 3
                                      #~ print x ~#

                                  def another_test():
                                    #~ x = 11
                                      #~ x *= 3
                                      #~ print x ~#
                                      print "hey" """

  def test_regex_slash(self):
    self.assertEqual(1, len(re.findall(self.regex, self.slash_comment, re.M)))
    self.assertEqual(2, len(re.findall(self.regex, self.slash_comment_multiple, re.M)))
    self.assertEqual(1, len(re.findall(self.regex, self.slash_comment_inline, re.M)))
    self.assertEqual(2, len(re.findall(self.regex, self.slash_comment_multiple_inline, re.M)))

  def test_regex_pound(self):
    self.assertEqual(1, len(re.findall(self.regex, self.pound_comment, re.M)))
    self.assertEqual(2, len(re.findall(self.regex, self.pound_comment_multiple, re.M)))
    self.assertEqual(1, len(re.findall(self.regex, self.pound_comment_inline, re.M)))
    self.assertEqual(2, len(re.findall(self.regex, self.pound_comment_multiple_inline, re.M)))

if __name__ == '__main__':
    unittest.main()