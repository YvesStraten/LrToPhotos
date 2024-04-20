#!/usr/bin/env python3

import os
import sys
import osxphotos
from osxphotos.cli.batch_edit import photoscript_photo

from lrtools.lrcat import LRCatDB, LRCatException
from lrtools.lrselectgeneric import LRSelectException
from lrtools.display import display_results


def main() -> None:
    try:
        path = os.path.expanduser("~/Downloads/Lightroom Catalog.lrcat")
        lrdb = LRCatDB(path)
    except LRCatException:
        print("Could not access")

    columns = "name,keywords"

    try:
        rows = lrdb.lrphoto.select_generic(columns).fetchall()

    except LRSelectException:
        print("No photo")



    counter = 0
    photosWithKeywords = [  ]

    for row in rows:

        if row[1] != None:
            photosWithKeywords.append([row[0], row[1]])


            counter += 1

    print(counter)

    sort = sorted(photosWithKeywords, key=lambda field: field[1])
    # for photo in photosWithKeywords:
    #     print("filename:", photo[0], "Tags: ", photo[1])
    #     # for index, field in enumerate(row):
    #     #     print(index)
    #     #     print(field)
    #     #
    for field in sort:
        for index, _ in enumerate(field):
            print("filename:", field[0], "Tags: ", field[1])

    # path = os.path.expanduser("~/Pictures/Test.photoslibrary")
    # photos = osxphotos.PhotosDB(path)

    # for photo in photos.photos():
    #     editable = photoscript_photo(photo)
    #     editable.keywords = [ "nlah", "hello" ]

    # # Remove the object, and refresh db
    # del photos

    # photos = osxphotos.PhotosDB(path)

    # for photo in photos.photos():
    #     print(photo.keywords)

main()
