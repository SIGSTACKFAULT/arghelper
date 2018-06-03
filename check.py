#!/usr/bin/python3
import discord, pycurl, sys
import try_url, settings

from bases import bases

suffixes = [
	".png",
	".jpg",
	".gif"
]

def permutations(thing):
	# get 'em all, even if the base doesn't have a suffix:
	p = []
	for base in bases:
		for suffix in suffixes:
			# we need an immutable type for set(); we'll turn this into a dict later.
			p.append((base.format(thing=thing, suffix=suffix), base))

	# remove dupes
	q = list(set(p))

	#now make it back into a big dict.
	return {url:base for (url, base) in p}

def try_urls(thing, opts={}):
	p = permutations(thing)
	out = []
	for permutation, base in p.items():
		code = try_url.try_url(permutation, opts=opts)
		if((code in bases[base])):
			out.append("{url} - {code}".format(url=permutation, code=code))
		elif(opts.get("verbose", False) == True):
			out.append("<{url}> - {code}".format(url=permutation, code=code))
	
	o = out#.sort()
	return o

async def try_and_send(client, M, thing, opts={}):
	await client.send_typing(M.channel)
	out = try_urls(thing, opts=opts)
	if(out == []):
		await client.send_message(M.channel, "`{thing}`: None found.".format(thing=thing))
	else:
		await client.send_message(M.channel, "\n".join(out))


def parse_flags(argv):
	opts = {
		"nocache" : False,
		"verbose" : False,
	}
	opt_map = {
		"nocache" : {
			True : ["-c", "--nocache"],
			False: ["-C", "--cache"]
		},
		"verbose" : {
			True : ["-v", "--verbose"]
		},
	}
	for option, triggers in opt_map.items():
		for trigger, flags in triggers.items():
			for flag in flags:
				for i, arg in enumerate(argv):
					if(arg == flag):
						opts[option] = trigger
						argv.pop(i)
				
	return opts, argv
	

async def check(client, M, argv):
	"""The actual function called by main"""
	opts, argv = parse_flags(argv)
	ulist = argv[1:]
	
	if(ulist == []):
		await client.send_message(M.channel, "?")
	else:
		for url in ulist:
			await try_and_send(client, M, url, opts=opts)
	try_url.cache.cache.save()



if(__name__ == "__main__"):
	import sys
	opts, argv = parse_flags(sys.argv)
	ulist = argv[1:]
	for url in ulist:
		try_urls(url, opts=opts)
	try_url.cache.cache.save()
