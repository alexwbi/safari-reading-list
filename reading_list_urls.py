import plistlib

BOOKMARKS_PATH = 'Library/Safari/Bookmarks.plist'
READING_LIST_KEY = 'com.apple.ReadingList'


def get_reading_list_urls():
    bookmarks = _read_file()
    reading_list = _reading_list(bookmarks)
    pass


def _read_file():
    with open(BOOKMARKS_PATH, 'rb') as f:
        return plistlib.load(f)


def _reading_list(bookmarks):
    return list(filter(lambda item: item['Title'] == READING_LIST_KEY, bookmarks['Children']))[0]
