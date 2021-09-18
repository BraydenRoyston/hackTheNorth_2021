import os
from typing import List
import lyricsgenius
import json


def insert_good_songs(client):

    dirname = os.path.dirname(__file__)

    db = client['htn']
    collection = db['badSongs']

    genius = lyricsgenius.Genius(os.environ.get("CLIENT_ACCESS_TOKEN"))

    with open(os.path.join(dirname, './bad.json')) as bad_songs_file:
        bad_songs: List[dict] = json.load(bad_songs_file)

        for bad_song in bad_songs:
            song = genius.search_song(
                artist=bad_song['artist'], title=bad_song['song'])

            if song is None:
                continue

            result = {}

            result['artist'] = bad_song['artist']
            result['song'] = bad_song['song']
            result['lyrics'] = song.lyrics
            result['isGoodSong'] = 0

            collection.insert_one(result)
