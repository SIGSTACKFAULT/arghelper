import json, discord, zlib
from settings import *

class Cache:
	def __init__(self):
		self.load()
	
	def save(self):
		if(ZIP_CACHE):
			with open(ZIP_CACHEFILE, "wb") as f:
				f.write(zlib.compress(self.ssave().encode()))
		else:
			with open(CACHEFILE, "w") as f:
				self.fsave(f)
	
	def load(self):
		try:
			if(ZIP_CACHE):
				with open(ZIP_CACHEFILE, "rb") as f:
					self.sload(zlib.decompress(f.read()).decode())
			else:
				with open(CACHEFILE) as f:
					self.fload(f)
		except FileNotFoundError:
			self.cache = {}
	
	def sload(self, s):
		try:
			self.cache = json.loads(s)
		except json.JSONDecodeError:
			print("JSONDecodeError: Cache is probably empty.")
			self.cache = {}
		
	def ssave(self):
		return json.dumps(self.cache, sort_keys=True, separators=(',',':'))
	
	
	def get(self, url):
		return self.cache.get(url, None)
	
	def add(self, url, code):
		self.cache[url] = code


	def __str__(self):
		return str(self.cache)

class Fake:
	def get(self, url):
		return None
	def add(self, url, code):
		pass

cache = Cache()
fake = Fake()

async def getcache(client, M, argv):
	cache.save()
	if(ZIP_CACHE):
		await client.send_file(ZIP_CACHEFILE)
	else:
		await client.send_file(CACHEFILE)

print("Cache ready!")
