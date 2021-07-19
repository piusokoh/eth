# eth
This project implements a caching proxy for eth_getBlockByNumber. 
The project is implemented as a Flask app that exposes an endpoint /block/< id > where id is the id of the block whose details we want to fetch from Cloudfare

Instructions for running the code (The project was tested in Python 3.8 but should work in any Python version from 3.5)
  1. Clone the repo
  2. Run pip install -r requirements.txt
  3. cd /app
  4. Run python app.py (This should start the app which will be running on http://127.0.0.1:5000/)
  5. Visit this URL in your browser http://127.0.0.1:5000/block/< id > e.g. http://127.0.0.1:5000/block/0x1b4
  
You will observe that the first time this endpoint is hit, it makes the call to cloudfare to fetch the response. But if there is an attempt to access the same block id again, the response is much faster as the response is sent from the cache and no call is made to the cloudfare API the second time around. The caching mechanism used is LRU (implemented using Python OrderedDict) with a capacity of 128 entries.
