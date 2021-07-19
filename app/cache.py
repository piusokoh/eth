# imports
from collections import OrderedDict

# declare main class LRUCache
class LRUCache:

	# create constructor to enforce cache capacity as class parameter
    # cache is implemented using Python's handy OrderedDict class that enforces order of entries
    # the last item in the dict is the most recently used and the first item is the least recently used
	def __init__(self, capacity: int):
		self.cache = OrderedDict() 
		self.capacity = capacity   

	# Implement the get function to retrieve a value given a key
    # Since we are using an OrderedDict, we can return the value corresponding to the key
	# that is queried in O(1) and return -1 if we
	# don't find the key in the dictionary / cache.
	# Also whenever a key is accessed, we move the key to the end
	# to show that it was recently used.
	def get(self, key):
		if key not in self.cache:
			return -1
		else:
			self.cache.move_to_end(key)
			return self.cache[key]

	# Implement the put function to insert a key and value into the cache
    # First, we add the key-value pair to the dictionary.
	# Secondly, we move the key to the end to show that it was recently used.
	# Third, we also check whether the length of the
	# Ordered Dictionary cache has exceeded its capacity,
	# If so we remove the first key (least recently used)
	def put(self, key, value):
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache) > self.capacity:
			self.cache.popitem(last = False)





