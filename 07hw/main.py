import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "hahaha"


headers = {
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
@app.route('/r/<reddit_name>')
def testing(reddit_name):
    r = requests.get("https://www.reddit.com/r/" + reddit_name + "/.json", headers=headers)
    html = r.text
    parsed = json.loads(html)

    context = {
        'redditName': reddit_name,
        'posts': parsed['data']['children']
    }
    return render_template('reddit.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
