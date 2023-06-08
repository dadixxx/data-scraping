from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='db', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! This page has been viewed %s times.' % count

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
