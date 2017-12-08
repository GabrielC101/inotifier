import psutil
from twisted.python.filepath import FilePath


def is_file_open(file='./test/'):
    """Check if a file is currently open."""
    file = FilePath(file)

    process_list = get_processes_list()
    for l in process_list:
        if file.path in l:
            return True
    return False


def get_processes_list():
    """Returns all open process as list"""
    proc = get_processes()
    proc_list = []
    for p in proc:
        proc_list.append(p)
    return proc_list


def get_processes():
    """Returns a generator the gives the paths of all open files, excluding those requiring root access"""
    for proc in psutil.process_iter():
        try:
            open_file = proc.open_files()
        except Exception as e:
            open_file = False
        if open_file:
            for o in open_file:
                yield o.path


def monitor_is_file_open(file_path):
    """Return a generator that monitors whether a file is open."""
    t = True
    while t:
        i = is_file_open(file_path)
        yield i


def main(file_path='./test'):
    g = monitor_is_file_open(file_path)
    for a in g:
        print a
        #if a == False:
        #    return 0


if __name__ == '__main__':
    main()

