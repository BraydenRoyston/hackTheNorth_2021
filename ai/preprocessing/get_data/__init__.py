import os
from typing import List
import lyricsgenius
import json


def insert_raw_data(client):
    dirname = os.path.dirname(__file__)

    db = client['htn']
    collection = db['rawDatas']

    collection.delete_many({})

    genius = lyricsgenius.Genius(os.environ.get("CLIENT_ACCESS_TOKEN"))

    with open(os.path.join(dirname, './bad_songs/bad.json')) as bad_songs_file:
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

    with open(os.path.join(dirname, './good_songs/good.json')) as good_songs_file:
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
