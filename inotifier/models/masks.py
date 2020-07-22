from inotify import constants

class ReadableDict:
    def __getitem__(self, key):
        return key.lower()[3:]


readable_dict = ReadableDict()


_FLAG_TO_HUMAN = [
    (constants.IN_ACCESS, 'access'),
    (constants.IN_MODIFY, 'modify'),
    (constants.IN_ATTRIB, 'attrib'),
    (constants.IN_CLOSE_WRITE, 'close_write'),
    (constants.IN_CLOSE_NOWRITE, 'close_nowrite'),
    (constants.IN_OPEN, 'open'),
    (constants.IN_MOVED_FROM, 'moved_from'),
    (constants.IN_MOVED_TO, 'moved_to'),
    (constants.IN_CREATE, 'create'),
    (constants.IN_DELETE, 'delete'),
    (constants.IN_DELETE_SELF, 'delete_self'),
    (constants.IN_MOVE_SELF, 'move_self'),
    (constants.IN_UNMOUNT, 'unmount'),
    (constants.IN_Q_OVERFLOW, 'queue_overflow'),
    (constants.IN_IGNORED, 'ignored'),
    (constants.IN_ONLYDIR, 'only_dir'),
    (constants.IN_DONT_FOLLOW, 'dont_follow'),
    (constants.IN_MASK_ADD, 'mask_add'),
    (constants.IN_ISDIR, 'is_dir'),
    (constants.IN_ONESHOT, 'one_shot')
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
                s.append(readable_dict[constants.MASK_LOOKUP[k]])
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
                s.append(constants.MASK_LOOKUP[k])
        return s

    def as_string(self):
        return self.readable_mask
