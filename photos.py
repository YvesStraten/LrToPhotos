#!/usr/bin/env python3

import os
from osxphotos.cli.batch_edit import photoscript_photo
import osxphotos

def main() -> None:
    path = os.path.expanduser("~/Pictures/Test.photoslibrary")
    photos = osxphotos.PhotosDB(path)

    for photo in photos.photos():
        editable = photoscript_photo(photo)
        editable.keywords = [ "nlah", "hello" ]

    # Remove the object, and refresh db
    del photos

    photos = osxphotos.PhotosDB(path)

    for photo in photos.photos():
        print(photo.keywords)

main()
