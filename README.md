# safari-reading-list
After moving to better browsers (Brave) and offline reading lists (Pocket), I needed a way to rescue hundreds of saved articles in Reading List without slogging through Safari's clunky Reading List UI. Here's how.


#### Exporting Reading List articles
To generate a CSV of all Reading List articles, run the python script like this:
`python reading_list_urls.py <your_base_dir>`, for example `python reading_list_urls.py '/Users/Alex'`.


#### Adding articles to Pocket or Evernote
To add all articles to Pocket or Evernote, refer to this nifty bash script from @arcadia168: https://gist.github.com/arcadia168/0bade46a6bb720395f56.

Note that the script to copy all Safari Reading List articles into a text file includes image URLs as well, which my python script excludes. The
script for adding articles to Pocket/Evernote through emails works well though.

Sidenote: It's nice that Pocket makes it really easy to export all of your saved links with https://getpocket.com/export.
