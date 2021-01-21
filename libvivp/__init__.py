import os
import json
from .utils import *
from .vPackage import vPackage
from git import Git
import git
import shutil
import subprocess

"""
# libvivp

Contains all helper functions to interface with a vpackage

"""


def setup(vivp_dir, packageName, packageAuthors, packageURL):
    """
    ## setup(vivp_dir, packageName, packageAuthors, packageURL)
    Runs a quick setup on the vivp_dir

    Creates vpackage.json with packageName, packageAuthors and packageURL

    ### Raises exception if

    1. Input directory already has a vpackage.json
    2. packageURL is not a valid URL
    """
    if is_vivp_dir(vivp_dir):
        raise Exception("Already VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=True, saveable=True)
    p.data['packageDetails']['packageName'] = packageName
    p.data['packageDetails']['packageAuthors'] = packageAuthors
    if packageURL:
        if (is_valid_git_url(packageURL)):
            p.data['packageURL'] = packageURL
        else:
            raise Exception('Invalid packageURL : ' + packageURL)
    p.save()
    print(p)
    pass

def install(vivp_dir, package_list):
    """
    ## install(vivp_dir, package_list)
    Installs a list of packages (package_list)

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. Dependency already exists
    3. Invalid dependency URL
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)


    for dep in package_list:
        if is_valid_git_url(dep):
            if not p.has_dependency(dep):
                p.data['dependencyList'].append(dep)
            else:
                raise Exception('Dependency already added: ' + dep)
        else:
            raise Exception('Invalid dependency : ' + dep)
    
    p.save()
    print(p)
    refresh_all_dependencies(vivp_dir)
    pass


def update(vivp_dir):
    """
    ## update(vivp_dir)
    Updates all the depenencies to appropriate version

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    refresh_all_dependencies(vivp_dir)


def remove(vivp_dir, package_list):
    """
    ## remove(vivp_dir, package_list)
    Removes the list of dependencies (package_list)

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. Dependency does not exist
    3. Invalid dependency URL
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)

    for dep in package_list:
        if is_valid_git_url(dep):
            if p.has_dependency(dep):
                p.data['dependencyList'].remove(dep)
            else:
                raise Exception('Dependency does not in list : ' + dep)
        else:
            raise Exception('Invalid dependency : ' + dep)
    
    p.save()
    print(p)
    refresh_all_dependencies(vivp_dir)
    pass


def list_vivp(vivp_dir):
    """
    ## list_vivp(vivp_dir)
    Lists all the dependencies and the modules they have exposed throught the 'fileList'

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    """
    # TODO Return the result as dictionary
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=False)
    #dependency_files_list = []
    if os.path.isdir(get_repos_dir(vivp_dir)):
        folder_list = os.listdir(get_repos_dir(vivp_dir))
        for dep in folder_list:
            print(dep)
            package_dep_path = os.path.join(get_repos_dir(vivp_dir), dep)
            p = vPackage(filePath=os.path.join(package_dep_path, VPACKAGE_JSON), createNew=False, saveable=False)
            for dep_file in p.data['fileList']:
                print("\t", dep_file)
                #dependency_files_list.append(os.path.join(package_dep_path, dep_file))

def refresh_all_dependencies(vivp_dir):
    """
    ## refresh_all_dependencies(vivp_dir)
    Updates all the depenencies to appropriate version

    Clears the cache entirely and performs a git clone on all dependencies

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    """

    # TODO use git clone
    # TODO add version control support for the dependencies
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=False)

    print("[vivp]", "Clearing cache")
    CACHE_DIR = get_cache_dir(vivp_dir)
    REPOS_DIR = get_repos_dir(vivp_dir)
    # Remove VPACKAGE_HIDDEN directory
    if os.path.isdir(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)

    os.makedirs(CACHE_DIR)
    os.makedirs(REPOS_DIR)

    # iterate through all packages and clone
    for dep in p.data['dependencyList']:
        print("[vivp]", "git clone ", dep)
        output = git.Git(REPOS_DIR).clone(dep)
        print(output)


def get_files_from_dependencies(vivp_dir):
    """
    ## get_files_from_dependencies(vivp_dir)
    Returns the list of all file paths that are exposed by 'fileList'

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=False)
    dependency_files_list = []
    if os.path.isdir(get_repos_dir(vivp_dir)):
        folder_list = os.listdir(get_repos_dir(vivp_dir))
        for dep in folder_list:
            package_dep_path = os.path.join(get_repos_dir(vivp_dir), dep)
            p = vPackage(filePath=os.path.join(package_dep_path, VPACKAGE_JSON), createNew=False, saveable=False)
            for dep_file in p.data['fileList']:
                dependency_files_list.append(os.path.join(package_dep_path, dep_file))
    return dependency_files_list

def execute(vivp_dir):
    """
    ## execute(vivp_dir)
    Runs the testbench : 

    ```bash
    $ rm *.out *.vcd
    $ iverilog [testBench List] -I vivp_dir/.vpackage/repos/
    $ vvp a.out
    $ gtkwave {*.vcd}[0]
    ```

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. More than 1 VCD file
    3. No VCD Files
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    file_list = []

    for f in p.data['testBench']:
        file_list.append(make_safe(os.path.join(vivp_dir, f)))
    
    vcd_files = list(filter(lambda x: x.endswith(".vcd"), os.listdir() ))
    for vcd_file in vcd_files:
        os.remove(vcd_file)
    
    out_files = list(filter(lambda x: x.endswith(".out"), os.listdir() ))
    for out_file in out_files:
        os.remove(out_file)

    # TODO : Load files from .vpackage/repos/

    exec_arr = ["iverilog"]
    for f in file_list:
        exec_arr.append(f)
    exec_arr.append("-I")
    exec_arr.append(".vpackage/repos/")
    print("[vivp]", " ".join(exec_arr))
    proc = subprocess.Popen(exec_arr)
    proc.wait()

    exec_str = "vvp a.out" # check list of .out files
    print("[vivp]", exec_str)
    proc = subprocess.Popen(exec_str.split(" "))
    proc.wait()

    vcd_files = list(filter(lambda x: x.endswith(".vcd"), os.listdir() ))
    if len(vcd_files)==0:
        Exception("Failed : no VCD Files")
    elif len(vcd_files)==1:
        exec_str = "gtkwave " + vcd_files[0]
        print("[vivp]", exec_str)
        proc = subprocess.Popen(exec_str.split(" "))
        proc.wait()
        print("[vivp]", "Done...")
    else:
        Exception("Failed : too many VCD Files")
    pass


def execute_legacy1(vivp_dir):
    """
    ## execute_legacy1(vivp_dir)
    Legacy testbench; Gathers all fileList from all dependencies and fileList+testBench List from current vivp_dir and runs it through iverilog

    Better to use include statements instead

    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. More than 1 VCD file
    3. No VCD Files
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    file_list = []
    for f in p.data['fileList']:
        #file_list.append('"' + os.path.join(vivp_dir, f) + '"')
        file_list.append(make_safe(os.path.join(vivp_dir, f)))
    for f in p.data['testBench']:
        #file_list.append('"' + os.path.join(vivp_dir, f) + '"')
        file_list.append(make_safe(os.path.join(vivp_dir, f)))
    dependency_files = get_files_from_dependencies(vivp_dir)
    for f in dependency_files:
        #file_list.append('"' + f + '"')
        file_list.append(make_safe(os.path.join(vivp_dir, f)))

    vcd_files = list(filter(lambda x: x.endswith(".vcd"), os.listdir() ))
    for vcd_file in vcd_files:
        os.remove(vcd_file)
    
    out_files = list(filter(lambda x: x.endswith(".out"), os.listdir() ))
    for out_file in out_files:
        os.remove(out_file)

    # TODO : Load files from .vpackage/repos/

    exec_str = "iverilog " + " ".join(file_list)
    exec_arr = ["iverilog"]
    for f in file_list:
        exec_arr.append(f)
    print("[vivp]", exec_str)
    #proc = subprocess.Popen(exec_str.split(" "))
    proc = subprocess.Popen(exec_arr)
    proc.wait()

    exec_str = "vvp a.out" # check list of .out files
    print("[vivp]", exec_str)
    proc = subprocess.Popen(exec_str.split(" "))
    proc.wait()

    vcd_files = list(filter(lambda x: x.endswith(".vcd"), os.listdir() ))
    if len(vcd_files)==0:
        Exception("Failed : no VCD Files")
    elif len(vcd_files)==1:
        exec_str = "gtkwave " + vcd_files[0]
        print("[vivp]", exec_str)
        proc = subprocess.Popen(exec_str.split(" "))
        proc.wait()
        print("[vivp]", "Done...")
    else:
        Exception("Failed : too many VCD Files")
    pass


def add_testbench(vivp_dir, file_list):
    """
    ## add_testbench(vivp_dir, file_list)
    Adds file_list to 'testBench' list 


    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. File Already in List
    3. Invalid file path
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    for f in file_list:
        if is_sub_file(vivp_dir, f):
            if not p.has_testbench(f):
                p.data['testBench'].append(f)
            else:
                raise Exception("File already in list : " + f)
        else:
            raise Exception("Invalid path : " + f)
    p.save()


def remove_testbench(vivp_dir, file_list):
    """
    ## remove_testbench(vivp_dir, file_list)
    Removes file_list from 'testBench' list 


    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. File not in List
    3. Invalid file path
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    for f in file_list:
        if is_sub_file(vivp_dir, f):
            if p.has_testbench(f):
                p.data['testBench'].remove(f)
            else:
                raise Exception("File not in list : " + f)
        else:
            raise Exception("Invalid path : " + f)
    p.save()


def add_files(vivp_dir, file_list):
    """
    ## add_files(vivp_dir, file_list)
    Adds file_list to 'fileList' list 


    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. File Already in List
    3. Invalid file path
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    for f in file_list:
        if is_sub_file(vivp_dir, f):
            if not p.has_file(f):
                p.data['fileList'].append(f)
            else:
                raise Exception("File already in list : " + f)
        else:
            raise Exception("Invalid path : " + f)
    p.save()


def remove_files(vivp_dir, file_list):
    """
    ## remove_files(vivp_dir, file_list)
    Removes file_list from 'fileList' list 


    ### Raises exception if

    1. Input directory does not have a vpackage.json
    2. File not in List
    3. Invalid file path
    """
    if not is_vivp_dir(vivp_dir):
        raise Exception("Not VIVP directory")
    p = vPackage(filePath=os.path.join(vivp_dir, VPACKAGE_JSON), createNew=False, saveable=True)
    for f in file_list:
        if is_sub_file(vivp_dir, f):
            if p.has_file(f):
                p.data['fileList'].remove(f)
            else:
                raise Exception("File not in list : " + f)
        else:
            raise Exception("Invalid path : " + f)
    p.save()