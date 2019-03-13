#!/usr/bin/env python

from __future__ import absolute_import, print_function

import datetime

from os.path import join

from twisted.python.filepath import FilePath

from inotifier.models.masks import InotifyMask


class InotifyEvent(object):

    @classmethod
    def build_from_inotify_adapter(cls, base_event):
        (header, type_names, watch_path, filename) = base_event
        mask = header.mask
        file_path = join(watch_path, filename)
        return cls(mask, file_path, watch_path)

    def __init__(self, mask, file_changed, watch_path):
        self.mask = InotifyMask(mask)
        self.file_changed = FilePath(file_changed)
        self.watch_path = FilePath(watch_path)
        self.time = datetime.datetime.now()

    @property
    def inode_num(self):
        try:
            return self.file_changed.getInodeNumber()
        except OSError as e:
            return None
        
    def initiate_time_as_string(self):
        template = "{}-{}-{}---{}-{}-{}"
        return template.format(
            self.time.year,
            self.time.month,
            self.time.day,
            self.time.hour,
            self.time.minute,
            self.time.second
        )
