import unittest
from test import support
import libvivp
import os
import git
import shutil

class MainTests(unittest.TestCase):

    def setUp(self):
        if not os.path.exists("tmps/"):
            os.makedirs("tmps/")
        if os.path.isfile("tmps/vpackage.json"):
            os.remove("tmps/vpackage.json")
        libvivp.setup("tmps/", "TestPackageName", ["testAuthor1", "testAuthor2"], False)
        pass

    def tearDown(self):
        if os.path.isdir("tmps/"):
            shutil.rmtree("tmps/")
        pass

    def test_feature_install_remove(self):
        # Test Install and Remove Repos Feature
        libvivp.install("tmps/", ["https://github.com/AdityaNG/BasicModules", "https://github.com/AdityaNG/RippleCarryAdder"])
        libvivp.remove("tmps/", ["https://github.com/AdityaNG/RippleCarryAdder"])
        pass
    
    def test_feature_update(self):
        # Test Update repos feature
        libvivp.update("tmps/")
        pass

    def test_feature_list(self):
        # Test list feature
        libvivp.list_vivp("tmps/")
        pass

    def test_feature_testbench(self):
        # Test the execute command
        if os.path.isdir("tmps/RippleCarryAdder"):
            shutil.rmtree("tmps/RippleCarryAdder")
        git.Git("tmps/").clone("https://github.com/AdityaNG/RippleCarryAdder")
        libvivp.update("tmps/RippleCarryAdder")
        libvivp.execute("tmps/RippleCarryAdder")
        libvivp.execute_legacy1("tmps/RippleCarryAdder")
        pass


class UtilsTests(unittest.TestCase):

    def setUp(self):
        
        pass

    def tearDown(self):
        
        pass

    def test_feature_utils(self):
        if libvivp.utils.replaceAll("***___***", "_", "A") != "***AAA***": raise Exception("Fail")
        if libvivp.utils.make_safe("path/with one/space") != "path/with\\ one/space": raise Exception("Fail")
        pass
    
class vPackageTests(unittest.TestCase):

    def setUp(self):
        if not os.path.exists("tmps/"):
            os.makedirs("tmps/")
        if os.path.isfile("tmps/vpackage.json"):
            os.remove("tmps/vpackage.json")
        libvivp.setup("tmps/", "TestPackageName", ["testAuthor1", "testAuthor2"], False)
        pass

    def tearDown(self):
        if os.path.isdir("tmps/"):
            shutil.rmtree("tmps/")
        pass

    def test_feature_vPackage(self):
        p = libvivp.vPackage(filePath=os.path.join("tmps", libvivp.utils.VPACKAGE_JSON))
        repr(p)
        print(p)
        pass


if __name__ == '__main__':
    unittest.main()
