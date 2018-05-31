import discord, pycurl, sys
import cache


bases = {
	"https://imgur.com/{arg}" : [200],
	"https://i.cubeupload.com/{arg}{suffix}" : [200],
	"https://tinyimg.io/i/{arg}{suffix}" : [200],
	"https://www.youtube.com/watch?v={arg}" : [200]
}

suffixes = [
	".png",
	".jpg",
	".gif"
]


def try_url(url, curl_verb=False, agent=None):
	"""Actually do the http request"""
	from_cache = cache.get(url)

	if(from_cache != None):
		print("(CACHE) {:35}: {}".format(url, from_cache))
		return from_cache
	else:
		try:
			curl = pycurl.Curl()
			curl.setopt(curl.NOBODY, True)
			curl.setopt(curl.VERBOSE, curl_verb)
			if(agent != None):
				curl.setopt(curl.USERAGENT, agent)
			curl.setopt(curl.URL, url)
			curl.perform()
			code = curl.getinfo(pycurl.HTTP_CODE)
			cache.add(url, code)
			print("> HEAD  {:35}: {}".format(url, code))
			return code
		except:
			return str(sys.exc_info())


def try_urls(thing, verbose=False, agent=None):
	urls = []
	for key, value in bases.items():
		if("{suffix}" in key):
			for suffix in suffixes:
				urls.append((key, key.format(arg=thing, suffix=suffix)))
		else:
			urls.append((key, key.format(arg=thing, suffix="")))
			
	tries = {}
	for i, url in enumerate(urls):
		code = try_url(url[1], agent=agent)
		for found_code in bases[url[0]]:
			if((code == found_code) or (verbose==True)):
				tries[url[1]] = code
				break
	return tries



async def try_and_send(client, M, thing, verbose=False):
	await client.send_typing(M.channel)
	r = try_urls(thing, verbose=verbose, agent=client.curl_agent)
	out = ["<{}> - {}".format(url,code) for url, code in r.items()]
	out.sort()
	if(out == []):
		await client.send_message(M.channel, "`{thing}`: None found.".format(thing=thing))
	else:
		await client.send_message(M.channel, "\n".join(out))



async def check(client, M, argv):
	ulist = argv[1:]
	try:
		ulist.pop(ulist.index("-v"))
		verbose = True
	except:
		verbose = False
		
	if(ulist == []):
		await client.send_message(M.channel, "?")
	else:
		for url in ulist:
			await try_and_send(client, M, url, verbose=verbose)

async def getUserAgent(client, M, argv):
	await client.send_message(M.channel, "```\n"+client.curl_agent+"\n```")


if(__name__ == "__main__"):
	if("-v" in sys.argv):
		curl_verb = True
	else:
		curl_verb = False
	code = try_url("https://tinyimg.io/i/HlKgkKP.png", curl_verb=curl_verb)
	print(code)
