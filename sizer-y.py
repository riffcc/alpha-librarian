#!/usr/bin/python3

def human_read_to_byte(size):
    size_name = ("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    size = size.split()                # divide '1 GB' into ['1', 'GB']
    num, unit = float(size[0]), size[1]
    idx = size_name.index(unit)        # index in list of sizes determines power to raise it to
    factor = 1024 ** idx               # ** is the "exponent" operator - you can use it instead of math.pow()
    return num * factor

filesizes_list = open("x.txt", "r").read().splitlines()

countX = 1
totalsize = 0
for filesize in filesizes_list:
    print(countX)
    print(human_read_to_byte(filesize))
    countX += 1
    totalsize += human_read_to_byte(filesize)
    print(totalsize)