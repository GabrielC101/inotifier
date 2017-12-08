import psutil
from twisted.python.filepath import FilePath


def is_file_open(file='./test/'):
    """Check if a file is currently open."""
    file = FilePath(file)

    process_list = get_open_files()
    for l in process_list:
        if file.path in l:
            return True
    return False


def get_open_files():
    """Returns a list of open files."""
    for proc in psutil.process_iter():
        try:
            open_file = proc.open_files()
        except Exception as e:
            open_file = []
        return [o.path for o in open_file]


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


if __name__ == '__main__':
    main()

