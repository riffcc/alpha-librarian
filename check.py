#!/usr/bin/python3
# This tool is designed to check each collection in the radio folders, and ensure it was retrieved correctly and fully.
# Currently it only supports content from archive.org, this will change later.
import os
import internetarchive
from fnmatch import fnmatch
from glob import glob

# Enable quiet mode - only log collections with issues, rather than all collections.
quiet = 1

# Grab a list of collections from the collections folder, based on the folder names.
collections_list = [os.path.basename(x) for x in glob("/opt/radio/collections/*")]

# For each collection...
for collection in collections_list:
    # Retrieve the latest list of items from archive.org that make it up
    collection_items_list = internetarchive.search_items('collection:' + collection)
    # and store how many that is.
    items_in_collection = collection_items_list.num_found

    # Search within a particular collection's folder
    collroot = '/opt/radio/collections/' + collection
    pattern = "*.torrent"

    # Set our counter to zero to start with
    torrentcount = 0

    # For each .torrent file we find in that collection folder, increment our counter
    for path, subdirs, files in os.walk(collroot):
        for name in files:
            if fnmatch(name, pattern):
                torrentcount += 1

    # Loud - Print a report for every collection of how many items have been downloaded vs how many could be.
    if quiet == 0:
        print(str(torrentcount) + " out of " + str(items_in_collection) + " downloaded")

    # Quiet - Only print reports for collections that seem to have issues.
    if quiet == 1:
        if not torrentcount == items_in_collection:
            print("Only " + str(torrentcount) + " out of " + str(items_in_collection) + " downloaded (" + collection + ")")
