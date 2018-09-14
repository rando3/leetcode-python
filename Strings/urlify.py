import unittest


class URLify:
    def urlify(test, num):
        '''
        CtCI 1.3
        Write a method to replace all spaces in a string with '%20'. You may assume that the string
        has sufficient space at the end to hold the additional characters, and that you are given the "true"
        length of the string. (Note: If implementing in Java, please use a character array so that you can
        perform this operation in place.)
        EXAMPLE:
        Input: "Mr John Smith ", 13
        Output: "Mr%20John%20Smith"
        '''
        if test is None:
            return None
        if num <= 0:
            return test
        build = [char if char != " " else "%20" for char in test.strip()]
        return ''.join(build)

    def urlify2(string, length):
        '''function replaces single spaces with %20 and removes trailing spaces'''
        new_index = len(string)

        for i in reversed(range(length)):
            if string[i] == ' ':
                # Replace spaces
                string[new_index - 3:new_index] = '%20'
                new_index -= 3
            else:
                # Move characters
                string[new_index - 1] = string[i]
                new_index -= 1

        return string

class TestURLify(unittest.TestCase):
    def test_urlify(self):
        # Tests strings with normal input
        self.assertEqual(URLify.urlify2("My name is John    ", 19), "My%20name%20is%20John")
        self.assertEqual(URLify.urlify2("Mr John Smith ", 13), "Mr%20John%20Smith")


if __name__ == '__main__':
    unittest.main()
