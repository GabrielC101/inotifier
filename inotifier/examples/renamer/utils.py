#!/usr/bin/env python

from __future__ import absolute_import, print_function

from os import walk, stat, path
from os.path import abspath, join

import psutil
from twisted.python.filepath import FilePath


def lookup_inode(inode, rootdir='.'):
    """Find a file path for an inode."""
    for folder, subs, files in walk(rootdir):

        for f in files:
            absolute_path = abspath(join(folder, f))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return FilePath(absolute_path)

        for s in subs:
            absolute_path = path.abspath(join(folder, s))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return FilePath(absolute_path)


def is_file_open(file='./test/'):
    """Check if a file is currently open."""
    file = FilePath(file)

    process_list = get_open_files()
    for l in process_list:
        if file.path in l:
            return True
    return False


def get_open_files():
    """Returns a list of open files."""
    for proc in psutil.process_iter():
        try:
            open_file = proc.open_files()
        except Exception as e:
            open_file = []
        return [o.path for o in open_file]


def monitor_is_file_open(file_path):
    """Return a generator that monitors whether a file is open."""
    t = True
    while t:
        i = is_file_open(file_path)
        yield i
