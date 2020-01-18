import plistlib

BOOKMARKS_PATH = 'Library/Safari/Bookmarks.plist'


def get_reading_list_urls():
    bookmarks = _read_file()
    pass


def _read_file():
    with open(BOOKMARKS_PATH, 'rb') as f:
        return plistlib.load(f)
