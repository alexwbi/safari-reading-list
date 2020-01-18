import csv
import plistlib

BOOKMARKS_PATH = 'Library/Safari/Bookmarks.plist'
READING_LIST_KEY = 'com.apple.ReadingList'
CSV_HEADING = ['Reading List (in reverse chronological order)']


def reading_list_csv():
    urls = get_reading_list_urls()
    with open('reading_list_urls.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(CSV_HEADING + urls)


def get_reading_list_urls():
    bookmarks = _read_file()
    reading_list = _reading_list(bookmarks)
    return _urls(reading_list)


def _read_file():
    with open(BOOKMARKS_PATH, 'rb') as f:
        return plistlib.load(f)


def _reading_list(bookmarks):
    return list(filter(lambda item: item['Title'] == READING_LIST_KEY, bookmarks['Children']))[0]


def _urls(reading_list):
    return [item['URLString'] for item in reading_list['Children']]


if __name__ == 'main':
    get_reading_list_urls()
