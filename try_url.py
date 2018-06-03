import pycurl, cache

def blind_try(url, agent=None):
	"""Blindly return the http code for a url. Don't ask any questions."""
	curl = pycurl.Curl()
	curl.setopt(curl.NOBODY, True)
	curl.setopt(curl.URL, url)
	if(agent):
		curl.setopt(curl.USERAGENT, agent)
	curl.perform()
	code = curl.getinfo(pycurl.HTTP_CODE)
	print("> HEAD   {url:40}:{code}".format(url=url, code=code))
	return code

def blind_try_cached(url, C, agent=None):
	"""Blindly look up the url, respecting the cache.
	Pass cache as cache.fake if you don't want me to look up in the cache."""
	
	response = C.get(url)
	if(response == None):
		response = blind_try(url, agent=agent)
		C.add(url, response)
	else:
		print("(CACHED) {url:40}:{code}".format(url=url, code=response))
	
	return response

def try_url(url, opts={}):
	"""Actually use this function"""
	
	agent = opts.get("useragent")
	nocache = opts.get("nocache", False)
	if(nocache == True):
		arg_cache = cache.fake
	else:
		arg_cache = cache.cache
	try:
		r = blind_try_cached(url, arg_cache, agent=agent)
	except pycurl.error:
		return None
	else:
		return r
