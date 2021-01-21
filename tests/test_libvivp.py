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

    def test_feature_not_vivp_dir(self):
        # Test Install and Remove Repos Feature
        def fn_fails(fn):
            try:
                fn()
                return False
            except: return True
        
        def setup():
            libvivp.setup("tmps/", "TestPackageName", ["testAuthor1", "testAuthor2"], False)

        def install1():
            libvivp.install("tmps/dummy", ["testAuthor1", "testAuthor2"])

        def install2():
            libvivp.install("tmps/", ["testAuthor1", "testAuthor2"])

        def install3():
            libvivp.install("tmps/", ["https://github.com/AdityaNG/BasicModules"])
            libvivp.install("tmps/", ["https://github.com/AdityaNG/BasicModules"])

        def remove1():
            libvivp.remove("tmps/dummy", ["testAuthor1", "testAuthor2"])

        def remove2():
            libvivp.remove("tmps/", ["testAuthor1", "testAuthor2"])

        def remove3():
            libvivp.remove("tmps/", ["https://github.com/AdityaNG/BasicModules"])      
            libvivp.remove("tmps/", ["https://github.com/AdityaNG/BasicModules"])      

        def update():
            libvivp.update("tmps/dummy")  

        def refresh_all_dependencies():
            libvivp.refresh_all_dependencies("tmps/dummy")  

        fail_fns = [setup, install1, install2, install3, remove1, remove2, remove3, update, refresh_all_dependencies]
        for fn in fail_fns:
            if not fn_fails(fn): raise Exception("Fail", fn)
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
        libvivp.list_vivp("tmps/RippleCarryAdder")
        
        libvivp.remove_testbench("tmps/RippleCarryAdder", ["testbench.v"])
        passed=True
        try:
            libvivp.remove_testbench("tmps/RippleCarryAdder", ["testbench.v"])
            passed = False
        except:
            pass
        if not passed: raise Exception("Fail")
        libvivp.add_testbench("tmps/RippleCarryAdder", ["testbench.v"])
        passed=True
        try:
            libvivp.add_testbench("tmps/RippleCarryAdder", ["testbench.v"])
            passed = False
        except:
            pass
        if not passed: raise Exception("Fail")

        passed=True
        try:
            libvivp.remove_files("tmps/RippleCarryAdder", ["RippleCarryAdder.v"])
            passed = False
        except:
            pass
        if not passed: raise Exception("Fail")

        libvivp.add_files("tmps/RippleCarryAdder", ["RippleCarryAdder.v"])
        
        passed=True
        try:
            libvivp.add_files("tmps/RippleCarryAdder", ["RippleCarryAdder.v"])
            passed = False
        except:
            pass
        if not passed: raise Exception("Fail")

        libvivp.remove_files("tmps/RippleCarryAdder", ["RippleCarryAdder.v"])
        
        
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
