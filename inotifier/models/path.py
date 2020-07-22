from pathlib import Path as _Path


# pathlib.Path can't be directly subclassed
# because of how the class is dynamically generated.
class Path(type(_Path())):

    @property
    def inode_number(self):
        return self.stat().st_ino
