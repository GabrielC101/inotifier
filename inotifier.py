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
            i.remove_watch('./text')


def main():
    fm = InotifyFileMonitor()


if __name__ == '__main__':
    main()
