import csv
import os
import plistlib
import sys
import time

BOOKMARKS_PATH_SUFFIX = 'Library/Safari/Bookmarks.plist'
READING_LIST_KEY = 'com.apple.ReadingList'
CSV_HEADING = 'Reading List (in reverse chronological order)'


def export_reading_list_csv(base_dir):
    with open(f'reading_list_urls_{_timestamp()}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADING)
        for url in get_reading_list_urls(base_dir):
            writer.writerow(url)


def get_reading_list_urls(base_dir):
    bookmarks = _read_file(base_dir)
    reading_list = _reading_list(bookmarks)
    return _urls(reading_list)


def _timestamp():
    return time.ctime().replace(' ', '_')


def _read_file(base_dir):
    filepath = os.path.join(base_dir, BOOKMARKS_PATH_SUFFIX)
    with open(filepath, 'rb') as f:
        return plistlib.load(f)


def _reading_list(bookmarks):
    return list(filter(lambda item: item['Title'] == READING_LIST_KEY, bookmarks['Children']))[0]


def _urls(reading_list):
    return [item['URLString'] for item in reading_list['Children']]


if __name__ == '__main__':
    base_dir = sys.argv[1]
    export_reading_list_csv(base_dir)
