# Test with less arguments than expected.
# Test with more arguments than expected.
# Test with invalid file paths.
# Test with empty files
# Test with multiple folders with different paths and files.

import pytest
from main_module import find_keywords, plot_graph

dir_names = [
    "/Users/kalpanamaram/PycharmProjects/keyword_search_automation",
    "/Users/kalpanamaram/PycharmProjects/Test",
    "/Users/Siva/PycharmProjects/keyword_search_automation"
]


def test_find_keywords():
    assert find_keywords("/Users/Siva/PycharmProjects/keyword_search_automation", "hello")







