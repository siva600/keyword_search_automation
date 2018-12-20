import unittest
from main_module import find_keywords, plot_graph


class testMainModule(unittest.TestCase):
    # testing valid dirname and keyword with expected output.
    def testEquals(self):
        root_dir = '/Users/kalpanamaram/PycharmProjects/keyword_search_automation'
        keyword = 'list'
        self.assertEquals(type(find_keywords(root_dir, keyword)), dict)
        self.assertNotEqual(type(find_keywords(root_dir, keyword)), list)
        self.assertIsNotNone(find_keywords(root_dir, 'key'))

    # testing exception handling in find_keywords function.
    def testException(self):
        with self.assertRaises(Exception):
            root_dir = '/Newuser/kalpanamaram/PycharmProjects/keyword_search_automation'
            find_keywords(root_dir, 'list')

    # testing assertion for null keyword.
    def testKeyword(self):
        with self.assertRaises(Exception):
            root_dir = '/Newuser/kalpanamaram/PycharmProjects/keyword_search_automation'
            find_keywords(root_dir, '')


if __name__ == '__main__':
    unittest.main()






