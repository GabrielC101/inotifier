from os import path
from time import sleep
from typing import Optional

import inotify.adapters

from inotifier.models.events import InotifyEvent


class InotifierBase:
    def __init__(self, initial_watch_path: str = '.', include_dirs=True):
        self.include_dirs = include_dirs
        self.initial_watch_path: str = path.normpath(
            path.abspath(initial_watch_path)
        )
        self.i: Optional[inotify.adapters.Inotify] = None

    def run(self):
        self.i = inotify.adapters.Inotify()
        self.i.add_watch(self.initial_watch_path)
        try:
            for base_event in self.i.event_gen():
                if base_event is not None:
                    inotify_event: InotifyEvent = InotifyEvent.build_from_inotify_adapter(
                        base_event
                    )
                    if self.include_dirs or (
                            not self.include_dirs and 'isdir' not in inotify_event.mask.human_readable_mask
                    ):
                        self.__process_event(inotify_event)
                sleep(.1)
        finally:
            # Cleans up watches via __del__ method.
            del self.i

    def __process_event(self, inotify_event: InotifyEvent) -> None:
        for r in inotify_event.mask.readable_mask:
            self.all_events(inotify_event)
            method = getattr(self, f'on_{r}')
            method(inotify_event)

    def all_events(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_ACCESS(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_MODIFY(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_ATTRIB(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_CLOSE_WRITE(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_CLOSE_NOWRITE(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_OPEN(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_MOVED_FROM(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_MOVED_TO(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_CREATE(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_DELETE(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_DELETE_SELF(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_MOVE_SELF(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_UNMOUNT(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_Q_OVERFLOW(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_IGNORED(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_ONLYDIR(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_DONT_FOLLOW(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_MASK_ADD(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_ISDIR(self, inotify_event: InotifyEvent) -> None:
        pass

    def on_IN_ONESHOT(self, inotify_event: InotifyEvent) -> None:
        pass
