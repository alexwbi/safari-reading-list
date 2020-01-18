import csv
import os
import plistlib
import time

BOOKMARKS_PATH = os.path.join(os.getcwd(), 'Library/Safari/Bookmarks.plist')
READING_LIST_KEY = 'com.apple.ReadingList'
CSV_HEADING = 'Reading List (in reverse chronological order)'


def export_reading_list_csv():
    with open(f'reading_list_urls {time.ctime()}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows([CSV_HEADING] + get_reading_list_urls())


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


if __name__ == '__main__':
    export_reading_list_csv()
