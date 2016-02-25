from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def yo():
    return 'Yo, Adrian! I did it!'

@app.route('/env')
def env():
    return '<br>'.join(['%s = %s' % (k, v) for k, v in os.environ.iteritems()])

@app.route('/counter')
def counter():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
