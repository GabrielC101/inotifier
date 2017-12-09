#!/usr/bin/env python

from __future__ import absolute_import, print_function


class Inode(object):
    def __init__(self, id_num):
        self.id = id_num
        self.file_paths = {}

