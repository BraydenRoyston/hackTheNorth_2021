from .good_songs import insert_good_songs


def insert_raw_data(client):
    db = client['htn']
    collection = db['rawDatas']
    collection.delete_many({})
    insert_good_songs(collection=collection)
    # insert_bad_songs(client=client)
