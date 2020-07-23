import datetime
from os.path import join

from inotifier.models.masks import InotifyMask
from inotifier.models.path import Path


class InotifyEvent:

    @classmethod
    def build_from_inotify_adapter(cls, base_event):
        (header, type_names, watch_path, filename) = base_event
        mask = header.mask
        file_path = join(watch_path, filename)
        return cls(mask, file_path, watch_path)

    def __init__(self, mask, file_changed, watch_path):
        self.mask = InotifyMask(mask)
        self.file_changed: Path = Path(file_changed)
        self.watch_path: Path = Path(watch_path)
        self.time: datetime.datetime = datetime.datetime.now()

    @property
    def inode_number(self):
        try:
            return self.file_changed.inode_number
        except FileNotFoundError:
            return None

    def initiate_time_as_string(self):
        return self.time.isoformat().replace(':', '-').split('.')[0]

