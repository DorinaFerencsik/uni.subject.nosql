from datetime import datetime
import pymongo
conn = pymongo.MongoClient()
db = conn['testing']
test_coll = db['test_coll']


def main():
    test_obj = {'name': 'sec', 'title': 'last'}
    test_coll.insert_one(test_obj)
    print("inserted object: ")
    print(test_obj)

    oid = test_obj['_id']
    oid_str = str(oid)
    print('Generated object id: ', oid_str)
    generation_time = int(oid_str[0:8], 16)
    host = int(oid_str[8:14], 16)
    process_id = int(oid_str[14:18], 16)
    increment = int(oid_str[18:], 16)
    print('Date of object id generation: ')
    oid_date = datetime.fromtimestamp(generation_time)
    print(oid_date.strftime('%Y. %B %d. %H:%M:%S'))
    print('Host: ', str(host))
    print('Process id: ', str(process_id))
    print('Increment: ', str(increment))


if __name__ == "__main__":
    main()

