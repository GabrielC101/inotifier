import inotify.adapters
from os import path
from twisted.python.filepath import FilePath
from humanReadableMask import InotifyMask



class InotifyFileMonitor(object):
    def __init__(self, watch_path='./test'):
        i = inotify.adapters.Inotify()
        i.add_watch(watch_path)
        try:
            for event in i.event_gen():
                if event is not None:
                    (header, type_names, watch_path, filename) = event
                    mask = InotifyMask(header.mask)
                    file_path = FilePath(path.join(watch_path, filename))
                    print mask.mask
                    print mask.readable_mask
                    print mask.human_readable_mask
                    print file_path.path
                    '''
                    imask = humanReadableMask.humanReadableMask(header.mask)
                    print imask[0]
                    print path.join(watch_path,filename)
                    print watch_path
                    print '-----------------------'
                    print
                    '''
        finally:
            i.remove_watch('./test')

'''



'''
    def On_IN_ACCESS(self, mask, file_path):
        pass

    def On_IN_MODIFY(self, mask, file_path):
        pass

    def On_IN_ATTRIB(self, mask, file_path):
        pass

    def On_IN_CLOSE_WRITE(self, mask, file_path):
        pass

    def On_IN_CLOSE_NOWRITE(self, mask, file_path):
        pass

    def On_IN_OPEN(self, mask, file_path):
        pass

    def On_IN_MOVED_FROM(self, mask, file_path):
        pass

    def On_IN_MOVED_TO(self, mask, file_path):
        pass

    def On_IN_CREATE(self, mask, file_path):
        pass

    def On_IN_DELETE(self, mask, file_path):
        pass

    def On_IN_DELETE_SELF(self, mask, file_path):
        pass

    def On_IN_MOVE_SELF(self, mask, file_path):
        pass

    def On_IN_UNMOUNT(self, mask, file_path):
        pass

    def On_IN_Q_OVERFLOW(self, mask, file_path):
        pass

    def On_IN_IGNORED(self, mask, file_path):
        pass

    def On_IN_ONLYDIR(self, mask, file_path):
        pass

    def On_IN_DONT_FOLLOW(self, mask, file_path):
        pass

    def On_IN_MASK_ADD(self, mask, file_path):
        pass

    def On_IN_ISDIR(self, mask, file_path):
        pass

    def On_IN_ONESHOT(self, mask, file_path):
        pass






def main():
    fm = InotifyFileMonitor()


if __name__ == '__main__':
    main()
