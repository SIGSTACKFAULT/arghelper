import json, discord

CACHEFILE = "cache.json"

cache = {}

def load_cache():
	global cache
	try:
		with open(CACHEFILE, "r") as f:
			cache = json.loads(f.read())
	except json.decoder.JSONDecodeError:
		print("JSONDecodeError: Cache is probably empty.")
		cache = {}

def save_cache():
	global cache
	with open(CACHEFILE, "w") as f:
		f.write(json.dumps(cache, sort_keys=True, separators=(',', ':')))
		
async def getcache(client, M, argv):
	save_cache()
	await client.send_file(M.channel, CACHEFILE)

def get(url):
	return cache.get(url, None)

def add(url, code):
	cache[url] = code
	save_cache()

try:
		load_cache()
except FileNotFoundError:
	from os import system
	system("touch " + CACHEFILE)
	print("No cache file found, creating one.")
	load_cache()
else:
	print("Cache ready!")

