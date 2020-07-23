#!/usr/bin/env python3

import os
from sys import argv
from time import sleep

from inotifier.inotifier import InotifierBase
from inotifier.models.path import Path
from inotifier.utils import is_file_open, lookup_inode


class RenamerBase(InotifierBase):

    def __init__(self, *args, **kwargs):
        self.sep = '---'
        self.event_log_dict = {}
        self.changed_list = []
        kwargs['include_dirs'] = False
        super(RenamerBase, self).__init__(*args, **kwargs)

    def log_inotify_event(self, inotify_event):
        file_changed: Path = inotify_event.file_changed
        if inotify_event.file_changed.exists():
            inode_changed = inotify_event.file_changed.inode_number
        else:
            inode_changed = None
        type_of_change = inotify_event.mask.readable_mask[0]
        if inode_changed in self.event_log_dict:
            self.event_log_dict[inode_changed].append(
                (file_changed, type_of_change)
            )
        else:
            self.event_log_dict[inode_changed] = []
            self.event_log_dict[inode_changed].append(
                (file_changed, type_of_change)
            )

    def rename(self, file_name, created_time_string):
        file_name: Path = Path(file_name)
        b_name = file_name.name
        par = file_name.parent
        new_path = Path(
            str(par) + '/' + created_time_string + self.sep + b_name
        )

        os.rename(str(file_name), str(new_path))
        template = '{} renamed to {}'
        print(
            template.format(str(file_name), str(new_path))
        )
        if new_path.exists():
            self.changed_list.append(new_path.inode_number)
        print(
            "files changed: {}".format(
                self.changed_list
            )
        )


class Renamer(RenamerBase):

    def all_events(self, inotify_event):
        if inotify_event.file_changed.exists():
            self.log_inotify_event(inotify_event)

    def on_IN_ATTRIB(self, inotify_event):
        if inotify_event.file_changed.exists():
            inode_num = inotify_event.file_changed.inode_number
            if inode_num not in self.changed_list:
                if '---' not in str(inotify_event.file_changed):

                    file_name = str(inotify_event.file_changed)

                    if inode_num not in self.changed_list:

                        file_open = True
                        while file_open:
                            if not is_file_open(file_name):
                                sleep(5)
                                file_name = str(
                                    lookup_inode(
                                        inode_num,
                                        str(inotify_event.watch_path)
                                    )
                                )
                                self.rename(
                                    file_name,
                                    inotify_event.initiate_time_as_string()
                                )
                                file_open = False


def main(folder_to_monitor):
    Renamer(folder_to_monitor).run()


if __name__ == '__main__':

    main(argv[1])
