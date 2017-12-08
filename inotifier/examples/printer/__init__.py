#!/usr/bin/env python

from __future__ import absolute_import, print_function

from inotifier.inotifier import InotifierBase


class Printer(InotifierBase):
    def all_events(self, inotify_event):
        print(inotify_event.mask.human_readable_mask)
        print(inotify_event.file_changed)
