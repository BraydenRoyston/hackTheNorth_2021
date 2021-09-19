from dotenv import load_dotenv
from pymongo import MongoClient
from get_data import insert_raw_data
from add_features import fill_preprocessed
import sys
import os

load_dotenv()


def main():

    client = MongoClient('mongodb://localhost:27017/')

    if(len(sys.argv) > 1 and sys.argv[1] == "--reset"):
        insert_raw_data(client=client)

    fill_preprocessed(client=client)


if __name__ == "__main__":
    main()
