collections_list = open("collections.txt", "r").read().splitlines()

for collection in collections_list:
    print(collection)

print(len(collections_list))