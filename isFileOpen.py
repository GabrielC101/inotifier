import psutil
from twisted.python.filepath import FilePath
import sys
import os


#checks if a file is currently open
def isFileOpen(file='./test/'):
    #file = os.path.join(os.getcwd(),file)
    file = FilePath(file)

    print file.path
    list = getProcessesList()
    for l in list:
        if file.path in l:
            return True
    return False

#returns all open process as list
def getProcessesList():
    proc = getProcesses()
    proc_list = []
    for p in proc:
        proc_list.append(p)
    return proc_list

#returns a generator the gives the paths of all open files, excluding those requiring root access
def getProcesses():
    for proc in psutil.process_iter():
        try:
            open_file = proc.open_files()
        except:
            open_file = False
        if open_file:
            for o in open_file:
                yield o.path
#returns a generator that monitors whether a file is open
def monitorIsFileOpen(file):
    t = True
    while t:
        i = isFileOpen(file)
        yield i


def _main(file='./test'):
    g = monitorIsFileOpen(file)
    for a in g:
        print a
        #if a == False:
        #    return 0

if __name__ == '__main__':
    _main()

