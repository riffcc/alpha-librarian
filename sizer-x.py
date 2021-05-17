#!/usr/bin/python3
# Fetch torrent sizes
# TODO: Report number of files before we go etc
import os
from fnmatch import fnmatch

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

root = '/opt/radio/collections'
pattern = "*.torrent"

alltorrentsize = 0

print("Thanks for using The Librarian.")

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):

            stream = os.popen('transmission-show ' + os.path.join(path, name))
            output = stream.read()
            parseable = output.splitlines()
            for line in parseable:
                if "Total Size" in line:
                    print(line)