import os
from typing import List
import lyricsgenius
import json


def insert_good_songs(collection):

    dirname = os.path.dirname(__file__)

    genius = lyricsgenius.Genius(os.environ.get("CLIENT_ACCESS_TOKEN"))

    with open(os.path.join(dirname, './good.json')) as good_songs_file:
        good_songs: List[dict] = json.load(good_songs_file)

        for good_song in good_songs:
            song = genius.search_song(
                artist=good_song['artist'], title=good_song['song'])

            if song is None:
                continue

            result = {}

            result['artist'] = good_song['artist']
            result['song'] = good_song['song']
            result['lyrics'] = song.lyrics
            result['isGoodSong'] = 1

            collection.insert_one(result)
