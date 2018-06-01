import json, discord

CACHEFILE = "cache.json"

class Cache:
	def __init__(self, *args, **kwargs):
		try:
			with open(CACHEFILE, "r") as f:
				self.blind_load(f)
		except json.decoder.JSONDecodeError:
			print("JSONDecodeError: Cache is probably empty.")
			self.cache = {}
	
	def blind_load(self, f):
		self.cache = json.loads(f.read())

	def save(self):
		with open(CACHEFILE, "w") as f:
			print(json.dumps(self.cache, sort_keys=True, separators=(',', ':')))
	
	def load(self):
		with open(CACHEFILE, "r") as f:
			self.blind_load(f)
	
	def get(self, url):
		return self.cache.get(url, None)
	
	def add(self, url, code):
		self.cache[url] = code

cache = Cache()

async def getcache(client, M, argv):
	cache.save()
	await client.send_file(CACHEFILE)

print("Cache ready!")

