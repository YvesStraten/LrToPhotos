#!/usr/bin/env python3

import os
import sys
import osxphotos
from osxphotos.cli.batch_edit import photoscript_photo

from lrtools.lrcat import LRCatDB, LRCatException
from lrtools.lrselectgeneric import LRSelectException

from photos import PhotoEntity, PhotoList

def transferKeywords(applePath: str, LightRoomPath:str) -> None:
    try:
        photos = osxphotos.PhotosDB(applePath)
    except:
        print("Could not open photos database")

    try:
        columns = "name,keywords"

        lrdb = LRCatDB(LightRoomPath)
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

    print("Number of photos to transfer:", len(photosWithKeywords))

    # for photo in photos.photos():
    #     editable = photoscript_photo(photo)
    #     editable.keywords = [ "nlah", "hello" ]

    # # Remove the object, and refresh db
    # del photos

    # photos = osxphotos.PhotosDB(path)

    # for photo in photos.photos():
    #     print(photo.keywords)


def main() -> None:
    args = sys.argv

    helpMenu = (
        "Photos Keyword transferer \n",
        "Usage: python photosDriver.py <path to .photoslibrary> <path to .lrcat>",
        "All paths are relative, e.g ~/User/Downloads"
    )

    if len(args) > 3 or len(args) == 1:
        for item in helpMenu:
            print(item)

    else:
        try:
            photosPath = os.path.expanduser(sys.argv[1])
            lrcatPath = os.path.expanduser(sys.argv[2])

            if not os.path.exists(photosPath) or not os.path.exists(lrcatPath):
                raise Exception()
            else:
                transferKeywords(photosPath, lrcatPath)

        except:
            print("Wrong paths to catalogs \n")
            for item in helpMenu:
                print(item)

main()
