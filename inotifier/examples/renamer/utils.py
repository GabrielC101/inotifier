from os import path, stat, walk
from os.path import abspath, join
try:
    import psutil
except (ImportError, NameError) as e:
    raise ImportError('Must install psutil to use renamer example!') from e
from inotifier.models.path import Path


def lookup_inode(inode, rootdir='.') -> Path:
    """Find a file path for an inode."""
    for folder, subs, files in walk(rootdir):

        for f in files:
            absolute_path = abspath(join(folder, f))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return Path(absolute_path).absolute()

        for s in subs:
            absolute_path = path.abspath(join(folder, s))
            ap_inode = stat(absolute_path).st_ino
            if inode == ap_inode:
                return Path(absolute_path).absolute()


def is_file_open(file_path='./test/'):
    """Check if a file is currently open."""
    file_path = Path(file_path)

    process_list = _get_open_files()
    for processes in process_list:
        if file_path.absolute() in processes:
            return True
    return False


def _get_open_files():
    """Returns a list of open files."""
    for proc in psutil.process_iter():
        try:
            open_file = proc.open_files()
        except Exception:
            open_file = []
        return [o.path for o in open_file]
