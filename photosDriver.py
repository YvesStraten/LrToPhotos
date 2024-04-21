#!/usr/bin/env python3

import os
import sys
import osxphotos
from osxphotos import photokit
from osxphotos.cli.batch_edit import photoscript_photo

from lrtools.lrcat import LRCatDB, LRCatException
from lrtools.lrselectgeneric import LRSelectException

from photos import PhotoEntity, PhotoList


def main() -> None:
    try:
        path = os.path.expanduser("~/Pictures/Test.photoslibrary")
        photos = osxphotos.PhotosDB(path)
    except:
        print("Could not open photos database")

    try:
        columns = "name,keywords"

        path = os.path.expanduser("~/Downloads/Lightroom Catalog.lrcat")
        lrdb = LRCatDB(path)
        rows = lrdb.lrphoto.select_generic(columns).fetchall()

    except LRCatException:
        print("Could not open lightroom database")

    except LRSelectException:
        print("No photos available")

    photosList = []

    for row in rows:

        if row[1] == None:
            photosList.append(PhotoEntity(row[0], []))
        else:
            keywordsArr = row[1].split(",")

            photosList.append(PhotoEntity(row[0], keywordsArr))

    Catalog = PhotoList()

    Catalog.setPhotos(photosList)

    photosWithKeywords = Catalog.getPhotosWithKeywords()
    for photo in photosWithKeywords:
        print(photo)

    print("Number of photos:", len(photosWithKeywords))
    print("Apple db")

    for photo in photos.photos():
        print(photo.filename)
        print(photo)

    # for photo in photos.photos():
    #     editable = photoscript_photo(photo)
    #     editable.keywords = [ "nlah", "hello" ]

    # # Remove the object, and refresh db
    # del photos

    # photos = osxphotos.PhotosDB(path)

    # for photo in photos.photos():
    #     print(photo.keywords)


main()
