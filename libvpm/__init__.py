import os
import json
from .utils import is_vpm_dir, VPACKAGE_JSON, is_valid_git_url, VPACKAGE_HIDDEN, get_repos_dir, get_cache_dir
from .vPackage import vPackage
from git import Git
import git
import shutil

def setup(vpm_dir, packageName, packageAuthors, packageURL):
    if is_vpm_dir(vpm_dir):
        raise Exception("Already VPM directory")
    p = vPackage(filePath=os.path.join(vpm_dir, VPACKAGE_JSON), createNew=True, saveable=True)
    p.data['packageDetails']['packageName'] = packageName
    p.data['packageDetails']['packageAuthors'] = packageAuthors
    if packageURL:
        if (is_valid_git_url(packageURL)):
            p.data['packageURL'] = packageURL
        else:
            raise Exception('Invalid packageURL : ' + packageURL)
    #g = Git(vpm_dir)
    p.save()
    print(p)
    pass

def install(vpm_dir, package_list):
    if not is_vpm_dir(vpm_dir):
        raise Exception("Not VPM directory")
    p = vPackage(filePath=os.path.join(vpm_dir, VPACKAGE_JSON), createNew=False, saveable=True)


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
    refresh_all_dependencies(vpm_dir)
    pass

def update(vpm_dir, package_list):
    if not is_vpm_dir(vpm_dir):
        raise Exception("Not VPM directory")
    pass

def remove(vpm_dir, package_list):
    if not is_vpm_dir(vpm_dir):
        raise Exception("Not VPM directory")
    p = vPackage(filePath=os.path.join(vpm_dir, VPACKAGE_JSON), createNew=False, saveable=True)


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
    refresh_all_dependencies(vpm_dir)
    pass

def list_vpm(vpm_dir):
    if not is_vpm_dir(vpm_dir):
        raise Exception("Not VPM directory")
    pass

def refresh_all_dependencies(vpm_dir):
    if not is_vpm_dir(vpm_dir):
        raise Exception("Not VPM directory")
    p = vPackage(filePath=os.path.join(vpm_dir, VPACKAGE_JSON), createNew=False, saveable=False)

    CACHE_DIR = get_cache_dir(vpm_dir)
    REPOS_DIR = get_repos_dir(vpm_dir)
    # Remove VPACKAGE_HIDDEN directory
    if os.path.isdir(CACHE_DIR):
        #os.rm(CACHE_DIR)
        shutil.rmtree(CACHE_DIR)

    os.makedirs(CACHE_DIR)
    os.makedirs(REPOS_DIR)

    # iterate through all packages and clone
    for dep in p.data['dependencyList']:
        output = git.Git(REPOS_DIR).clone(dep)
        print(output)

    pass