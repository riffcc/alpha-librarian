#!/usr/bin/python3
# Download stuff from archive.org
# https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers

import internetarchive
import json

if __name__ == '__main__':
    collections_list = open("collections.txt", "r").read().splitlines()

    for collection in collections_list:
        print("Fetching " + collection )
        collection_files_path = "/opt/radio/ingest/" + collection
        collection_items_list = internetarchive.search_items('collection:' + collection)
        items_in_collection = collection_items_list.num_found
        counter = 0
        url_list = ""
        for item in collection_items_list:
            counter += 1
            print("Collecting URL " + str(counter) + "/" + str(items_in_collection))
            # get the item name out of the collection
            item_json = json.dumps(item)
            item_json_to_python = json.loads(item_json)
            identifier = item_json_to_python["identifier"]
            # build our URL to download
            url = "https://archive.org/download/" + identifier + "/" + identifier + "_archive.torrent"
            url_list = url_list + url
            url_list = url_list + "\n"
        file = open("/opt/radio/ingest/" + collection + ".txt", "w")
        file.write(url_list)
        file.close()