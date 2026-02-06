from typing import TypedDict, List

class syncedLyric(TypedDict): # List
    startTimeMs: float # second
    text: str

syncedLyricsList = List[syncedLyric]

class rawLrcJson(TypedDict):
    id: int
    name: str
    trackName: str
    artistName: str
    albumName: str
    duration: float # second
    instrumental: bool
    plainLyrics: str
    syncedLyrics: str

class lrcJson(TypedDict):
    id: int
    name: str
    trackName: str
    artistName: str
    albumName: str
    duration: float # second
    instrumental: bool
    plainLyrics: str
    syncedLyrics: syncedLyricsList