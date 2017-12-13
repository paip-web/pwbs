#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - Watcher

This module creates functions to watch files as well as Hashing Files.
Watching files working by change in hash of files.

NAME - PAiP Web Module - Watcher
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.1
"""
# Imports
import hashlib
import os
import fnmatch
from datetime import datetime
# Functions
def __HashMessage():
    """Function for Print Message every HashFiles Function run
    """
    print("\r[{0}]: Hashing Files...".format(datetime.now().strftime("%H:%M:%S")), end="")
def __HashNull():
    """Null Function for HashFiles Function
    """
    pass

def md5(fname):
    """Function to make md5 hash of file
    Args:
        fname (object): File Name

    Returns:
        :obj:`str`: Returning Hash of File
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def findFiles(path_to_watch, arg_files):
    """Function to find files that matching pattern
    Args:
        path_to_watch (object): Path of starting recursive search of files
        arg_files (object): Filename Regular Expression String (like "*.py")

    Returns:
        :obj:`str`: Returning Matches of search
    """
    matches = []
    for root, dirnames, filenames in os.walk(path_to_watch):
        for filename in fnmatch.filter(filenames, arg_files):
            matches.append(os.path.join(root, filename))
    return matches

def HashFiles(path_to_watch, filenames_to_watch, excluded=[], message=__HashNull):
    """Function to hash files
    Args:
        path_to_watch (object): Path of starting recursive search of files
        filenames_to_watch (object): Filename Regular Expression String (like "*.py")
        excluded (object): Excluded items from hashing
        message (function): Function to do before hashing [Can be print]

    Returns:
        :obj:`list`: Returning List of Files Hashes
    """
    message()
    watch_files = findFiles(path_to_watch, filenames_to_watch)
    watch_files = [item for item in watch_files if item not in excluded]
    hash_table = []
    for x in watch_files:
        hash_table.append(md5(x))
    return hash_table

def watchFile(path_to_watch, filenames_to_watch, excluded={}, function=print):
    """Function to watch file for changes
    TODO: CODE CHANGE
    """
    ex2 = []
    for ex, ex1 in excluded.items():
        ex3 = findFiles(ex, ex1)
        ex2 += ex3
    excluded = ex2
    while True:
        lastHash = HashFiles(path_to_watch, filenames_to_watch, excluded)
        while lastHash == HashFiles(path_to_watch, filenames_to_watch, excluded):
            try:
                with open("stop.watching.file.1234567890", "r") as f:
                    #print("PWCIW: Locking File Exist")
                    raise Exception("STOP")
            except FileNotFoundError:
                continue
        try:
            with open("stop.watching.file.1234567890", "r") as f:
                #print("PWCIW: Locking File Exist")
                raise Exception("STOP")
        except FileNotFoundError:
            pass
        #print("\nPWCIW: Hash Changed")
        function()
