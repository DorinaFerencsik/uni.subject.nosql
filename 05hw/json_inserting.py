import json
import os

import pymongo

conn = pymongo.MongoClient()
db = conn['radio']
coll = db['slay']


def main():
    coll.delete_many({})
    print('Deleted everything from collection for clean start...')
    data_path = os.getcwd() + '\\05hw\\data\\'
    json_file_names = [json_name for json_name in os.listdir(data_path) if json_name.endswith('.json')]

    for index, js in enumerate(json_file_names):
        with open(data_path + js) as json_file:
            json_text = json.load(json_file)
            coll.insert_one(json_text)


if __name__ == '__main__':
    main()
