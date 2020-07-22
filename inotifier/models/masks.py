from inotify.constants import *

class ReadableDict:
    def __getitem__(self, key):
        return key.lower()[3:]


readable_dict = ReadableDict()


_FLAG_TO_HUMAN = [
    (IN_ACCESS, 'access'),
    (IN_MODIFY, 'modify'),
    (IN_ATTRIB, 'attrib'),
    (IN_CLOSE_WRITE, 'close_write'),
    (IN_CLOSE_NOWRITE, 'close_nowrite'),
    (IN_OPEN, 'open'),
    (IN_MOVED_FROM, 'moved_from'),
    (IN_MOVED_TO, 'moved_to'),
    (IN_CREATE, 'create'),
    (IN_DELETE, 'delete'),
    (IN_DELETE_SELF, 'delete_self'),
    (IN_MOVE_SELF, 'move_self'),
    (IN_UNMOUNT, 'unmount'),
    (IN_Q_OVERFLOW, 'queue_overflow'),
    (IN_IGNORED, 'ignored'),
    (IN_ONLYDIR, 'only_dir'),
    (IN_DONT_FOLLOW, 'dont_follow'),
    (IN_MASK_ADD, 'mask_add'),
    (IN_ISDIR, 'is_dir'),
    (IN_ONESHOT, 'one_shot')
]


class InotifyMask:

    def __init__(self, mask):
        self.mask = mask
        self.human_readable_mask = self.human_readable_mask(self.mask)

    def human_readable_mask(self, mask):
        """
        Auxiliary function that converts an hexadecimal mask into a series
        of human readable flags.
        """
        s = []
        for k, v in _FLAG_TO_HUMAN:
            if k & mask:
                s.append(readable_dict[MASK_LOOKUP[k]])
        return s

    @property
    def readable_mask(self):
        """
        Auxiliary function that converts an hexadecimal mask into a series
        of human readable flags.
        """
        s = []
        for k, v in _FLAG_TO_HUMAN:
            if k & self.mask:
                s.append(MASK_LOOKUP[k])
        return s

    def as_string(self):
        return self.readable_mask
