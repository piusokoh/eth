# imports
import time
import requests #used for sending the request to Cloudfare endpoint
from cache import LRUCache # cache module is from the file cache.py in the same path as this file
from flask import Flask, render_template, request, jsonify

# initialise the Flask app
app = Flask(__name__)


# initialize the cache with a capacity of 128
cache = LRUCache(128)



# This endpoint retrieves blocks by id by calling the eth_getBlockByNumber Cloudfare endpoint
# A cache of capacity 128 is used to store recently accessed blocks for faster retrieval if needed
# The function run by this endpoint takes the block id as argument
# first the cache is checked using the block id as key 
#   - if the key exists in the cache, the response is gotten from the cache which is much faster than calling cloudfare endpoint
#   - if the key is not found in the cache, a call is made to the cloudfare endpoint to fetch the data
#   - the key and response are then added to the cache for faster recovery next time
@app.route('/block/<id>', methods=['GET'])
def get_block(id):
    
    response = cache.get(id)                # check for the id in the cache
    if response != -1:                      # id is found in cache
        print('found in cache')
        return response                     # return value from the cache
    else:                                   # id is not found in cache
        headers = {                         # prepare request headers and data
            'Content-Type': 'application/json',
        }

        data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["'+id+'", true],"id":1}'

        response = requests.post('https://cloudflare-eth.com/', headers=headers, data=data) # send request to cloudfare endpoint
        cache.put(id, response.json())  # put the response from cloudfare endpoint in the cache
        return response.json() # return response retrieved from cloudfare endpoint


if __name__ == '__main__':
    app.run(debug=True)
