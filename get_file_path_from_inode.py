#!/usr/bin/env python

from __future__ import absolute_import, print_function
from sys import argv
import os


def get_file_path_from_inode(inode, rootdir='.'):
    for folder, subs, files in os.walk(rootdir):

        for f in files:
            absolute_path = os.path.abspath(os.path.join(folder, f))
            ap_inode = os.stat(absolute_path).st_ino
            if inode == ap_inode:
                return absolute_path

        for s in subs:
            absolute_path = os.path.abspath(os.path.join(folder, s))
            ap_inode = os.stat(absolute_path).st_ino
            if inode == ap_inode:
                return absolute_path


def main(inode):
    for i in inode:
        i = int(i)
        print('finding filepath for inode {}:'.format(i))
        print(get_file_path_from_inode(i))


if __name__ == '__main__':
    args = argv[1:]
    main(args)
