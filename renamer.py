from inotifier import InotifyFileMonitorBase
from isFileOpen import monitorIsFileOpen, isFileOpen
from twisted.python import filepath
import os
import sys

sep = '---'

event_log_dict = {}

created_dict = {}

closed_write_list = []

changed_list = []

def log_inotify_event(inotify_event):
    global event_log_dict
    file_changed = inotify_event.file_changed.path
    if inotify_event.file_changed.exists():
        inode_changed = inotify_event.file_changed.getInodeNumber()
    else:
        inode_changed = None
    type_of_change = inotify_event.mask.readable_mask[0]
    if inode_changed in event_log_dict:
        event_log_dict[inode_changed].append((file_changed,type_of_change))
    else:
        event_log_dict[inode_changed] = []
        event_log_dict[inode_changed].append((file_changed,type_of_change))

    #print event_log_dict




class Renamer(InotifyFileMonitorBase):
    #def __init__(self, initial_watch_path):
        #sep = '---'
        #super(Renamer, self).__init__()

    def allEvents(self, inotify_event):
        if inotify_event.file_changed.exists():
            log_inotify_event(inotify_event)

    def On_IN_CREATE(self, inotify_event):
        #log_inotify_event(inotify_event)
        sep = '---'

        created_dict[inotify_event.file_changed.getInodeNumber()] = \
        str(inotify_event.time.year) + '-' + \
        str(inotify_event.time.month) + '-' + \
        str(inotify_event.time.day) + '---' + \
        str(inotify_event.time.hour) + '-' + \
        str(inotify_event.time.minute) + '-' + \
        str(inotify_event.time.second)

        #print created_dict

    def On_IN_CLOSE_WRITE(self, inotify_event):
        if inotify_event.file_changed.exists():
            closed_write_list.append(inotify_event.file_changed.getInodeNumber())

    def On_IN_MOVED_FROM(self, inotify_event):
        #log_inotify_event(inotify_event)
        pass
    def On_IN_MOVED_TO(self, inotify_event):
        #log_inotify_event(inotify_event)
        pass
    def On_IN_ATTRIB(self, inotify_event):
        if inotify_event.file_changed.exists():
            inode_num = inotify_event.file_changed.getInodeNumber()
            if inode_num not in changed_list:
                if '---' not in inotify_event.file_changed.path:
                    t = True

                    file_name = inotify_event.file_changed.path

                    if inode_num not in changed_list:
                        while t:
                            if isFileOpen(file_name) == False:
                                self.rename(file_name, created_dict[inode_num])
                                return


    def change(self, inotify_event):
        pass

    def rename(self, file_name, created_time_string):
        file_name = filepath.FilePath(file_name)
        b_name = file_name.basename()
        par = file_name.parent()
        new_path = filepath.FilePath(par.path + '/' + created_time_string + sep + b_name)

        os.rename(file_name.path, new_path.path)

        print file_name.path
        print new_path.path
        if new_path.exists():
            changed_list.append(new_path.getInodeNumber())




def main(folder_to_monitor):
    fm = Renamer(folder_to_monitor)


if __name__ == '__main__':

    main(sys.argv[1])
