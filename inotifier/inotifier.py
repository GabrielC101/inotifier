from __future__ import absolute_import, print_function

from os import path

import inotify.adapters

from inotifier.events import InotifyEvent
from inotifier.utils import lookup_inode


class InotifierBase(object):
    def __init__(self, initial_watch_path='.'):

        self._event_method_dict = {
            'IN_ACCESS': self.on_IN_ACCESS,
            'IN_MODIFY': self.on_IN_MODIFY,
            'IN_ATTRIB': self.on_IN_ATTRIB,
            'IN_CLOSE_WRITE': self.on_IN_CLOSE_WRITE,
            'IN_CLOSE_NOWRITE': self.on_IN_CLOSE_NOWRITE,
            'IN_OPEN': self.on_IN_OPEN,
            'IN_MOVED_FROM': self.on_IN_MOVED_FROM,
            'IN_MOVED_TO': self.on_IN_MOVED_TO,
            'IN_CREATE': self.on_IN_CREATE,
            'IN_DELETE': self.on_IN_DELETE,
            'IN_DELETE_SELF': self.on_IN_DELETE_SELF,
            'IN_MOVE_SELF': self.on_IN_MOVE_SELF,
            'IN_UNMOUNT': self.on_IN_UNMOUNT,
            'IN_Q_OVERFLOW': self.on_IN_Q_OVERFLOW,
            'IN_IGNORED': self.on_IN_IGNORED,
            'IN_ONLYDIR': self.on_IN_ONLYDIR,
            'IN_DONT_FOLLOW': self.on_IN_DONT_FOLLOW,
            'IN_MASK_ADD': self.on_IN_MASK_ADD,
            'IN_ISDIR': self.on_IN_ISDIR,
            'IN_ONESHOT': self.on_IN_ONESHOT
        }

        initial_watch_path = path.normpath(path.abspath(initial_watch_path))

        self.i = inotify.adapters.Inotify()
        self.i.add_watch(initial_watch_path)
        try:
            for base_event in self.i.event_gen():
                if base_event is not None:
                    inotify_event = InotifyEvent.build_from_inotify_adapter(base_event)
                    self.__process_event(inotify_event)
        finally:
            self.i.remove_watch('./test')

    def __process_event(self, inotify_event):
        for r in inotify_event.mask.readable_mask:
            self.all_events(inotify_event)
            self._event_method_dict[r](inotify_event)

    def all_events(self, inotify_event):
        pass

    def on_IN_ACCESS(self, inotify_event):
        pass

    def on_IN_MODIFY(self, inotify_event):
        pass

    def on_IN_ATTRIB(self, inotify_event):
        pass

    def on_IN_CLOSE_WRITE(self, inotify_event):
        pass

    def on_IN_CLOSE_NOWRITE(self, inotify_event):
        pass

    def on_IN_OPEN(self, inotify_event):
        pass

    def on_IN_MOVED_FROM(self, inotify_event):
        pass

    def on_IN_MOVED_TO(self, inotify_event):
        pass

    def on_IN_CREATE(self, inotify_event):
        pass

    def on_IN_DELETE(self, inotify_event):
        pass

    def on_IN_DELETE_SELF(self, inotify_event):
        pass

    def on_IN_MOVE_SELF(self, inotify_event):
        pass

    def on_IN_UNMOUNT(self, inotify_event):
        pass

    def on_IN_Q_OVERFLOW(self, inotify_event):
        pass

    def on_IN_IGNORED(self, inotify_event):
        pass

    def on_IN_ONLYDIR(self, inotify_event):
        pass

    def on_IN_DONT_FOLLOW(self, inotify_event):
        pass

    def on_IN_MASK_ADD(self, inotify_event):
        pass

    def on_IN_ISDIR(self, inotify_event):
        pass

    def on_IN_ONESHOT(self, inotify_event):
        pass
