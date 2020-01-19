import csv
import os
import plistlib
import sys
import time


class URLFetcher(object):

    BOOKMARKS_PATH_SUFFIX = 'Library/Safari/Bookmarks.plist'
    READING_LIST_KEY = 'com.apple.ReadingList'

    def __init__(self, base_dir):
        self.filepath = os.path.join(base_dir, self.BOOKMARKS_PATH_SUFFIX)

    def reading_list_urls(self):
        return [item['URLString'] for item in self._reading_list()]

    def _reading_list(self):
        reading_list = list(filter(self._is_reading_list, self._bookmarks()))
        return reading_list[0]['Children']

    def _is_reading_list(self, item):
        return item['Title'] == self.READING_LIST_KEY

    def _bookmarks(self):
        with open(self.filepath, 'rb') as f:
            bookmarks = plistlib.load(f)
            return bookmarks['Children']


class URLExporter(object):

    CSV_HEADING = 'Reading List (in reverse chronological order)'

    def __init__(self, base_dir):
        self.urls = URLFetcher(base_dir).reading_list_urls()

    def export(self):
        with open(self._output_filename(), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.CSV_HEADING)
            for url in self.urls:
                writer.writerow(url)

    def _output_filename(self):
        return f'reading_list_urls_{self._timestamp()}.csv'

    @staticmethod
    def _timestamp():
        return time.ctime().replace(' ', '_')


if __name__ == '__main__':
    base_dir = sys.argv[1]
    URLExporter(base_dir).export()
