import time
import redis 
from flask import Flask
from socket import gethostname

def get_hostname():
    return gethostname()

app = Flask(__name__)
# Redis is the hostname of the redis container
# Using default port for Redis 6379
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    hostname = get_hostname()
    return 'Hello from Docker! I have been seen {} times on host: {}\n'.format(count, hostname)