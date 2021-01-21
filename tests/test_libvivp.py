import unittest
from test import support
import libvivp
import os

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        if not os.path.exists("tmps/"):
            os.makedirs("tmps/")
        os.remove("tmps/vpackage.json")
        libvivp.setup("tmps/", "TestPackageName", ["testAuthor1", "testAuthor2"], False)
        pass

    def tearDown(self):
        pass

    def test_feature_one(self):
        # Test feature one.
        libvivp.install("tmps/", ["https://github.com/AdityaNG/BasicModules", "https://github.com/AdityaNG/RippleCarryAdder"])
        pass

    def test_feature_two(self):
        # Test feature two.
        pass

if __name__ == '__main__':
    unittest.main()
