#!/usr/bin/env python3

from sys import argv

from inotifier.inotifier import InotifierBase
from inotifier.models.events import InotifyEvent


class Printer(InotifierBase):
    def all_events(self, inotify_event: InotifyEvent):
        template = "{} changed by {} events".format(
            str(inotify_event.file_changed),
            inotify_event.mask.human_readable_mask
        )
        print(template)


def main(folder_to_monitor):
    Printer(folder_to_monitor).run()


if __name__ == '__main__':

    main(argv[1])
