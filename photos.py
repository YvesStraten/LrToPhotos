class PhotoEntity:
    def __init__(self, name: str, keywords: list[str]) -> None:
        self.filename = name
        self.keywords = keywords

    def getFileName(self) -> str:
        return self.filename

    def getKeywords(self) -> list[str]:
        return self.keywords

    def __str__(self) -> str:
        return f"Photo with filename {self.filename} and keywords {self.keywords}"

    def __eq__(self, other) -> bool:
        return self.filename == other.filename


class PhotoList:
    def __init__(self) -> None:
        self.photos = []

    def addPhoto(self, photo: PhotoEntity) -> None:
        self.photos.append(photo)

    def setPhotos(self, photos: list[PhotoEntity]) -> None:
        self.photos = photos

    def getPhotos(self) -> list[PhotoEntity]:
        toReturn = [  ]

        for photo in self.photos:
            toReturn.append(photo)

        return toReturn

    def getPhotosWithKeywords(self) -> list[PhotoEntity]:
        toReturn = []
        for photo in self.photos:
            if len(photo.keywords) > 0:
                toReturn.append(photo)

        return toReturn
