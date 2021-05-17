#!/usr/bin/python3
# Fetch torrent sizes
# TODO: Report number of files before we go etc
import os
from torrentool.api import Torrent
from fnmatch import fnmatch

root = '/opt/radio/collections'
pattern = "*.torrent"

alltorrentsize = 0

print("Thanks for using The Librarian.")

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            torrentstats = Torrent.from_file(os.path.join(path, name))
            alltorrentsize += torrentstats.total_size
            print('Torrent size ' + str(torrentstats.total_size) + ' for a total so far of ' + str(alltorrentsize))
            print('DEBUG' + os.path.join(path, name))

# Reading filesize
my_torrent = Torrent.from_file('/opt/radio/collections/arienscompanymanuals/archive.org/download/collection_01_ariens_manuals/collection_01_ariens_manuals_archive.torrent')
size = my_torrent.total_size  # Total files size in bytes.

print(size)