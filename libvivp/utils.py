# === Utilities used by libvivp ===

import os
from git import Git
from urllib.parse import urlparse

VPACKAGE_JSON = 'vpackage.json'
VPACKAGE_HIDDEN = '.vpackage'
REPOS = 'repos'

def replaceAll(s, subs, rep):
    """
    Replaces all substrings in a string with another string
    """
    count = 0
    for i in s:
        if i == subs:
            count += 1
    return s.replace(subs, rep, count)


def make_safe(s):
    """Replaces all spaces with \\\\"""
    return replaceAll(s, " ", "\\ ")


def is_vivp_dir(d):
    """Returns True if d is a vivp directory, False otherwise"""
    return os.path.exists(os.path.join(d, VPACKAGE_JSON))
    if not os.path.exists(os.path.join(d, VPACKAGE_JSON)):
        return False
    # TODO : Validate the vpackage.json file

    try: # Check if git repo
        g = Git(d)
        g.remote()
    except:
        return False
    return True


def is_vivp_file(d):
    """Returns True if d is a vpackage.json, False otherwise"""
    # TODO : Validate the vpackage.json structure and validity
    try:
      open(d, "r")
      return True
    except IOError:
      return False


def is_sub_file(vivp_dir, d):
    """Returns True if d is a file within the directory vivp_dir, False otherwise"""
    try:
      open(os.path.join(vivp_dir, d), "r")
      return True
    except IOError:
      return False


def is_valid_git_url(u):
    """Returns True if u is a valid git URL, False otherwise"""
    try:
        a = urlparse(u)
        if a.netloc == "github.com":
            return True
        else:
            return False
    except:
        return False
    return True


def get_cache_dir(vivp_dir):
    """returns the chache directory withing vivp_dir"""
    return os.path.join(vivp_dir, VPACKAGE_HIDDEN)


def get_repos_dir(vivp_dir):
    """returns the repos directory withing vivp_dir"""
    return os.path.join(vivp_dir, VPACKAGE_HIDDEN, REPOS)