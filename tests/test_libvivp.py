import unittest
from test import support
import libvivp
import os
import git
import shutil

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

    def test_feature_install_remove(self):
        # Test feature one.
        libvivp.install("tmps/", ["https://github.com/AdityaNG/BasicModules", "https://github.com/AdityaNG/RippleCarryAdder"])
        libvivp.remove("tmps/", ["https://github.com/AdityaNG/RippleCarryAdder"])
        pass
    
    def test_feature_update(self):
        # Test feature two.
        libvivp.update("tmps/")
        pass

    def test_feature_list(self):
        # Test feature two.
        libvivp.list_vivp("tmps/")
        pass

    def test_feature_testbench(self):
        # Test feature
        if os.path.isdir("tmps/RippleCarryAdder"):
            shutil.rmtree("tmps/RippleCarryAdder")
        git.Git("tmps/").clone("https://github.com/AdityaNG/RippleCarryAdder")
        libvivp.update("tmps/RippleCarryAdder")
        libvivp.execute("tmps/RippleCarryAdder")
        pass

if __name__ == '__main__':
    unittest.main()
