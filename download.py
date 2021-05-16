#!/usr/bin/python3
# Download stuff from archive.org
# https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers

import internetarchive
import json
import requests
import os
from tqdm import tqdm

if __name__ == '__main__':
    collections_list = open("collections.txt", "r")
    for collection in collections_list:
        collection_files_path = "/opt/radio/ingest/" + collection
        try:
            os.makedirs(collection_files_path, exist_ok=True)
            print("Directory '%s' created successfully" % collection_files_path)
        except OSError as error:
            print("Directory '%s' already existed." % collection_files_path)
        collection_items_list = internetarchive.search_items('collection:' + collection)
        items_in_collection = collection_items_list.num_found
        counter = 0
        for item in collection_items_list:
            counter += 1
            print("Downloading item " + str(counter) + "/" + str(items_in_collection))
            # get the item name out of the collection
            item_json = json.dumps(item)
            item_json_to_python = json.loads(item_json)
            identifier = item_json_to_python["identifier"]
            # build our URL to download
            url = "https://archive.org/download/" + identifier + "/" + identifier + "_archive.torrent"
            response = requests.get(url, stream=True)

            with open(collection_files_path + "/" + identifier + ".torrent", "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)
                handle.close