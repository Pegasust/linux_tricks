#!/usr/bin/env python3
"""
The Linux filesystem abbreviator such that
there is no ambiguity for each directory
when pressing TAB

The program assumes that the input folder is valid
"""
from typing import Dict, List
import os

def path_join(path: List[str])->str:
    """
    Joins all directories in `path`
    `path` is formatted: `/etc/hello/world/`->`[etc, hello, world]`
      NOTE: root (`/`)->[]
    """
    if len(path) == 0:
        return os.path.sep
    return f"{os.path.sep}{os.path.join(*path)}"

def abbreviate(raw_path: List[str], env_hints: Dict[str, str]=None)->List[str]:
    """
    Abbreviates the `raw_path` into a path that can be expanded
    by pressing tab per item:
    /home/u20/pegasust/some/very/long/directory_name_here/for_some_obvious_reasons/
    becomes
    ideally: /h/u/p/s/v/l/d/f/
    or:      /ho/u2/pegas/s/v/l/directory_na/for_some_/

    Note that raw_path is always absolute path, and is passed in like this:
    [home, u20, pegasust, some, very, long, directory_name_here, for_some_obvious_reasons]

    params:
      raw_path: absolute path that are separated by path separator. Guaranteed to be a path
        to a directory/folder
      env_hints: [optional & optionally used]: The symbols that may be used to substitute
        to minimize the path length
    """
    env_hints = dict() if not env_hints else env_hints
    path_so_far: str
    path_so_far = path_join([])

    retval = []
    for i, path in enumerate(raw_path):
        if len(path) == 0:
            continue
        dirs = set(os.listdir(path_so_far))
        dirs.remove(path)
        all_prefixes = set()
        for dir in dirs:
            pathlet = ""
            for c in dir:
                pathlet += c
                all_prefixes.add(pathlet)
        pathlet = ""
        for c in path:
            pathlet += c
            if pathlet not in all_prefixes:
                retval.append(pathlet)
                break
        path_so_far = os.path.join(path_so_far, path)
    return retval

def main(raw_path:List[str], env_hints:Dict[str, str])->str:
    return path_join(abbreviate(path, hints))

if __name__ == "__main__":
    import sys
    path = sys.argv[1].split('/')[1:]
    _hints = sys.argv[2:]
    hints = dict()
    for entry in _hints:
        k, v = entry.split(os.path.sep)
        hints[k]=v
    
    print(path_join(abbreviate(path, hints)))
    
