# the templates folder with the result.html is required for using the /hw1/3 endpoint
# also the database restore is needed as specified in 02.py
# the answer will be 5100

from flask import Flask, render_template
import pymongo

conn = pymongo.MongoClient()

db = conn['mongolab']
coll = db['numbers']

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route('/hw1/3')
def total():
    cursor = coll.find()
    total_count = 0
    for doc in cursor:
        total_count += doc['value']
    #
    print('Total count: ', str(total_count))
    context = {
        'result': int(total_count)
    }
    return render_template('result.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
