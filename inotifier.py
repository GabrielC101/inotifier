import inotify.adapters
from os import path
from twisted.python.filepath import FilePath
from humanReadableMask import InotifyMask


class InotifyEvent(object):
    def __init__(self, mask, file_changed, watch_path):
        self.mask = mask
        self.file_changed = file_changed
        self.watch_path = watch_path

class InotifyFileMonitorBase(object):
    def __init__(self, initial_watch_path='.'):

        #self.initial_watch_path = initial_watch_path

        self._event_method_dict ={
        'IN_ACCESS':self.On_IN_ACCESS,
        'IN_MODIFY':self.On_IN_MODIFY,
        'IN_ATTRIB':self.On_IN_ATTRIB,
        'IN_CLOSE_WRITE':self.On_IN_CLOSE_WRITE,
        'IN_CLOSE_NOWRITE':self.On_IN_CLOSE_NOWRITE,
        'IN_OPEN':self.On_IN_OPEN,
        'IN_MOVED_FROM':self.On_IN_MOVED_FROM,
        'IN_MOVED_TO':self.On_IN_MOVED_TO,
        'IN_CREATE':self.On_IN_CREATE,
        'IN_DELETE':self.On_IN_DELETE,
        'IN_DELETE_SELF':self.On_IN_DELETE_SELF,
        'IN_MOVE_SELF':self.On_IN_MOVE_SELF,
        'IN_UNMOUNT':self.On_IN_UNMOUNT,
        'IN_Q_OVERFLOW':self.On_IN_Q_OVERFLOW,
        'IN_IGNORED':self.On_IN_IGNORED,
        'IN_ONLYDIR':self.On_IN_ONLYDIR,
        'IN_DONT_FOLLOW':self.On_IN_DONT_FOLLOW,
        'IN_MASK_ADD':self.On_IN_MASK_ADD,
        'IN_ISDIR':self.On_IN_ISDIR,
        'IN_ONESHOT':self.On_IN_ONESHOT
        }

        initial_watch_path = path.abspath(initial_watch_path)
        initial_watch_path = path.normpath(initial_watch_path)

        self.i = inotify.adapters.Inotify()
        self.i.add_watch(initial_watch_path)
        try:
            for base_event in self.i.event_gen():
                if base_event is not None:
                    (header, type_names, watch_path, filename) = base_event
                    mask = InotifyMask(header.mask)
                    file_path = FilePath(path.join(watch_path, filename))


                    inotify_event = InotifyEvent(mask,file_path, watch_path)

                    self.allEvents(inotify_event)

                    #print mask.mask
                    #print mask.readable_mask
                    #print mask.human_readable_mask
                    #print file_path.path
                   
        finally:
            self.i.remove_watch('./test')

    def allEvents(self, inotify_event):
        #print inotify_event.mask.readable_mask
        for r in inotify_event.mask.readable_mask:
            self._event_method_dict[r](inotify_event)



    def On_IN_ACCESS(self, inotify_event):
        pass

    def On_IN_MODIFY(self, inotify_event):
        pass

    def On_IN_ATTRIB(self, inotify_event):
        pass

    def On_IN_CLOSE_WRITE(self, inotify_event):
        pass

    def On_IN_CLOSE_NOWRITE(self, inotify_event):
        pass

    def On_IN_OPEN(self, inotify_event):
        pass

    def On_IN_MOVED_FROM(self, inotify_event):
        pass

    def On_IN_MOVED_TO(self, inotify_event):
        pass

    def On_IN_CREATE(self, inotify_event):
        pass

    def On_IN_DELETE(self, inotify_event):
        pass

    def On_IN_DELETE_SELF(self, inotify_event):
        pass

    def On_IN_MOVE_SELF(self, inotify_event):
        pass

    def On_IN_UNMOUNT(self, inotify_event):
        pass

    def On_IN_Q_OVERFLOW(self, inotify_event):
        pass

    def On_IN_IGNORED(self, inotify_event):
        pass

    def On_IN_ONLYDIR(self, inotify_event):
        pass

    def On_IN_DONT_FOLLOW(self, inotify_event):
        pass

    def On_IN_MASK_ADD(self, inotify_event):
        pass

    def On_IN_ISDIR(self, inotify_event):
        pass

    def On_IN_ONESHOT(self, inotify_event):
        pass






def main():
    fm = InotifyFileMonitorBase('./test')


if __name__ == '__main__':
    main()
