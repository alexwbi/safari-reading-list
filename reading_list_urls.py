import plistlib

BOOKMARKS_PATH = 'Library/Safari/Bookmarks.plist'


def get_reading_list_urls():
    with open(BOOKMARKS_PATH, 'rb') as f:
        bookmarks = plistlib.load(f)
    pass
