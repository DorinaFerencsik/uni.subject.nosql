# answer for 01 is 42 :)

# restore database & collection from dump file (run mongorestore) before running this script
# the answer for 02 will be 795
import pymongo

conn = pymongo.MongoClient()
db = conn['mongolab']
coll = db['numbers']


def main():
    cursor = coll.find()
    total = 0
    for doc in cursor:
        if doc['value'] % 5 == 0:
            total += doc['value']
    total = int(total)
    print("The answer is: {}".format(total))


if __name__ == "__main__":
    main()


