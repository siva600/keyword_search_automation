import unittest
from main_module import find_keywords, plot_graph


class testMainModule(unittest.TestCase):
    # give respective directory name below.
    root_dir = '.'

    # testing valid dirname and keyword with expected output.
    def testEquals(self):
        keyword = 'list'
        self.assertEquals(type(find_keywords(self.root_dir, keyword)), dict)
        self.assertNotEqual(type(find_keywords(self.root_dir, keyword)), list)
        self.assertIsNotNone(find_keywords(self.root_dir, 'key'))

    # testing exception handling in find_keywords function.
    def testException(self):
        with self.assertRaises(Exception):
            find_keywords(self.root_dir, 'list')

    # testing assertion for null keyword.
    def testKeyword(self):
        with self.assertRaises(Exception):
            find_keywords(self.root_dir, '')


if __name__ == '__main__':
    unittest.main()






