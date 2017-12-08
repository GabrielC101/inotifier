#!/usr/bin/env python

from __future__ import absolute_import, print_function

from os import walk, stat, path
from os.path import abspath, join


def lookup_inode(inode, rootdir='.'):
    """Find a file path for an inode."""
    for folder, subs, files in walk(rootdir):

        for f in files:
            absolute_path = abspath(join(folder, f))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return absolute_path

        for s in subs:
            absolute_path = path.abspath(join(folder, s))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return absolute_path